import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer, pipeline
from settings import model_name, system_message, prompt_template


def initialize_model_and_tokenizer(model_name_or_path):
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available. Please check your GPU installation.")

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        device_map="cuda"
    ).to('cuda')
    return model, tokenizer

def generate_text(model, tokenizer, service):
    prompt = prompt_template.format(service=service)
    full_prompt = f'''system
    {system_message}|im_end|>
    user
    {prompt}
    assistant
    '''

    generation_params = {
        "do_sample": True,
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_new_tokens": 512,
        "repetition_penalty": 1.1
    }

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        **generation_params
    )

    pipe_output = pipe(full_prompt)[0]['generated_text']
    # Извлекаем ответ ассистента из общего текста
    assistant_response = pipe_output.split("assistant\n", 1)[-1]
    return assistant_response.strip()

model, tokenizer = initialize_model_and_tokenizer(model_name)

output_text = generate_text(model, tokenizer, "Потребительский кредит")
