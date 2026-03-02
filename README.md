# 🫁 Cancer Classifier API

A deep learning project that detects lung and colon cancer from histopathological images using a CNN model served via FastAPI.

---

## 📁 Project Structure
```
cancer-classifier-api/
├── model/                   # Trained CNN model
├── training/                # Model training notebook (Google Colab)
├── API.ipynb                # FastAPI server notebook (Google Colab + ngrok)
├── Requirements.docx        # Project requirements
└── README.md
```

---

## 🗂️ Cancer Classes

| Class | Description |
|---|---|
| `Colon Adenocarcinoma` | Malignant colon tumor |
| `Colon Benign Tissue` | Healthy colon tissue |
| `Lung Adenocarcinoma` | Malignant lung tumor |
| `Lung Benign Tissue` | Healthy lung tissue |
| `Lung Squamous Cell Carcinoma` | Malignant lung squamous tumor |

---

## 🧠 Model Architecture

- Built using TensorFlow/Keras Sequential API
- 3 Convolutional layers with MaxPooling
- Dense layers with Softmax output
- Input size: `64x64x3`
- Output: 5 classes
- Validation Accuracy: **97%**

---

## 📊 Dataset

[Lung and Colon Cancer Histopathological Images](https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images) from Kaggle — 25,000+ histopathological images across 5 classes.

---

## 🚀 Running the API (Google Colab)

### 1. Open `API.ipynb` in Google Colab

### 2. Install dependencies
```python
!pip install fastapi uvicorn pyngrok nest-asyncio pillow numpy -q
```

### 3. Set your ngrok token
```python
ngrok.set_auth_token("YOUR_NGROK_TOKEN_HERE")  # Get from https://dashboard.ngrok.com
```

### 4. Run all cells — you will get a public URL like:
```
https://xxxx.ngrok-free.app
```

---

## ⚠️ Important

Never commit your ngrok token to GitHub. Always replace it with `YOUR_NGROK_TOKEN_HERE` before pushing.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/ping` | Check if server is alive |
| POST | `/predict` | Upload image and get prediction |
| GET | `/docs` | Swagger UI for testing |

### Example Response
```json
{
  "class": "Lung Adenocarcinoma",
  "confidence": 95.23
}
```

---

## 🛠️ Tech Stack

- **Model Training:** TensorFlow / Keras
- **API Framework:** FastAPI
- **Server:** Uvicorn
- **Tunneling:** ngrok
- **Image Processing:** Pillow, NumPy
- **Visualization:** Matplotlib
- **Environment:** Google Colab

---

## 📦 Requirements
```
fastapi
uvicorn
tensorflow
keras
pillow
numpy
matplotlib
pyngrok
nest-asyncio
```

---

## 👤 Author

**Anish Panicker**  
[GitHub](https://github.com/AnishPanicker)

---
