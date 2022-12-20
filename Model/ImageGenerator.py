import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from torch import autocast

class ImageGenerator:
    def __init__(self):
            self.m_modelID = "stabilityai/stable-diffusion-2-1"
            self.m_device = "cuda"

            self.m_pipeline = StableDiffusionPipeline.from_pretrained(self.m_modelID, revision="fp16", torch_dtype=torch.float16)
            self.m_pipeline.scheduler = DPMSolverMultistepScheduler.from_config(self.m_pipeline.scheduler.config)
            self.m_pipeline = self.m_pipeline.to(self.m_device)
            self.m_pipeline.enable_attention_slicing()

    def generateImage(self, prompt, width=768, height=768, numInferenceSteps=50, guidanceScale=7.5, seed=0):
            generator = torch.Generator(self.m_device).manual_seed(seed)
            image = self.m_pipeline(prompt, height=height, width=width, num_inference_steps=numInferenceSteps, guidance_scale=guidanceScale, generator=generator).images[0]
            return image

        