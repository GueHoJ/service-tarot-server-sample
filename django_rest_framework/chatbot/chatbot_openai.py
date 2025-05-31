from django.conf import settings
from openai import OpenAI
from openai import AsyncOpenAI
from asgiref.sync import sync_to_async
import json

from app.utils.common_utils import log_info
from chatbot.utils import get_gpt_parameters, store_message, update_message, update_conversation_history

aclient = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def chat_with_gpt(messages, stop=None, temperature=0.7, max_tokens=150):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop)
    # print(f"response : {response}")
    return response.choices[0].message.content


async def chat_with_gpt_stream(messages, model="gpt-3.5-turbo", stop=None, temperature=0.7, max_tokens=150):
    try:
        stream = await aclient.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop,
            stream=True)
        async for chunk in stream:
            # Directly access the "choices" and "delta" fields
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                # Only yield non-empty content
                print(content, end="", flush=True)  # Optional for CLI debug
                yield content  # Yield the content chunk

    except Exception as e:
        print(f"Error during streaming: {e}")
        yield f"Error: {e}"


async def chat_with_gpt_params_stream(chatbot_params, user_id=None, session_id=None):
    # Wrap both synchronous functions
    get_gpt_parameters_async = sync_to_async(get_gpt_parameters)
    store_message_async = sync_to_async(store_message)
    update_message_async = sync_to_async(update_message)
    update_conversation_history_async = sync_to_async(update_conversation_history)

    params = await get_gpt_parameters_async(user_id=user_id, session_id=session_id)

    log_info(f"chat_with_gpt_params_stream chatbot_params: {chatbot_params}\n"
             f"chat_with_gpt_params_stream params: {params}")

    # Extract messages from chatbot_params or initialize if not present
    messages = chatbot_params.get("messages", [])

    # Get the last message
    await save_last_message(messages, session_id, user_id, store_message_async)

    # Extract the system_prompt from chatbot_params (could be None or a dict)
    system_prompt_dict = chatbot_params.get("system_prompt")

    if system_prompt_dict and system_prompt_dict.get("role") == "system":
        # We have a system message from the user
        system_prompt_content = system_prompt_dict.get("content", "")

        if messages and messages[0].get("role") == "system":
            # Update the content of the first system message
            messages[0]["content"] = system_prompt_content
            log_info(f"Updated existing system message to: {system_prompt_content}")

            await update_system_message(messages[0], session_id, user_id, update_message_async)
        else:
            # Insert a new system message at the beginning
            system_message = {
                "role": "system",
                "content": system_prompt_content
            }
            messages.insert(0, system_message)
            log_info(f"Inserted new system message: {system_prompt_content}")

            await update_system_message(system_message, session_id, user_id, update_message_async)
    else:
        # If the user did NOT pass a system_prompt or it's missing the correct structure,
        # ensure there's at least one default system message:
        if not messages or messages[0].get("role") != "system":
            system_message = {
                "role": "system",
                "content": params.get("description","You are a helpful assistant.")
            }
            messages.insert(0, system_message)
            log_info("Inserted default system prompt from DB")

            await update_system_message(system_message, session_id, user_id, update_message_async)

    config_name = chatbot_params.get("config_name", params.get("config_name"))
    model = chatbot_params.get("model", params["model"])
    messages = messages
    temperature = chatbot_params.get("temperature", params["temperature"])
    max_tokens = chatbot_params.get("max_tokens", params["max_tokens"])
    stop = chatbot_params.get("stop_sequences", params["stop_sequences"])
    top_p = chatbot_params.get("top_p", params["top_p"])
    frequency_penalty = chatbot_params.get("frequency_penalty", params["frequency_penalty"])
    presence_penalty = chatbot_params.get("presence_penalty", params["presence_penalty"])

    log_info(f"GPT Parameters:\n"
             f"config_name: {config_name}\n"
             f"model: {model}\n"
             f"messages: {messages}\n" 
             f"temperature: {temperature}\n"
             f"max_tokens: {max_tokens}\n"
             f"stop: {stop}\n"
             f"top_p: {top_p}\n"
             f"frequency_penalty: {frequency_penalty}\n"
             f"presence_penalty: {presence_penalty}")


    try:
        stream = await aclient.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stream=True
        )

        # Collect the full response to add to conversation history
        full_response = ""
        async for chunk in stream:
            print(chunk, end="", flush=True)  # Optional for CLI debug
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                print(content, end="", flush=True)  # Optional for CLI debug
                yield content

        # Add the assistant's response to the conversation history
        messages.append({"role": "assistant", "content": full_response})

        # Get the last message
        await save_last_message(messages, session_id, user_id, store_message_async)
        
        # You might want to yield the updated messages as a special message
        print(json.dumps({"type": "messages_update", "messages": messages}))
        await manage_conversation_history(messages, session_id, user_id, update_conversation_history_async)
        
        # Yield end of message signal
        yield json.dumps({"type": "message_end", "message": "end of the message"})

    except Exception as e:
        print(f"Error during streaming: {e}")
        yield f"Error: {e}"


async def update_system_message(message, session_id, user_id, update_message_async):
    log_info(f"System message: {message}")
    await update_message_async(message, user_id=user_id, session_id=session_id)


async def save_last_message(messages, session_id, user_id, store_message_async):
    last_message = messages[-1] if messages else None
    log_info(f"Last message: {last_message}")
    await store_message_async(last_message, user_id=user_id, session_id=session_id)

async def manage_conversation_history(conversation_history, session_id, user_id, update_conversation_history_async):
    log_info(f"Conversation history: {conversation_history}")
    await update_conversation_history_async(conversation_history, user_id=user_id, session_id=session_id)


def chatbot():
    conversation_history = []
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        print(f"message check : {conversation_history}")

        user_input = input("Human: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break

        # Append user input to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Add a system prompt to guide the AI's behavior
        system_prompt = {"role": "system", "content": "Always say done when your answer is finished."}

        # Combine the system prompt and conversation history
        messages = [system_prompt] + conversation_history

        # Call OpenAI API
        try:
            ai_response = chat_with_gpt(messages, stop=["bye", "exit", "quit", "done"])
            print(f"Chatbot: {ai_response}")

            # Append AI response to the conversation history
            conversation_history.append({"role": "assistant", "content": ai_response})
        except Exception as e:
            print(f"Error: {e}")
            break


def chatbotStream():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    print("Chatbot: Hi! What can I help you?\n", end="", flush=True)

    while True:
        user_input = input("Human: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\nChatbot: Goodbye!")
            break

        # Append user input to the messages
        messages.append({"role": "user", "content": user_input})

        # Stream response
        assistant_response = ""
        for chunk in chat_with_gpt_stream(messages):
            print(chunk, end="", flush=True)  # Print each chunk in real time
            assistant_response += chunk  # Collect the full response

        print("\n")  # Add a newline after the full response

        # Append the assistant's response to the messages
        messages.append({"role": "assistant", "content": assistant_response})


if __name__ == "__main__":
    chatbotStream()
