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
| `colon_aca` | Colon Adenocarcinoma |
| `colon_n` | Colon Benign Tissue |
| `lung_aca` | Lung Adenocarcinoma |
| `lung_n` | Lung Benign Tissue |
| `lung_scc` | Lung Squamous Cell Carcinoma |

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

## 🚀 Running the API

### 1. Clone the repo

```bash
git clone https://github.com/AnishPanicker/cancer-classifier-api.git
cd cancer-classifier-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
cd API
uvicorn main:app --host localhost --port 8000 --reload
```

### 4. Open in browser

```
http://localhost:8000/docs
```

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
  "class": "Lung Benign Tissue",
  "confidence": 95.23
}
```

---

## 🛠️ Tech Stack

- **Model Training:** TensorFlow / Keras
- **API Framework:** FastAPI
- **Server:** Uvicorn
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
ilable under the [MIT License](LICENSE).
