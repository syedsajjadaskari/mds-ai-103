import os
from pathlib import Path
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential


api_key = os.getenv("AZURE_VISION_API_KEY")
vision_endpoint = os.getenv("AZURE_VISION_ENDPOINT")
if not api_key or not vision_endpoint:
    raise ValueError("Please set AZURE_VISION_API_KEY and AZURE_VISION_ENDPOINT environment variables")
credential = AzureKeyCredential(api_key)
client = ImageAnalysisClient(vision_endpoint, credential)
print("Client created successfully!")
