import os
from ultralytics import YOLO
import torch

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(BASE_DIR, "Datasets", "data.yaml")
 
    # ตรวจสอบว่าข้อมูลมีอยู่จริง
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"ไม่พบไฟล์ data.yaml : {data_path}")

    print(f"กำลังใช้ data.yaml จาก: {data_path}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = YOLO("yolov8n.pt").to(device)  
    model.train(
        data=data_path,
        epochs=300,
        imgsz=640,
        batch=64,           
        lr0=0.001,
        # freeze=10,
        project="Models",
        name="Final",
      
        device=0,       
       
        workers=2,         
        cache="disk",  
        iou=0.7
    )
  

    print("Training complete!")
