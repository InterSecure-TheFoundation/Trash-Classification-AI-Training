import os
import shutil
import random

# **กำหนด path หลัก**
source_root = "setdata"
destination_root = "Datasets"

limit_data_mode = True  # ใช้ limit จากจำนวนข้อมูลที่น้อยที่สุด
default_limit = 300     # หากไม่ใช้ mode auto
valid_samples = 100

# ค้นหาชื่อ dataset ทั้งหมด
datasets = sorted([d for d in os.listdir(source_root) if os.path.isdir(os.path.join(source_root, d))])
class_map = {name: idx for idx, name in enumerate(datasets)}

# หา limit_data อัตโนมัติถ้าเปิด mode
if limit_data_mode:
    all_counts = []
    count_map = {}
    for name in datasets:
        train_labels_path = os.path.join(source_root, name, "train", "labels")
        if os.path.exists(train_labels_path):
            label_files = [f for f in os.listdir(train_labels_path) if f.endswith(".txt")]
            count = len(label_files)
            all_counts.append(count)
            count_map[name] = count
    limit_data = min(all_counts) if all_counts else default_limit
    # แจ้งชื่อ dataset ที่มีจำนวนน้อยที่สุด
    min_dataset = min(count_map, key=count_map.get)
    print(f" limit_data = {limit_data} (พบใน dataset: '{min_dataset}')")
else:
    limit_data = default_limit
    print(f"limit_data (manual) = {limit_data}")
