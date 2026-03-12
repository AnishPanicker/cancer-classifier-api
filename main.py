from fastapi import FastAPI, File, UploadFile
import numpy as np
from io import BytesIO
from PIL import Image
import keras

MODEL = keras.models.load_model("model/model.keras")

CLASS_NAMES = [
    "Colon Adenocarcinoma",
    "Colon Benign Tissue",
    "Lung Adenocarcinoma",
    "Lung Benign Tissue",
    "Lung Squamous Cell Carcinoma"
]

IMG_SIZE = 64
app = FastAPI()

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))
    return np.array(image)

@app.get("/ping")
async def ping():
    return "Server is alive"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, axis=0)
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    return {
        "class": predicted_class,
        "confidence": round(confidence * 100, 2)
    }
