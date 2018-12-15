'''
- calendar  跟日历相关
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都需要先导入，string是特例
'''

import calendar
# calendar 获取一年的日历字符串
# 参数 可以不加，有默认值
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数

cal = calendar.calendar(2018)
print(type(cal))  # 是一个str类型
# print(cal)

# isleap：判断某一年是否是闰年
print(calendar.isleap(2000))

# leapdays：获取指定年份之间的闰年的个数
print(calendar.leapdays(2001,2018))

# month()获取某个月的日历字符串形式
# 格式：calender.month(年，月)
# 返回值：月日历的字符串
m1 = calendar.month(2018,3)
print(m1)

# monthrange() 获取一个月 是从周几开始以及这个月的天数
# 格式：calender.monthrange(year,month)
# 返回值：元组（周几开始，天数）
# 注意：周默认，0-6，表示周一到周天
t = calendar.monthrange(2018,4) # 2018年4月是周天开始，一共有30天
print(type(t))
print(t)

# monnthcalendar() 返回一个月每天的矩阵列表
# 格式： calendar.monthcalendar(year,month)
# 返回值：二维列表
# 注意：矩阵中没有的天数用0表示
m2 = calendar.monthcalendar(2018,3)
print(type(m2))
print(m2)

# prcal ：print calender 直接打印日历
# calendar.prcal(year)
'''
 Help on method pryear in module calendar:

 pryear(theyear, w=0, l=0, c=6, m=3) method of calendar.TextCalendar instance
     Print a year's calendar.
'''

# prmonth :打印整个月的日历
'''
Help on method prmonth in module calendar:

prmonth(theyear, themonth, w=0, l=0) method of calendar.TextCalendar instance
    Print a month's calendar.
'''