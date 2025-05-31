import torch, os
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast

# Singleton for the model instance
model_instance = None


def get_model():
    global model_instance
    if model_instance is None:
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        print("MPS backend available:", torch.backends.mps.is_available())
        print("MPS backend built:", torch.backends.mps.is_built())
        model_path = os.getenv("MODEL_PATH", "/Users/conai/.llama/checkpoints/Llama3.1-8B")
        task = os.getenv("TASK", "text-generation")
        print(f"Loading model from: {model_path} with task: {task}")

        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float32,
            device_map="auto",
            low_cpu_mem_usage=True,
            ignore_mismatched_sizes=True
        ).to(device)

        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        custom_pipeline = pipeline(
            task,
            model=model,
            tokenizer=tokenizer,
            max_length=128,
            temperature=0.9,
            top_p=0.9,
            top_k=50,
            truncation=True
        )
        model_instance = HuggingFacePipeline(pipeline=custom_pipeline)
        print("Model loaded successfully.")
    return model_instance


def load_llama_model(model_path, task):
    try:
        print(f"Loading model from: {model_path}")
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        print("MPS backend available:", torch.backends.mps.is_available())
        print("MPS backend built:", torch.backends.mps.is_built())

        # Load the tokenizer and model from the specified path
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        # tokenizer = LlamaTokenizer.from_pretrained(model_path)
        # model = AutoModelForCausalLM.from_pretrained(model_path,
        #                                              torch_dtype=torch.float32,
        #                                              device_map="auto",  # Enables device map
        #                                              low_cpu_mem_usage=True,  # Reduce memory usage during loading
        #                                              ignore_mismatched_sizes=True).to(device)

        model = model_instance

        # print("Device Map:", model.hf_device_map)
        print("MPS backend available:", torch.backends.mps.is_available())
        print(f"Model is running on: {next(model.parameters()).device}")

        # model = AutoModelForCausalLM.from_pretrained(
        #     model_path,
        #     device_map="auto",   # This will auto-assign the model to the correct device
        #     load_in_8bit=True    # Optional: For lower memory usage if your hardware supports it
        # )

        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        # Create a generation pipeline
        custom_pipeline = pipeline(
            task,
            model=model,
            tokenizer=tokenizer,
            max_length=128,
            temperature=0.9,  # Increase temperature for more creativity
            top_p=0.9,  # Nucleus sampling to include diverse tokens
            top_k=50,  # Consider the top 50 tokens at each step
            truncation=True  # Enable truncation to avoid excessive length
        )

        # Wrap the pipeline in LangChain's HuggingFacePipeline
        llm = HuggingFacePipeline(pipeline=custom_pipeline)

        return llm
    except Exception as e:
        print(f"Error loading model: {e}")
        raise
