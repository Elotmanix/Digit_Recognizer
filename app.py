from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # Added import for serving HTML
import numpy as np
import io
from PIL import Image, ImageOps
import joblib

model = joblib.load('mnist_model.pkl')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the index.html file
@app.get("/")
def serve_html():
    return FileResponse("static/index.html")

@app.post("/predict-image/")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    pil_image = Image.open(io.BytesIO(contents)).convert('L')
    pil_image = ImageOps.invert(pil_image)
    pil_image = pil_image.resize((28, 28), Image.LANCZOS)  # Updated resize method
    img_array = np.array(pil_image).reshape(1, -1)
    prediction = model.predict(img_array)
    return {"prediction": int(prediction[0])}
