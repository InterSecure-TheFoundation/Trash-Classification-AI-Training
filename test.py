import cv2
from ultralytics import YOLO

# โหลดโมเดล
model = YOLO("Models/Final2/weights/best.pt") 
# model = YOLO("runs/detect/train/weights/best.pt") 
# model = YOLO("Models/Met_Train/weights/best.pt") 
# โหลดและปรับขนาดภาพให้เป็น 640x640
image_path = "image8.png"
img = cv2.imread(image_path)


# ทำนายด้วย YOLO
results = model(img)

# แสดงภาพพร้อมผลลัพธ์
for result in results:
    img_out = result.plot()  # สร้างภาพพร้อม bounding box
    img_resized = cv2.resize(img_out, (640, 640))
    cv2.imshow("YOLO Detection", img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
