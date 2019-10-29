# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 9:54
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : retest.py
# @Software: PyCharm


import re

#re.compile('rule').search(content).group()
#re.compile('rule').findall(content)
#re.match('www', 'www.runoob.com')  返回位置
#re.match(r"(.*) are (.*?) .*", line, re.M | re.I)   通过group返回内容
#re.search(r'(.*) are (.*?) .*', line2, re.M | re.I)


# '.'     匹配所有字符串，除\n以外
# '-'     表示范围[0-9]
# '*'     匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
# '+'     匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+
# '^'     匹配字符串开头
# '$'     匹配字符串结尾 re
# '\'     转义字符， 使后一个字符改变原来的意思，如果字符串中有字符*需要匹配，可以\*或者字符集[*] re.findall(r'3\*','3*ds')结['3*']
# '*'     匹配前面的字符0次或多次 re.findall("ab*","cabc3abcbbac")结果：['ab', 'ab', 'a']
# '?'     匹配前一个字符串0次或1次 re.findall('ab?','abcabcabcadf')结果['ab', 'ab', 'ab', 'a']
# '{m}'   匹配前一个字符m次 re.findall('cb{1}','bchbchcbfbcbb')结果['cb', 'cb']
# '{n,m}' 匹配前一个字符n到m次 re.findall('cb{2,3}','bchbchcbfbcbb')结果['cbb']
# '\d'    匹配数字，等于[0-9] re.findall('\d','电话:10086')结果['1', '0', '0', '8', '6']
# '\D'    匹配非数字，等于[^0-9] re.findall('\D','电话:10086')结果['电', '话', ':']
# '\w'    匹配字母和数字，等于[A-Za-z0-9] re.findall('\w','alex123,./;;;')结果['a', 'l', 'e', 'x', '1', '2', '3']
# '\W'    匹配非英文字母和数字,等于[^A-Za-z0-9] re.findall('\W','alex123,./;;;')结果[',', '.', '/', ';', ';', ';']
# '\s'    匹配空白字符 re.findall('\s','3*ds \t\n')结果[' ', '\t', '\n']
# '\S'    匹配非空白字符 re.findall('\s','3*ds \t\n')结果['3', '*', 'd', 's']
# '\A'    匹配字符串开头
# '\Z'    匹配字符串结尾
# '\b'    匹配单词的词首和词尾，单词被定义为一个字母数字序列，因此词尾是用空白符或非字母数字符来表示的
# '\B'    与\b相反，只在当前位置不在单词边界时匹配
# []      是定义匹配的字符范围。比如 [a-zA-Z0-9] 表示相应位置的字符要匹配英文字符和数字。[\s*]表示空格或者*号
# '(?P<name>...)'  分组，除了原有编号外在指定一个额外的别名
print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{8})","371481199306143242").groupdict('city'))
# 结果{'province': '3714', 'city': '81', 'birthday': '19930614'}


#https://www.cnblogs.com/hello-wei/p/10181055.html
#search和group
example = "<div>test1</div><div>test2</div>"

greedPattern = re.compile("<div>.*</div>")
notGreedPattern = re.compile("<div>.*?</div>")

greedResult = greedPattern.search(example)
notGreedResult = notGreedPattern.search(example)

print("贪婪模式greedResult = %s" % greedResult.group())#<div>test1</div><div>test2</div>
print("非贪婪模式notGreedResult = %s" % notGreedResult.group())#<div>test1</div>

#反斜杠
print("*"*20,"反斜杠","*"*20)
example2="\\a\\b"
Pattern2_1 = re.compile("\\\\a")
Pattern2_2 = re.compile(r"\\b")
Result2_1 = Pattern2_1.search(example2)
Result2_2 = Pattern2_2.search(example2)
print("Result2_1 = %s" % Result2_1.group())
print("Result2_2 = %s" % Result2_2.group())

#flags 标志位参数
print("*"*20,"flags 标志位参数","*"*20)
content = 'Citizen wang , always fall in love with neighbour，WANG'
rr = re.compile(r'wan\w', re.I) # 不区分大小写
print(type(rr))
a = rr.findall(content)
print(type(a))
print(a)  #['wang', 'WANG']
# re.I(re.IGNORECASE)     使匹配对大小写不敏感
# re.L(re.LOCAL)               做本地化识别（locale-aware）匹配
# re.M(re.MULTILINE)         多行匹配，影响 ^ 和 $
# re.S(re.DOTALL)             使 . 匹配包括换行在内的所有字符
# re.U(re.UNICODE)           根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X(re.VERBOSE)          该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解


#re.match 尝试从一个字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，则返回None。
print("*"*20,"re.match   样例1","*"*20)
print(re.match('www', 'www.runoob.com').span())#(0, 3)  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))#None         # 不在起始位置匹配

print("*"*20,"re.match  样例2","*"*20)
line = "Cats are Smarter than dogs"
# re.M：多行匹配
# re.I:忽略大小写进行匹配
# match()以元组形式返回匹配成功的对象
match_obj = re.match(r"(.*) are (.*?) .*", line, re.M | re.I)
if match_obj:
    print("match_obj.group(): ", match_obj.group())#Cats are Smarter than dogs
    print("match_obj.group(1): ", match_obj.group(1))#Cats
    print("match_obj.group(2): ", match_obj.group(2))#Smarter
    print("match_obj.group(1,2): ", match_obj.group(1,2))#('Cats', 'Smarter')
    print("match_obj.groups(): ", match_obj.groups())#('Cats', 'Smarter')
