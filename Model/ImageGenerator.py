import torch
from diffusers import StableDiffusionPipeline
from torch import autocast

class ImageGenerator:
    def __init__(self, accessToken:str):
            self.m_accessToken = accessToken
            self.m_modelID = "CompVis/stable-diffusion-v1-4"
            self.m_device = "cuda"

            self.m_pipeline = StableDiffusionPipeline.from_pretrained(self.m_modelID, torch_dtype=torch.float16, revision="fp16", use_auth_token=self.m_accessToken)
            self.m_pipeline = self.m_pipeline.to(self.m_device)

    def generateImage(self, prompt, width=512, height=512, numInferenceSteps=50, guidanceScale=7.5):
            with autocast("cuda"):
                image = self.m_pipeline(prompt, height=height, widht=width, num_inference_steps=numInferenceSteps, guidance_scale=guidanceScale)["sample"][0]
            return image

        