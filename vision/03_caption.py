import os
from pathlib import Path
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures


credential = AzureKeyCredential(api_key)
client = ImageAnalysisClient(vision_endpoint, credential)
print("Client created successfully!")
image_url = "https://i.pinimg.com/736x/60/2b/b8/602bb85ade78cb57e2ef4bbd3d77fdb2.jpg"
results = client.analyze_from_url(image_url = image_url, 
visual_features=[VisualFeatures.CAPTION])
print("Caption found:")
print(f"  {results.caption.text} - Confidence: {results.caption.confidence:.2f}")