import pandas as pd
import numpy as np
# file_path = r'./demo.xlsx'
# fi = pd.read_excel(file_path,sheet_name='Sheet1',usecols=['name','age','sex']) #sheet1表读三行,只要name,age俩字段
# test = pd.read_excel(file_path,header=None) #header=none就是不要他的字段做表头
# print(fi)  #输出这个文件
# print('')
# print(fi.head())  #输出它的头
# print('head()')
# print(fi.columns)  #输出所有字段名
# print('columns')
# print(fi.describe())  #输出描述
# print('describe()')
# print(fi.index)   #输出索引
# print('index')
# print(fi['name'].values)  #输出其name字段
# print('fi[name]')
# cs = './test.csv'
# test.to_csv(cs,index=False)
#--------------------------------------------------------------------------------------------------------------------------
# name = 'facasd'
# age = 35
# sex= 'fhaosc'
# dataframe = pd.DataFrame([[name,age,sex]],columns=['name','age','sex'])
# add = fi.append(dataframe,ignore_index=True)
# add.to_excel('./demo.xlsx',index=False,engine='openpyxl',sheet_name='Sheet1')
#--------------------------------------------------------------------------------------------------------------------------
# fi = pd.DataFrame([[1,4,6]],columns=['name','dasdas','dasda'])
# fi.to_excel('example.xlsx',sheet_name='Sheet1',index=False)
#--------------------------------------------------------------------------------------------------------------------------
# exam = pd.read_excel('example.xlsx')
# ap = pd.DataFrame({'first':['dasda']})
# ap.to_excel('example.xlsx',index=False)
# ------------------------------------------------------------------------------------------------------------------------
# path = 'example.xlsx'
# fi = pd.read_excel(path,sheet_name='Sheet1')
# a = pd.DataFrame([['ubantu']],columns=['first'])
# b = fi.append(a,ignore_index=True)
# b.to_excel('./example.xlsx',index=False)
# ---------------------------------------------------------------------------------
# df = pd.read_excel('./example.xlsx')
# df = df.fillna(0)    用零填充空值
# df = df.drop_duplicates()   去除重复值
# df = df.replace({'first':{'dasda':'A','ubantu':'B'}})     first列dasda换成A，ubantu换成B
# df['first'].replace({'dasda':'A','ubantu':'B'})    跟上边意思一样
# df.replace(['dasda',1.0],2)    全局替换'dasda',1.0换成2.    2也可以换成列表，与前边列表一对一换
df = pd.DataFrame({'A':[1,2,3],'B':[2,3,4],'name':['coco','Mary','coco'],'age':[13,19,24]},index=['A','B','C'])
print(df)
#---------------------------- aggs对数据进行按行或按列操作，取平均值取最大值或最小值，参数可以接受列表，字典，或函数
# print(df.agg(sum,1))      #  1是行，0是列
# print(df.agg(['sum','min']))
# print(df.agg({'A':['min','mean'],'B':['max','min']}))
# pivot_table数据透视表，与前面相差无几能显示详细数据。
pl = df.pivot_table(index=['name'])
plus = df.pivot_table(index=['name'],values=['A','B'],aggfunc=np.sum,columns=['age'],fill_value=0)
# plus是计算所有名字相同的人的A和B的总和,显示上字段age,用0进行填充
print(plus,'\n',pl)