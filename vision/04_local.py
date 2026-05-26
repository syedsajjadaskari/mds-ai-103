import os
from pathlib import Path
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures


credential = AzureKeyCredential(api_key)
client = ImageAnalysisClient(vision_endpoint, credential)

image_path = "images.jpeg"

with open(image_path, "rb") as image_file:
    image_data = image_file.read()
results = client.analyze(
    image_data = image_data,
    visual_features=[VisualFeatures.TAGS]
)
print("Tags found:")
for tag in results.tags.list:
    print(f"  {tag.name} - {tag.confidence:.2f}")