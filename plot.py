# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

import csv
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端，确保在没有窗口的情况下也能保存图片
import matplotlib.pyplot as plt
from pathlib import Path

# 1. 确保输出文件夹存在
Path("out").mkdir(exist_ok=True)
print("开始读取数据...")

dates = []
rainfalls = []

# 2. 读取数据
with open("data/daily_rainfall.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader) # 跳过第1行标题
    next(reader) # 跳过第2行标题
    next(reader) # 跳过第3行副标题
    
    for row in reader:
        if not row: continue
        try:
            year, month, day, value = row[0], row[1], row[2], row[3]
            rain_val = float(value)
            dates.append(datetime(int(year), int(month), int(day)))
            rainfalls.append(rain_val)
        except (ValueError, IndexError):
            continue # 跳过无法解析的行

print(f"数据读取完成，共 {len(dates)} 条有效记录。")

# 3. 只画最近3年的数据
dates = dates[-365*3:]
rainfalls = rainfalls[-365*3:]

# 4. 开始绘图
print("开始绘图...")
plt.figure(figsize=(12, 5))
plt.plot(dates, rainfalls, color='blue', linewidth=0.8)
plt.fill_between(dates, rainfalls, color='blue', alpha=0.15)
plt.title("Hong Kong Observatory Daily Total Rainfall (Last 3 Years)")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.grid(True, alpha=0.3)

# 5. 保存图片
plt.savefig("out/plot.png")
print("绘图成功！图片已保存到 out/plot.png")