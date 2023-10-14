import numpy as np
# arr = np.array([[1,3,5],[1,5,8,],[1,4,6]])
# print(arr.shape,arr.ndim,arr.dtype,'\n',arr**2)  #每一维数组个数,几维数组，数组类型.每个数组元素的平方
# print(np.zeros((3,4)))  #二维数组里创建三个数组，每个数组4个元素。元素都以零填补   np.ones就是以一填补
# print(np.eye(3))# eye创建对角线全为1的二维数组.
# # 两种方法转换数据的类型   np.int32/float64(obj)直接转换   或者obj.astype(np.int32/float64)
# arr1 = np.array([[1,3,5,7,],[1,5,8,0]],dtype=np.float64)
# arr2 = np.array([1,4,6,8,90,],dtype=np.int32)
# arr3 = np.int32(arr1)
# print('-----------------------------------------------------------------------------------------------------')
# print(arr3)
# arr4 = arr2.astype(np.float64)
# print('\n',arr4)
# #-------------------------------------------------------------------------------------------------------------------------------
# arr = np.array([[1,4,6,7,]])     # 只有索引值为true会返回
# print(arr>4)
# print(arr==4)
# print(arr[arr==1])
# print(arr[arr==0])
# print(arr[True])
# ---------------------------------------------------------------------------------------------------------------------------------
# # 二维切片
# arr = np.arange(0,16).reshape(4,4)      # 取0到16，左闭右开，二维数组里四个数组，每个数组四个元素
# print(arr[:2,0:])      #加大F就是将数组以横向展开
# print(arr.flatten('F'))
# arr1 = np.array([1,])
# print(arr+arr)
# a = np.linspace(0,2,10)      0到2平均分成10隔
# a = np.random.rand(2,3)       随机生成二维数组共两个每个里面三个

# a = np.arange(0,16)
# a = a.reshape((4,4))     改变数组的形状

# a = np.array([1,2])       数组矩阵乘积,数组大小要相等
# b = np.array([3,4])
# a = np.dot(a,b)

# a = np.array([[1,5],[1,7]])    计算数组的和，数组大小要相等
# a = np.sum(a)

# a = np.array([[3,6],[6,9]])     计算数组的平均值，数组大小要想等
# a = np.mean(a)

# a = np.array([[1,6],[7,4]])       计算数组的平均差，数组大小要相等
# a = np.std(a)

# o = np.array([[1,6],[7,4]])
# a = np.max(o)                     数组中最大值
# b = np.min(o)                     数组中最小值

a = np.arange(64).reshape([4,4,4])
b = a.reshape(-1)
print(a)
c = a.ravel()
print('降维reshape方法',b)
print('降维ravel方法',c)
