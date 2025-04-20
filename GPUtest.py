import torch
print(torch.cuda.is_available())  # ควรได้ True
print(torch.cuda.device_count())  # ดูจำนวน GPU
print(torch.cuda.get_device_name(0))  # ดูชื่อ GPU
