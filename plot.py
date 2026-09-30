# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "pillow"]
# ///

import csv
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path

Path("out").mkdir(exist_ok=True)
print("1. 正在读取数据...")

dates = []
rainfalls = []

with open("data/daily_rainfall.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader); next(reader); next(reader)
    for row in reader:
        if not row: continue
        try:
            year, month, day, value = row[0], row[1], row[2], row[3]
            rain_val = float(value)
            dates.append(datetime(int(year), int(month), int(day)))
            rainfalls.append(rain_val)
        except (ValueError, IndexError):
            continue

print(f"2. 读取完成，共 {len(dates)} 条记录。")

# --- 关键修改：设定数据长度和窗口大小 ---
TOTAL_DAYS = 365   # 只展示最近 1 年的数据
WINDOW = 30        # 窗口大小为 30 天

# 截取最近一年的数据
if len(dates) > TOTAL_DAYS:
    dates = dates[-TOTAL_DAYS:]
    rainfalls = rainfalls[-TOTAL_DAYS:]

# --- 绘图设置 ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 4), dpi=100)
plt.tight_layout()

line, = ax.plot([], [], color='#00E5FF', linewidth=2)

# 固定 Y 轴，防止动画时上下剧烈跳动
max_rain = max(rainfalls) if rainfalls else 100
ax.set_ylim(0, max_rain * 1.2)
ax.set_title("Hong Kong Observatory Daily Rainfall (1-Year Overview)", fontsize=12, color='white')
ax.set_xlabel("Date", fontsize=10, color='#B0BEC5')
ax.set_ylabel("Rainfall (mm)", fontsize=10, color='#B0BEC5')
ax.grid(True, linestyle='--', alpha=0.3, color='#546E7A')

# --- 动画更新函数 ---
def update(frame):
    # 当前窗口的起点和终点
    end_idx = frame + WINDOW
    if end_idx > len(dates):
        end_idx = len(dates)
        
    # 滑动窗口：显示从 frame 到 frame+WINDOW 的数据
    line.set_data(dates[frame:end_idx], rainfalls[frame:end_idx])
    
    # 动态调整 X 轴范围，让它看起来像在滚动
    ax.set_xlim(dates[frame], dates[end_idx-1])
    return line,

# --- 生成动画 ---
frames_count = len(dates) - WINDOW
if frames_count < 1:
    print("数据量不足，无法生成滑动窗口动画。")
else:
    print(f"3. 正在生成动画（共 {frames_count} 帧，约需 10-20 秒）...")
    ani = animation.FuncAnimation(fig, update, frames=frames_count, interval=100, blit=False)
    ani.save("out/rainfall.gif", writer='pillow', fps=10)
    print("4. 成功！动图已保存到 out/rainfall.gif")