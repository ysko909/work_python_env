import numpy as np
import matplotlib.pyplot as plt

# ファイル出力デモ用
x = np.linspace(0, 1, 100)
y = x * 2
plt.plot(x, y)
# plt.show()
plt.savefig('plot.png')
