# -*- coding: utf-8 -*-
import types
print('test!!!')
print 100 + 200 + 300
a = 6
if a > 2:
    print 'yes'
elif a > 4:
    print 'no'
else:
    print 'equals'
if True:
    print True
else:
    print False
if 3 > 0 or 3 < 4:
    print ('3大于0小于4')
a = 'aaaa'
b = 'asdasda'
b = b.replace('a', 'b')
print b
classmates = ['mate1', 'mate2', 'mate3']

print len(classmates)
classmates.append('mate4')
classmates.insert(0, 'mate0')
for classmate in classmates:
    print(classmate)
cell = {'mate1': 1, 'mate2': 2, 'mate3': 3}
print cell.get('mate1')
if 'mate1' in cell:
    print 'mate1在'
# set 有序不重复集合
distinct = set([1, 1])
print distinct
# 转型
s = '1'
def checkType(s):
    if type(s) is types.StringType:
        print '字符串'
    else:
        print '不是字符串'


print int(s)

checkType('asfasf')

# def application(environ,start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
# return {b'<h1>Hello, web!</h1>'}


