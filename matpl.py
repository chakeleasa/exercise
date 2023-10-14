import matplotlib.pyplot as plt
import numpy as np
# x = [1, 2, 3, 4, 5]
# y = [5, 4, 3, 2, 1]
# plt.plot(x,y,color='red',linewidth=2)       折线图，加上linestyle='--'就是虚线
# plt.scatter(x, y, s=100, c='blue')        散点图
# -------条形图
# x = ['A', 'B', 'C', 'D', 'E']
# y = [5, 4, 3, 2, 1]
# plt.bar(x,y,width=0.3,color='gray')
# ----------饼图
# values = [5,3,2,8,1]
# colors = ['purple','red','blue','gray','black']
# lables = ['A','B','C','D','E']
# plt.pie(values,labels=lables,colors=colors)
# -----------------直方图
# data = np.linspace(1,1000,7)
# plt.hist(data,bins=10,color='red')
# -----------------imshow用于绘制图像
data = np.random.rand(10,10)
plt.imshow(data,cmap='gray')
plt.show()