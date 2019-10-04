# -*- coding:UTF8 -*-

# https://www.cnblogs.com/derek1184405959/p/8078948.html
# https://gist.github.com/rswofxd/2787060

# 2.在正则表达式中， 如下的字符是具有特殊含义的
# . (所有字符)  ^  $  *(0-N次)  +(1-N次)  ? (0-1次) { } [  ]  \  |  ( )
#       1)."[" 和 "]"。它们常用来指定一个字符类别，所谓字符类别就是你想匹配的一个字符集
#       2).其它地方的"^"只会简单匹配 "^"字符本身。例[^5] 将匹配除 "5" 之外的任意字符。
#       3).反斜杠后面可以加不同的字符以表示不同特殊意义。它也可以用于取消所有的元字符
#
# 3.RE 函数用法:
#       findall(rule , target [,flag] ) 在目标字符串中查找符合规则的字符串。
#       match() 决定 RE 是否在字符串刚开始的位置匹配
#       search() 扫描字符串，找到这个 RE 匹配的位置
#       findall() 找到 RE 匹配的所有子串，并把它们作为一个列表返回
#       finditer() 找到 RE 匹配的所有子串，并把它们作为一个迭代器返回
#       group() 返回被 RE 匹配的字符串
#       start() 返回匹配开始的位置
#       end() 返回匹配结束的位置
#       span() 返回一个元组包含匹配 (开始,结束) 的位置
#       compile( rule [,flag] )将正则规则编译成一个Pattern对象，以供接下来使用第一个参数
#
#                                   是规则式，第二个参数是规则选项。(使用compile加速)

# 语法	意义	说明
# "."	任意字符
# "^"	字符串开始	'^hello'匹配'helloworld'而不匹配'aaaahellobbb'
# "$"	字符串结尾	与上同理
# "*" 	0 个或多个字符（贪婪匹配）	<*>匹配<title>chinaunix</title>
# "+"	1 个或多个字符（贪婪匹配）	与上同理
# "?"	0 个或多个字符（贪婪匹配）	与上同理
# *?,+?,??	以上三个取第一个匹配结果（非贪婪匹配）	<*>匹配<title>
# {m,n}	对于前一个字符重复m到n次，{m}亦可	a{6}匹配6个a、a{2,4}匹配2到4个a
# {m,n}?	对于前一个字符重复m到n次，并取尽可能少	‘aaaaaa’中a{2,4}只会匹配2个
# "\\"	特殊字符转义或者特殊序列
# []	表示一个字符集	[0-9]、[a-z]、[A-Z]、[^0]
# "|"	或	A|B,或运算
# (...)	匹配括号中任意表达式
# (?#...)	注释，可忽略
# (?=...)	Matches if ... matches next, but doesn't consume the string.	'(?=test)'  在hellotest中匹配hello
# (?!...)	Matches if ... doesn't match next.	'(?!=test)'  若hello后面不为test，匹配hello
# (?<=...) 	Matches if preceded by ... (must be fixed length).	'(?<=hello)test'  在hellotest中匹配test
# (?<!...)	Matches if not preceded by ... (must be fixed length).	'(?<!hello)test'  在hellotest中不匹配test

# 特殊序列符号	意义
# \w	匹配任意数字和字母:[a-zA-Z0-9]
# \W	匹配任意非数字和字母:[^a-zA-Z0-9]

# \s	匹配任意空白字符:[\t\n\r\f\v]
# \S	匹配任意非空白字符:[^\t\n\r\f\v]

# \n	匹配一个换行符
# \t	匹配一个制表符

# \d	相当于[0-9]
# \D	相当于[^0-9]

# \A	只在字符串开始进行匹配
# \Z	只在字符串结尾进行匹配

# \b	匹配位于开始或结尾的空字符串
# \B	匹配不位于开始或结尾的空字符串

# 正则匹配
import re

# 日志出力
import logging

# print(re.__doc__)
print(100 * "#")

# \w与\W 字母数字下划线
print(re.findall(r'\w', 'hello derek \n 123'))
print(re.findall(r'\W', 'hello derek \n 123'))

print(100 * "#")
# \s与\S  匹配任意空白字符
print(re.findall(r'\s', 'hello  egon  123'))  # [' ', ' ', ' ', ' ']
print(re.findall(r'\S', 'hello  egon  123')
      )  # ['h', 'e', 'l', 'l', 'o', 'e', 'g', 'o', 'n', '1', '2', '3']

# \n \t都是空,都可以被\s匹配
print(re.findall(r'\s',
                 'hello \n egon \t 123'))  # [' ', '\n', ' ', ' ', '\t', ' ']

print(100 * "#")
# \n与\t
print(re.findall(r'\n', 'hello egon \n123'))  # ['\n']
print(re.findall(r'\t', 'hello egon\t123'))  # ['\t']

print(100 * "#")
# \d与\D
print(re.findall(r'\d', 'hello egon 123'))  # ['1', '2', '3']
print(re.findall(r'\D', 'hello egon 123 \n \t')
      )  # ['h', 'e', 'l', 'l', 'o', ' ', 'e', 'g', 'o', 'n', ' ']

print(100 * "#")
# \A与\Z   \A  匹配字符串开始  \Z 匹配字符串结束
print(re.findall(r'\Ahe', 'hello egon 123'))  # ['he'],\A==>^
print(re.findall(r'123\Z', 'hello egon 123'))  # ['he'],\Z==>$

