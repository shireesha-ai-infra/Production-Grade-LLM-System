from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")

lora = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj","v_proj"])
model = get_peft_model(model, lora)