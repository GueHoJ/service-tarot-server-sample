from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
import os

from transformers.models.auto.tokenization_auto import AutoTokenizer


def convert_model(input_dir, output_dir):
    # Debugging: Check if required files exist
    print("Directory:", input_dir)
    print("Files in directory:", os.listdir(input_dir))

    required_files = ["tokenizer.model", "config.json", "consolidated.00.pth"]
    for file in required_files:
        print(f"Checking for {file}: {'Found' if os.path.exists(os.path.join(input_dir, file)) else 'Missing'}")
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(input_dir, use_fast=True, legacy=True)
    print("Tokenizer object:", tokenizer)
    tokenizer.save_pretrained(output_dir)

    # Load and consolidate weights
    weight_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.startswith("consolidated.")]
    weight_files.sort()  # Ensure correct order

    # Combine weights into a single state_dict
    state_dict = {}
    for weight_file in weight_files:
        print(f"Loading weights from {weight_file}")
        state_dict.update(torch.load(weight_file, map_location="cpu"))

    # Save consolidated weights as a single file
    torch.save(state_dict, os.path.join(output_dir, "pytorch_model.bin"))
    print("Weights consolidated and saved as pytorch_model.bin.")

    # Load model configuration
    model = LlamaForCausalLM.from_pretrained(
        pretrained_model_name_or_path=output_dir,  # We're not loading from a standard pretrained directory
        state_dict=state_dict,
        config=os.path.join(input_dir, "config.json"),
        local_files_only=True  # Explicitly use local files
    )
    print("Model loaded successfully.")

    # Save model in Hugging Face format
    model.save_pretrained(output_dir)
    print("Model saved successfully in Hugging Face format.")


input_dir = "/Users/conai/.llama/checkpoints/Llama3.1-70B-Instruct"
output_dir = "/Users/conai/.llama/checkpoints/Llama3.1-70B-Instruct-HF"
os.makedirs(output_dir, exist_ok=True)
convert_model(input_dir, output_dir)
