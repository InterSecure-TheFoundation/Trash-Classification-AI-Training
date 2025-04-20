import os
import shutil
import random

#  กำหนด path หลัก
source_root = "setdata"
destination_root = "Datasets"

limit_data_mode = True
default_limit = 500
valid_samples = 100
reduction_amount = 100  # จำนวนที่จะหักออกจาก dataset ที่ไม่ใช่ whitelist
whitelist = ["Chip_bag" , "Paper"]  # รายชื่อ dataset ที่จะไม่ถูกหัก 100

# ค้นหา dataset ทั้งหมด
datasets = sorted([d for d in os.listdir(source_root) if os.path.isdir(os.path.join(source_root, d))])
class_map = {name: idx for idx, name in enumerate(datasets)}

# คำนวณ limit_data โดยอัตโนมัติ
if limit_data_mode:
    count_map = {}
    for name in datasets:
        train_labels_path = os.path.join(source_root, name, "train", "labels")
        if os.path.exists(train_labels_path):
            label_files = [f for f in os.listdir(train_labels_path) if f.endswith(".txt")]
            count_map[name] = len(label_files)

    limit_data = min(count_map.values()) if count_map else default_limit
    min_dataset = min(count_map, key=count_map.get)
    print(f"limit_data = {limit_data} (พบใน dataset: '{min_dataset}')")
else:
    limit_data = default_limit
    print(f"limit_data (manual) = {limit_data}")

# สร้างโฟลเดอร์ปลายทาง
for folder in ["train", "valid", "test"]:
    os.makedirs(os.path.join(destination_root, folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(destination_root, folder, "labels"), exist_ok=True)

# ประมวลผลแต่ละ dataset
for dataset_name in datasets:
    dataset_path = os.path.join(source_root, dataset_name)
    class_ob = str(class_map[dataset_name])

    print(f"กำลังประมวลผล `{dataset_name}` (class {class_ob})...")

    train_labels_path = os.path.join(dataset_path, "train", "labels")
    train_images_path = os.path.join(dataset_path, "train", "images")
    valid_labels_path = os.path.join(dataset_path, "valid", "labels")
    valid_images_path = os.path.join(dataset_path, "valid", "images")
    test_labels_path = os.path.join(dataset_path, "test", "labels")
    test_images_path = os.path.join(dataset_path, "test", "images")

    if not os.path.exists(train_labels_path):
        print(f"ไม่พบโฟลเดอร์: {train_labels_path}")
        continue

    train_label_files = [f for f in os.listdir(train_labels_path) if f.endswith(".txt")]

    # ลดจำนวนข้อมูลถ้าไม่ใช่ whitelist
    dataset_limit = limit_data if dataset_name in whitelist else max(limit_data - reduction_amount, 1)
    if len(train_label_files) > dataset_limit:
        train_label_files = random.sample(train_label_files, dataset_limit)

    # แบ่ง valid set หากไม่มี valid folder
    if not os.path.exists(valid_labels_path):
        valid_label_files = random.sample(train_label_files, min(valid_samples, len(train_label_files)))
        train_label_files = list(set(train_label_files) - set(valid_label_files))
    else:
        valid_label_files = [f for f in os.listdir(valid_labels_path) if f.endswith(".txt")]

    data_splits = {
        "train": (train_label_files, train_labels_path, train_images_path),
        "valid": (valid_label_files, 
                  valid_labels_path if os.path.exists(valid_labels_path) else train_labels_path,
                  valid_images_path if os.path.exists(valid_images_path) else train_images_path)
    }

    for folder, (label_files, labels_path, images_path) in data_splits.items():
        for idx, filename in enumerate(label_files, start=1):
            file_path = os.path.join(labels_path, filename)
            new_filename = f"{dataset_name}_{str(idx).zfill(5)}.txt"

            with open(file_path, "r") as file:
                lines = file.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    parts[0] = class_ob
                    new_lines.append(" ".join(parts))

            new_label_path = os.path.join(destination_root, folder, "labels", new_filename)
            with open(new_label_path, "w") as file:
                file.write("\n".join(new_lines) + "\n")

            img_filename = filename.replace(".txt", ".jpg")
            img_src = os.path.join(images_path, img_filename)
            new_img_filename = new_filename.replace(".txt", ".jpg")
            img_dest = os.path.join(destination_root, folder, "images", new_img_filename)

            if os.path.exists(img_src):
                shutil.copy(img_src, img_dest)

    # จัดการ test set
    if os.path.exists(test_labels_path) and os.path.exists(test_images_path):
        test_label_files = [f for f in os.listdir(test_labels_path) if f.endswith(".txt")]
        for filename in test_label_files:
            label_src = os.path.join(test_labels_path, filename)
            img_filename = filename.replace(".txt", ".jpg")
            img_src = os.path.join(test_images_path, img_filename)

            label_dest = os.path.join(destination_root, "test", "labels", f"{dataset_name}_{filename}")
            img_dest = os.path.join(destination_root, "test", "images", f"{dataset_name}_{img_filename}")

            shutil.copy(label_src, label_dest)
            if os.path.exists(img_src):
                shutil.copy(img_src, img_dest)

    print(f" เสร็จสิ้นการประมวลผล `{dataset_name}` !")

# สร้าง data.yaml
data_yaml_path = os.path.join(destination_root, "data.yaml")
with open(data_yaml_path, "w") as yaml_file:
    yaml_file.write(f"train: ../train/images\n")
    yaml_file.write(f"val: ../valid/images\n")
    yaml_file.write(f"test: ../test/images\n\n")
    yaml_file.write(f"nc: {len(datasets)}\n")
    yaml_file.write(f"names: {datasets}\n")

print(f"เสร็จสิ้นทั้งหมด! ข้อมูลถูกย้ายไปยัง `{destination_root}` เรียบร้อยแล้ว!")
print(f"สร้างไฟล์ `data.yaml` เรียบร้อย! (nc={len(datasets)}, names={datasets})")
