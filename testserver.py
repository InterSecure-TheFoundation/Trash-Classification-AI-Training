from flask import Flask, request, jsonify
from flask_cors import CORS  # import CORS
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
CORS(app)  # เปิด CORS ให้ทุก origin (เช่น fetch จากทุกเว็บได้)

# โหลดโมเดล YOLO
model = YOLO("runs/detect/train/weights/best.pt")
class_names = model.names

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    img = np.array(img)

    results = model(img)
    output = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            output.append({
                "class": class_names[class_id],
                "confidence": round(confidence, 4)
            })

    return jsonify(output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
