from huggingface_hub import hf_hub_download

# Specify the repository and file
repo_id = "TheBloke/Llama-2-7B-Chat-GGML"
filename = "llama-2-7b-chat.ggmlv3.q4_0.bin"

# Download to a local directory
model_path = hf_hub_download(repo_id=repo_id, filename=filename, local_dir="./models")
print(f"Model downloaded to: {model_path}")