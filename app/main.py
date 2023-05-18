import json
from fastapi import FastAPI, UploadFile, File
from torchvision.models import ResNet50_Weights,resnet50
from torchvision.transforms import transforms
from PIL import Image

#initialize app
app = FastAPI()


#intialize resnet and connected variables
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()
transform = transforms.ToTensor()

preprocess = weights.transforms()

#create endpoint
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Load and preprocess image
    image = Image.open(file.file)
    image_tensor = transform(image)

    # Apply preprocess
    batch = preprocess(image_tensor).unsqueeze(0)

    # Use the model and return predicted category
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    # Return prediction
    return {"predicted": category_name,
            "score": f"{100 * score:.1f}%"}
