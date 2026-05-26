import os
from pathlib import Path
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures


api_key = os.getenv("AZURE_VISION_API_KEY")
vision_endpoint = os.getenv("AZURE_VISION_ENDPOINT")
if not api_key or not vision_endpoint:
    raise ValueError("Please set AZURE_VISION_API_KEY and AZURE_VISION_ENDPOINT environment variables")
credential = AzureKeyCredential(api_key)
client = ImageAnalysisClient(vision_endpoint, credential)
print("Client created successfully!")

image_url = "https://cdn.britannica.com/63/211663-050-A674D74C/Jonny-Bairstow-batting-semifinal-match-England-Australia-2019.jpg"

result = client.analyze_from_url(
    image_url=image_url,
    visual_features=[VisualFeatures.TAGS]
)

print("Tags found:")
for tag in result.tags.list:
    print(f"  {tag.name} - {tag.confidence:.2f}")