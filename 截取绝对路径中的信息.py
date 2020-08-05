from pathlib import Path

file = r'E:\Windows Embellish\淘宝买的付费字体.zip'
stem = Path(file).stem
name = Path(file).name
suffix = Path(file).suffix

print(stem, name, suffix)
