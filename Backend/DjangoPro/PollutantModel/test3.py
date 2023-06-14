import pandas as pd
import matplotlib.pyplot as plt

# 读取csv文件并处理数据
df = pd.read_csv('/Users/apple/Pypro/Backend/DjangoPro/PollutantModel/data/reqult_201901_new/1_grid.csv')
x = df['lng']
y = df['lat']

# 生成折线图
plt.plot(x, y)
plt.title('Line Chart')
plt.xlabel('lng')
plt.ylabel('lat')
plt.show()
