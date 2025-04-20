from ultralytics import YOLO

def main():
    # โหลดโมเดลจากที่เทรนไว้แล้ว
    model_path = "runs/detect/train_copy/weights/best.pt"
    model = YOLO(model_path)

    # เทรนต่อ โดยใช้ dataset.yaml ที่มีคลาสครบทั้งหมด
    model.train(
        data="Datasets/data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,           
        lr0=0.001,
        freeze=10,
        project="Models",
        name="focus_paper_chipbag",
        patience=5,
        device=0,            
        mosaic=0.0,          
        copy_paste=0.0,    
        mixup=0.0,          
        workers=0           
    )

if __name__ == "__main__":
    main()
