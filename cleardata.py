import os

# Path หลักของ dataset
base_path = "Datasets"
subfolders = ["train", "valid", "test"]

# คำที่เราต้องการให้ "คงไว้" ในชื่อไฟล์
keep_keywords = ["Chip_bag", "Paper"]

for split in subfolders:
    image_dir = os.path.join(base_path, split, "images")
    label_dir = os.path.join(base_path, split, "labels")

    if not os.path.exists(label_dir) or not os.path.exists(image_dir):
        print(f"[!] ไม่พบโฟลเดอร์: {split}")
        continue

    # ลบ label ที่ไม่เกี่ยวข้อง
    for label_file in os.listdir(label_dir):
        if not any(keyword in label_file for keyword in keep_keywords):
            label_path = os.path.join(label_dir, label_file)
            os.remove(label_path)
            print(f" ลบ label: {label_path}")

    # ลบ image ที่ไม่เกี่ยวข้อง (.jpg หรือ .png)
    for image_file in os.listdir(image_dir):
        if not any(keyword in image_file for keyword in keep_keywords):
            image_path = os.path.join(image_dir, image_file)
            os.remove(image_path)
            print(f" ลบ image: {image_path}")
