from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from settings import (
    negative_prompt,
    num_inference_steps,
    height,
    width,
)

from transformers import LoRA

def init_model(model_path, lora_path):
    # Загрузка модели Stable Diffusion
    stable_diffusion_pipe = StableDiffusionPipeline.from_single_file(
        model_path,
        local_files_only=True,
        force_download=False,
        token=False,
        use_safetensors=True,
    ).to("cuda")

    # Загрузка LoRA адаптера и интеграция с моделью
    lora_adapter = LoRA.from_pretrained(lora_path)
    stable_diffusion_pipe.model.transformer = lora_adapter(stable_diffusion_pipe.model.transformer)

    # Установка планировщика
    stable_diffusion_pipe.scheduler = DPMSolverMultistepScheduler.from_config(
        stable_diffusion_pipe.scheduler.config
    )

    return stable_diffusion_pipe


def gen_logo(model, prompt):
    logo = model.stable_diffusion_pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps,
        height=height,
        width=width,
    ).images[0]
    return logo
