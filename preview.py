import csv

# 使用 utf-8-sig 编码打开文件，这是香港天文台 CSV 的标准编码
with open("data/daily_rainfall.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    
    # 跳过前两行多余的中英文标题
    next(reader) 
    next(reader) 
    
    # 第三行是真正的表头
    headers = next(reader)
    print("真正的表头:", headers)
    
    # 第四行才是第一行数据
    first_row = next(reader)
    print("第一行数据:", first_row)