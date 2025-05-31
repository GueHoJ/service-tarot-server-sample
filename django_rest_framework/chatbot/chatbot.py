from django.conf import settings
from llama_cpp import Llama

llm = Llama(model_path="./models/Llama-3.2-3B-Instruct-uncensored-Q8_0.gguf", n_gpu_layers=1, n_ctx=2048)


def chat_with_llama(prompt, max_tokens=100):
    response = llm(prompt, max_tokens=max_tokens, stop=["Human:", "\n"], echo=True)
    return response['choices'][0]['text'].strip()


def chatbot():
    conversation_history = ""
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("Human: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break

        conversation_history += f"Human: {user_input}\nAI:"
        response = chat_with_llama(conversation_history)
        ai_response = response.split("AI:")[-1].strip()

        print(f"Chatbot: {ai_response}")
        conversation_history += f" {ai_response}\n"


if __name__ == "__main__":
    chatbot()
