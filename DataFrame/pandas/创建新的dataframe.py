from pandas import DataFrame, Series
import numpy

class create_dataframe():
  # 先对数据做定义
  countries = ['Russian Fed.', 'Norway', 'Canada', 'United States']
  gold = [13, 11, 10, 9]
  silver = [11, 5, 10, 7]
  bronze = [9, 10, 5, 12]
  # 创建数据字典
  # '关键字' : panda序列(值), 自定义index
  # Series 用来定位序列值
  # 一个series是一个一维的数据类型
  olympics_medal_counts = {
    'country_name': Series(countries, index=['a', 'b', 'c', 'd']),
    'gold': Series(gold, index=['a', 'b', 'c', 'd']),
    'silver': Series(silver, index=['a', 'b', 'c', 'd']),
    'bronze': Series(bronze, index=['a', 'b', 'c', 'd']),
  }
  # 转换，创建数据帧
  # 一个dataframe是一个二维的表结构
  df = DataFrame(olympics_medal_counts)
  print(df)
  
  # 获取列
  # print(df['country_name'][2])

  # 调整显示的数据
  # print(df[['country_name', 'gold']])

  # 索引值
  # print(df.loc['a'])

  # 条件值
  # print(df[df['gold'] > 10])
  # print(df['silver'][df['gold'] >= 10])
  

  # 金牌的平均值
  # print(numpy.mean(df['gold']))
  
  # 铜牌数且至少拥有一枚金牌
  # df_b_g = df['bronze'][df['gold'] >= 1]
  # print(df_b_g)
  # print(numpy.mean(df_b_g))

  # 奖牌平均
  print(df[['gold','silver','bronze']].apply(numpy.mean))
