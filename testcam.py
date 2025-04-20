import cv2
from ultralytics import YOLO

# โหลดโมเดลที่ฝึกไว้
model = YOLO("runs/detect/train/weights/best.pt")

# --- 1️⃣ ตรวจจับภาพเดี่ยว ---
def detect_image(image_path):
    results = model(image_path)
    for result in results:
        img = result.plot()  # ใช้ .plot() เพื่อวาด Bounding Box
        cv2.imshow("YOLO Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# --- 2️⃣ ตรวจจับจากกล้อง Webcam ---
def detect_webcam():
    cap = cv2.VideoCapture(0)  # เปิดกล้อง (0 = กล้องเริ่มต้น)
    
    if not cap.isOpened():
        print("❌ ไม่สามารถเปิดกล้องได้!")
        return

    while True:
        ret, frame = cap.read()  # อ่านภาพจากกล้อง
        if not ret:
            print("❌ ไม่สามารถอ่านภาพจากกล้องได้!")
            break

        # ใช้ YOLO ตรวจจับ
        results = model(frame)

        # วาด Bounding Box ลงบนภาพ
        for result in results:
            frame = result.plot()

        # แสดงผล
        cv2.imshow("YOLO Webcam Detection", frame)

        # กด 'q' เพื่อออกจาก loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# --- เรียกใช้งาน ---
mode = "webcam"

if mode == "image":
    image_path = input("📸 ป้อนชื่อไฟล์ภาพ: ").strip()
    detect_image(image_path)
elif mode == "webcam":
    print("🎥 เปิดกล้อง... กด 'q' เพื่อออก")
    detect_webcam()
else:
    print("⚠️ โปรดเลือก 'image' หรือ 'webcam'")