else:
    print("None match!")

#re.search 扫描整个字符串并返回第一个成功的匹配。
print("*"*20,"re.search","*"*20)
line2 = "Cats are smarter than dogs";

searchObj = re.search(r'(.*) are (.*?) .*', line2, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())#Cats are smarter than dogs
    print("searchObj.group(1) : ", searchObj.group(1))#Cats
    print("searchObj.group(2) : ", searchObj.group(2))#smarter
    print("searchObj.groups() : ", searchObj.groups())#('Cats', 'smarter')
else:
    print("Nothing found!!")

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
print("*"*20,"re.search和re.match的区别","*"*20)
line3 = "Cats are smarter than dogs";

matchObj2 = re.match(r'dogs', line3, re.M | re.I)
if matchObj2:
    print("match --> matchObj.group() : ", matchObj2.group())
else:
    print("No match!!")  #No match!!

searchObj2 = re.search(r'dogs', line3, re.M | re.I)
if searchObj2:
    print("search --> searchObj2.group() : ", searchObj2.group()) #dogs
else:
    print("No match!!")

print(re.search(r'\+','7+').group())

#re.sub()  Python 的 re 模块提供了re.sub用于替换字符串中的匹配项
# 参数：
# pattern       正则中的模式字符串。
# repl            替换的字符串，也可为一个函数。
# string         要被查找替换的原始字符串。
# count         模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
print("*"*20,"re.sub()","*"*20)
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num) #电话号码 :  2004-959-559

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)#电话号码 :  2004959559

print("*"*20,"re.sub()中repl是函数","*"*20)
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))#A46G8HFD1134


#findall()  在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。注意： match 和 search 是匹配一次 findall 匹配所有。
print("*"*20,"findall()","*"*20)
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)

#re.finditer() 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
print("*"*20,"re.finditer()","*"*20)
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )

#re.split() split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：re.split(pattern, string[, maxsplit=0, flags=0])
print("*"*20,"re.split()","*"*20)
print(re.split('\W+','runoob,runoob,runoob.'))#['runoob', 'runoob', 'runoob', '']
print(re.split('(\W+)',' runoob,runoob,runoob.'))#['', ' ', 'runoob', ',', 'runoob', ',', 'runoob', '.', '']
print(re.split('\W+', ' runoob, runoob, runoob.', 1))#['', 'runoob, runoob, runoob.']
print(re.split('a', 'hello world'))#['hello world']  对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(re.split(r':+','runoob:runoob:runoob.'))#['runoob', 'runoob', 'runoob.']


# 正则表达式对象
# re.RegexObject
# re.compile() 返回 RegexObject 对象。
# re.MatchObject
#    group() 返回被 RE 匹配的字符串。
#    start() 返回匹配开始的位置
#    end()   返回匹配结束的位置
#    span()  返回一个元组包含匹配 (开始,结束) 的位置
# 正则表达式模式
# 模式字符串使用特殊的语法来表示一个正则表达式：
# 字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
# 多数字母和数字前加一个反斜杠时会拥有不同的含义。
# 标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
# 反斜杠本身需要使用反斜杠转义。
# 由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。
#下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。
# ^                 匹配字符串的开头
# $                 匹配字符串的末尾。
# .                 匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]             用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]            不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*               匹配0个或多个的表达式。
# re+               匹配1个或多个的表达式。
# re?               匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}            匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
# re{ n,}           精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
# re{ n, m}         匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b              匹配a或b
# (re)              匹配括号内的表达式，也表示一个组
# (?imx)            正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)           正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)           类似 (...), 但是不表示一个组
# (?imx: re)        在括号中使用i, m, 或 x 可选标志
# (?-imx: re)       在括号中不使用i, m, 或 x 可选标志
# (?#...)           注释.
# (?= re)           前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)           前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
# (?> re)           匹配的独立模式，省去回溯。
# \w                匹配数字字母下划线
# \W                匹配非数字字母下划线
# \s                匹配任意空白字符，等价于 [\t\n\r\f]。
# \S                匹配任意非空字符
# \d                匹配任意数字，等价于 [0-9]。
# \D                匹配任意非数字
# \A                匹配字符串开始
# \Z                匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
# \z                匹配字符串结束
# \G                匹配最后匹配完成的位置。
# \b                匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B                匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等。       匹配一个换行符。匹配一个制表符, 等
# \1...\9           匹配第n个分组的内容。
# \10               匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。


# 正则表达式实例
# [Pp]ython           匹配 "Python" 或 "python"
# rub[ye]               匹配 "ruby" 或 "rube"
# [aeiou]               匹配中括号内的任意一个字母
# [0-9]                   匹配任何数字。类似于 [0123456789]
# [a-z]                   匹配任何小写字母
# [A-Z]                  匹配任何大写字母
# [a-zA-Z0-9]        匹配任何字母及数字
# [^aeiou]              除了aeiou字母以外的所有字符
# [^0-9]                 匹配除了数字外的字符
#
#  特殊字符类
# .                  匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d                匹配一个数字字符。等价于 [0-9]。
# \D                匹配一个非数字字符。等价于 [^0-9]。
# \s                匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S                匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w                匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W               匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。