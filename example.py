import transformers

# Load the GPT-3 model
model = transformers.AutoModel.from_pretrained("microsoft/DialoGPT-medium")

# Create a tokenizer
tokenizer = transformers.AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")

# Define the input text
input_text = "Hello, how are you today?"

# Encode the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Generate a response
response = model.generate(input_ids)

# Decode the response
response_text = tokenizer.decode(response[0], skip_special_tokens=True)

print(response_text)
