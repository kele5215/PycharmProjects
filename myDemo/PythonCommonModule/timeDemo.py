"""
python常用模块

time模块

常用表示时间方式： 时间戳，格式化的时间字符串，元组（struct_time）

UTC（Coordinated Universal Time，世界协调时）亦即格林威治天文时间，世界标准时间。在中国为UTC+8。DST（Daylight Saving Time）即夏令时。

时间戳（timestamp）的方式：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。

元组（struct_time）方式：struct_time元组共有9个元素，返回struct_time的函数主要有gmtime()，localtime()，strptime()。
"""

import time

# 时间戳转换成struct_time
print(time.time())
print(time.gmtime())
print(time.localtime())
print(100 * '#')

# struct_time转换成时间戳
print(time.mktime(time.localtime()))
print(100 * '#')

# struct_time转换成format_time
"""
%a    本地（locale）简化星期名称
%A    本地完整星期名称
%b    本地简化月份名称
%B    本地完整月份名称
%c    本地相应的日期和时间表示
%d    一个月中的第几天（01 - 31）
%H    一天中的第几个小时（24小时制，00 - 23）
%I    第几个小时（12小时制，01 - 12）
%j    一年中的第几天（001 - 366）
%m    月份（01 - 12）
%M    分钟数（00 - 59）
%p    本地am或者pm的相应符    一
%S    秒（01 - 61）    二
%U    一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
%w    一个星期中的第几天（0 - 6，0是星期天）    三
%W    和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x    本地相应日期
%X    本地相应时间
%y    去掉世纪的年份（00 - 99）
%Y    完整的年份
%Z    时区的名字（如果不存在为空字符）
%%    ‘%’字符
"""
x = time.localtime()
print(time.strftime("%Y%m%d %H:%M:%S", x))
time_struct = time.strptime("30 Nov 00", "%d %b %y")
print(time_struct)
print(x.tm_year)
print(x.tm_mon)
print(x.tm_mday)
print(100 * '#')
