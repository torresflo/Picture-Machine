import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

from enum import Enum

class PretrainedModelName(Enum):
    StableDiffusion_2_1 = "stabilityai/stable-diffusion-2-1"
    DreamLike_PhotoReal_2_0 = "dreamlike-art/dreamlike-photoreal-2.0"
    OpenJourney_2 = "prompthero/openjourney-v2"
    Epic_Diffusion = "johnslegers/epic-diffusion"
    Anything_4_0 = "andite/anything-v4.0"

class ImageGenerator:
    def __init__(self):
        self.m_device = "cuda"
        self.m_modelName = None

    def loadModel(self, modelName: PretrainedModelName):
        if(self.m_modelName is None or self.m_modelName != modelName):
            self.m_modelName = modelName
            print(f"Loading model {self.m_modelName.value} in your GPU, please wait...")

            self.m_pipeline = StableDiffusionPipeline.from_pretrained(self.m_modelName.value, torch_dtype=torch.float16)
            self.m_pipeline.scheduler = DPMSolverMultistepScheduler.from_config(self.m_pipeline.scheduler.config)
            self.m_pipeline = self.m_pipeline.to(self.m_device)
            self.m_pipeline.enable_attention_slicing()

            self.m_pipeline.safety_checker = None
            self.m_pipeline.requires_safety_checker = False

    def generateImage(self, modelName: PretrainedModelName, prompt, width=768, height=768, numInferenceSteps=50, guidanceScale=7.5, seed=0):
        self.loadModel(modelName)
        generator = torch.Generator(self.m_device).manual_seed(seed)
        image = self.m_pipeline(prompt, height=height, width=width, num_inference_steps=numInferenceSteps, guidance_scale=guidanceScale, generator=generator).images[0]
        return image

        