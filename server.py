from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

# טעינת המודל
model_name = "deepseek/DeepSeek-V3"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get("text", "")

    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200, do_sample=True, temperature=0.7)
    
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)