print(100 * "#")
# ^与$
print(re.findall('^h', 'hello egon 123'))  # ['h']
print(re.findall('3$', 'hello egon 123'))  # ['3']

print(100 * "#")
# 重复匹配：| . | * | ? | .* | .*? | + | {n,m} |
# .  匹配任意字符，除了换行符，除非re.DOTALL标记
print(re.findall('a.b', 'a1b'))  # ['a1b']

# a和b中间匹配任意一个字符
print(re.findall('a.b', 'a1b a*b a b aaab'))  # ['a1b', 'a*b', 'a b', 'aab']
print(re.findall('a.b', 'a\nb'))
print(re.findall('a.b', 'a\nb', re.S))
print(re.findall('a.b', 'a\nb', re.DOTALL))

# *匹配*号前的字符0次或多次
print(re.findall('ab*', 'bbbbbbb'))  # []
print(re.findall('ab*', 'a'))  # ['a']
print(re.findall('ab*', 'abbbb'))  # ['abbbb']
print(re.findall('ab*', 'abababbabbbb'))  # ['ab', 'ab', 'abb', 'abbbb']

# ?   匹配前一个字符1次或0次
print(re.findall('ab?', 'a'))  # ['a']
print(re.findall('ab?', 'abbb'))  # ['ab']

# 匹配所有包含小数在内的数字
print(re.findall(
    r'\d+\.?\d*',
    "asdfasdf123as1.13dfa12adsf1asdf3"))  # ['123', '1.13', '12', '1', '3']

# .*默认为贪婪匹配
print(re.findall('a.*b', 'a1b22222222b'))  # ['a1b22222222b']

# .*?为非贪婪匹配：推荐使用
print(re.findall('a.*?b', 'a1b22222222b'))  # ['a1b']

# +   匹配前一个字符1次或多次
print(re.findall('ab+', 'abbaabb'))  # ['abb', 'abb']
print(re.findall('ab+', 'abbb'))  # ['abbb']

print(100 * "#")
# {n,m}  匹配前一个字符n到m次
print(re.findall('ab{2}', 'abbb'))  # ['abb']
print(re.findall('ab{2,4}', 'abbb'))  # ['abb']
print(re.findall('ab{1,}', 'abbb'))  # 'ab{1,}' ===> 'ab+'
print(re.findall('ab{0,}', 'abbb'))  # 'ab{0,}' ===> 'ab*'

print(100 * "#")
# []
print(re.findall('a[1*-]b',
                 'a1b a*b a-b'))  # []内的都为普通字符了，且如果-没有被转意的话，应该放到[]的开头或结尾

print(re.findall('a[^1*-]b', 'a1b a*b a-b a=b'))  # []内的^代表的意思是取反，所以结果为['a=b']

print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))  # []内的0-9的意思是数字，所以结果为['a1b']

print(re.findall('a[a-z]b',
                 'a1b a*b a-b a=b aeb'))  # []内的a-z意思是字母，所以结果为['azb']

print(re.findall(
    'a[a-zA-Z]b',
    'a1b a*b a-b a=b aeb aEb'))  # []内的a-z意思是大小字母，所以结果为['aeb', 'aEb']

# \# print(re.findall('a\\c','a\c')) #对于正则来说a\\c确实可以匹配到a\c,
# 但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
print(re.findall(
    r'a\\c', r'a\c'))  # r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
print(re.findall('a\\\\c', r'a\c'))  # 同上面的意思一样，和上面的结果一样都是['a\\c']

print(100 * "#")
# (): 匹配括号里面的内容
print(re.findall('ab+', 'ababab123'))  # ['ab', 'ab', 'ab']
print(re.findall('(ab)+123', 'ababab123'))  # ['ab']，匹配到末尾的ab123中的ab
print(re.findall('(?:ab)+123',
                 'ababab123'))  # findall的结果不是匹配的全部内容，而是组内的内容,?:可以让结果为匹配的全部内容

# |
print(
    re.findall(
        'compan(?:y|ies)',
        'Too many companies have gone bankrupt, and the next one is my company'
    ))

# ===========================re模块提供的方法介绍===========================
print(100 * "#")
# 1
print(re.findall('e', 'alex make love'))  # ['e', 'e', 'e'],返回所有满足匹配条件的结果,放在列表里

# 2
print(re.search('e', 'alex make love').group(
))  # e,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

# 3
print(re.match(
    'e', 'alex make love'))  # None,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match

# 4
print(re.split('[ab]',
               'abcd'))  # ['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割

# 5
print('===>', re.sub('a', 'A',
                     'alex make love'))  # ===> Alex mAke love，不指定n，默认替换所有

print('===>', re.sub('a', 'A', 'alex make love', 1))  # ===> Alex make love
print('===>', re.sub('a', 'A', 'alex make love', 2))  # ===> Alex mAke love
print('===>', re.sub('e', 'E', 'alex make love', 3))  # ===> Alex mAke love

print('===>',
      re.subn('e', 'E',
              'alex make love'))  # ===> ('Alex mAke love', 2),结果带有总共替换的个数

print(100 * "#")
# 6
obj = re.compile(r'\d{2}')

print(obj.search('abc123eeee').group())  # 12
print(obj.findall('abc123eeee12a12b121c'))  # ['12'],重用了obj

logging.warning('wrong password more than 3 times')
logging.critical('server is down')
logging.error('error message')
