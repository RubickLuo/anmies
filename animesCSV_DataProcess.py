# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:51:30 2019

@author: LqH-_
"""

import pandas as pd


df = pd.read_csv('C:/Users/LqH-_/Desktop/animes/animes.csv', encoding='utf-8')

# 数据清洗
df['num_of_scoring_peopel'] = df['num_of_scoring_peopel'].str.replace('人评','').astype('int')


# allList = df['num_of_play'].tolist() + df['num_of_subscribe'].tolist() + df['num_of_danmu'].tolist()
# num_of_playList = df['num_of_play'].tolist()
# num_of_subscribeList = df['num_of_subscribe'].tolist()
# num_of_danmuList = df['num_of_danmu'].tolist()

# 数据清洗：单位统一（次）
allList = []
allList.append(df['num_of_play'].tolist())
allList.append(df['num_of_subscribe'].tolist())
allList.append(df['num_of_danmu'].tolist())

for listIndex in allList:
    for i,val in enumerate(listIndex):
        if val[-1:] == '万':
            val = float(val[:-1]) * 10000
        elif val[-1:] == '亿':
            val = float(val[:-1]) * 100000000
        elif val == '-':
            val = 0.0
        else:
            val = float(val)
        listIndex[i] = val
    if allList.index(listIndex) == 0:
        df['num_of_play'] = listIndex
    elif allList.index(listIndex) == 1:
        df['num_of_subscribe'] = listIndex
    elif allList.index(listIndex) == 2:
        df['num_of_danmu'] = listIndex


# print(num_of_playList)

# 导出已清洗数据
# df.to_excel('C:/Users/LqH-_/Desktop/animes已清洗数据20191209.xlsx')
# 电影相关评价指标 0-1标准化
df['评分指标'] = (df['score'] - df['score'].min()) / (df['score'].max() - df['score'].min())
df['人气指标'] = (df['num_of_scoring_peopel'] - df['num_of_scoring_peopel'].min()) / (df['num_of_scoring_peopel'].max() - df['num_of_scoring_peopel'].min())


'''
# 出图

import matplotlib.style as psl
psl.use('ggplot')

# 查看num_of_play TOP10
dptop10 = df.sort_values(by = 'num_of_play', ascending=False).iloc[:10]
dptop10['num_of_play'].plot(kind='bar',figsize = (10,5),rot=45,grid=True,color='y')

# num_of_subscribe TOP10
gltop10 = df.sort_values(by = 'num_of_subscribe', ascending=False).iloc[:10]
gltop10['num_of_subscribe'].plot(kind='bar',figsize = (10,5),rot=45,grid=True,color='g')

# 指标之间的关系图
import seaborn as sns
sns.pairplot(df)

re = df.corr()
    # 查看相关性
'''
import pyecharts as pe
# import pandas as pd
import matplotlib as plt

#显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] 

# df['name'] = df['name'].str.split(' ').str[0]

# 查看num_of_play TOP10
pltop10 = df.sort_values(by = 'num_of_play', ascending=False).iloc[:10]
pltop10.to_excel('C:/Users/LqH-_/Desktop/animes/num_of_play.xlsx')
x = pltop10['name'].tolist()
y1 = pltop10['num_of_play'].tolist()
y2 = pltop10['num_of_subscribe'].tolist()
y3 = pltop10['num_of_danmu'].tolist()

# 绘制交互柱状图
bar = pe.Bar('num_of_play-TOP10',height=450,width=1000)
bar.add('播放量',x,y1,is_stack=True)
bar.add('订阅量',x,y2,is_more_utils=True,is_datazoom_show=True,is_stack=True)
bar.add('弹幕数量',x,y3,is_more_utils=True,is_datazoom_show=True,is_stack=True)
bar.render('C:/Users/LqH-_/Desktop/num_of_play-TOP10.html')














