import numpy, io
from fastapi import FastAPI, UploadFile, File
from torchvision.models import ResNet50_Weights,resnet50
from torchvision.transforms import transforms
from PIL import Image
import json

app = FastAPI()


# Step 1: Initialize model with the best available weights
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()
transform = transforms.ToTensor()
# Step 2: Initialize the inference transforms
preprocess = weights.transforms()

# Load class names
with open('imagenet-simple-labels.json') as f:
    class_names = json.load(f)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Load and preprocess image
    image = Image.open(file.file)
    image_tensor = transform(image)

    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(image_tensor).unsqueeze(0)

    # Step 4: Use the model and print the predicted category
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    # Return prediction
    return {"predicted": category_name,
            "score": f"{100 * score:.1f}%"}
