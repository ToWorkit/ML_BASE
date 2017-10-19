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
  # print(df)
  
  # 一块金牌四分，银牌二分，铜牌一分
  # 取出奖牌
  medal_counts = df[['gold', 'silver', 'bronze']]
  print(medal_counts)
  # 对应分数求矩阵乘积
  points = numpy.dot(medal_counts, [4, 2, 1])
  # print(points)
  # 将国家和分数重新组成数据集
  olympics_points = {
    'country_name': Series(countries),
    'points': Series(points)
  }
  olp_df = DataFrame(olympics_points)
  print(olp_df)
  
