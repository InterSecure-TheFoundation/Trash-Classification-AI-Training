# ระบบการฝึกโมเดล AI สำหรับการจำแนกขยะ (Trash Classification AI Training)

โครงการนี้เป็นส่วนหนึ่งของระบบแอปพลิเคชัน **TrashScan** ซึ่งพัฒนาเพื่อช่วยผู้ใช้งานในการแยกประเภทขยะได้อย่างถูกต้องผ่านกล้องถ่ายภาพของโทรศัพท์มือถือ โดยใช้เทคโนโลยี **ปัญญาประดิษฐ์ (Artificial Intelligence: AI)** ในการวิเคราะห์ภาพถ่ายของขยะและจำแนกประเภทขยะแบบเรียลไทม์

## วัตถุประสงค์ของระบบ

ระบบฝึกสอนโมเดล AI ในโฟลเดอร์นี้มีจุดมุ่งหมายเพื่อ:
- สร้างโมเดลที่สามารถตรวจจับและจำแนกขยะได้หลากหลายประเภทในสภาพแวดล้อมจริง
- ใช้โมเดลร่วมกับแอปพลิเคชัน TrashScan เพื่อแสดงผลข้อมูลประเภทขยะแก่ผู้ใช้งาน
- สนับสนุนพฤติกรรมการแยกขยะในชีวิตประจำวัน และส่งเสริมการรีไซเคิลอย่างถูกวิธี

## รายการวัตถุที่โมเดลสามารถจำแนกได้ (Class Labels)

โมเดลที่พัฒนานี้สามารถจำแนกวัตถุขยะได้ทั้งหมด 8 ประเภท ได้แก่:

```
names: ['Chip_bag', 'Glass', 'Leaf', 'Paper', 'battery', 'can', 'plastic_bag', 'plastic_bottle']
```

- **Chip_bag**: ซองขนม เช่น ถุงมันฝรั่งทอด
- **Glass**: แก้วน้ำ ขวดแก้ว หรือเศษแก้ว
- **Leaf**: เศษใบไม้หรือขยะอินทรีย์
- **Paper**: กระดาษทั่วไป เช่น หนังสือพิมพ์ กล่องกระดาษ
- **Battery**: ถ่านไฟฉาย แบตเตอรี่ต่าง ๆ
- **Can**: กระป๋องอลูมิเนียม เช่น กระป๋องน้ำอัดลม
- **Plastic_bag**: ถุงพลาสติกทั่วไป
- **Plastic_bottle**: ขวดน้ำพลาสติก หรือบรรจุภัณฑ์พลาสติก

## การฝึกโมเดล (Training Process)

โมเดลที่ใช้ในระบบได้รับการฝึกจากข้อมูลภาพ (Dataset) ซึ่งนำเข้าจากแพลตฟอร์ม **Roboflow** โดยใช้ YOLOv8 สำหรับการตรวจจับวัตถุในภาพ (Object Detection)

การเตรียมข้อมูลและการฝึกฝนประกอบด้วยขั้นตอนหลัก:
- ดาวน์โหลดและรวมข้อมูลจากหลายชุดข้อมูลเพื่อความหลากหลายของวัตถุ
- ทำการปรับแต่ง Datasers 
- ฝึกโมเดลด้วย YOLOv8 พร้อมปรับค่าพารามิเตอร์สำหรับการตรวจจับวัตถุข

## แหล่งข้อมูล Dataset ที่ใช้ในการฝึกโมเดล

โมเดล Trash Classification ได้รับการฝึกโดยใช้ข้อมูลภาพจาก Roboflow Universe ดังรายการต่อไปนี้:

- https://universe.roboflow.com/public-ws/batteries  
- https://universe.roboflow.com/yolo-eurh8/plastic-nayza/dataset/1/images  
- https://universe.roboflow.com/trash-dataset-for-oriented-bounded-box/trash-detection-1fjjc/model/14  
- https://universe.roboflow.com/models/object-detection  
- https://universe.roboflow.com/battery-i4e70/batteries-4lmwn  
- https://universe.roboflow.com/vision-wajsm/spray-0tvqy/dataset/4  
- https://universe.roboflow.com/asdasd-boz3q/glass-xrghl/dataset/3  
- https://universe.roboflow.com/noverflow/dust-sdujb  
- https://universe.roboflow.com/jc2/leaf-count-w5m5l  
- https://universe.roboflow.com/project-zq0wz/metal-can/dataset/1/download/yolov8  
- https://universe.roboflow.com/naviyn/fyp-gimtb  
- https://universe.roboflow.com/school-gchcr/batteries-1aib9/dataset/1  

