'''
有这么一个数组,[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56],请以100
为分界线，讲小于等于100的放到一个新数组中，将大于100的放到另一个新数组中
list1=[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
list2=[]
list3=[]
for i in list1:
    if i<100:
        list2.append(i)
    else:
        list3.append(i)
print(list2)
print(list3)

请用python打印出99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}='.format(i,j),i*j,end=' ')
    print('')


# 输入某年某月某日，判断这一天是这一年的第几天？
x=[31,28,31,30,31,30,31,31,30,31,30,31]
year=2019
mon=2
day=31
sum=0
if year%4==0 and year%100!=0 and year%400==0:  #闰年加一天
    for i in range(mon-1):
        sum=x[mon]+sum
    sum=sum+day+1
else:
    for i in range(mon-1):
        sum=x[mon]+sum
    sum=sum+day
print('今天是2019年的第{}天'.format(sum))

'''
# 有一个5 位数的任意数字，请将数字的顺序颠倒。（不是长的像数字的字符串哦）'''
# a=input("输入一个5位数的数字：")
# b=a[::-1]
# print(b) 字符串了
'''
c=52134
print('c的格式为',type(c))
b=str(c)    
print('b的格式为',type(b))
'''


# 重新自己实现一遍，我们课堂上讲的【发红包】功能
a=input('输入你想发红包的金额')
if a
if a >0.01 and a<=200 and a!=0:
    print('你发红包的金额为{},发送成功'.format(a))
else:
    print('发送失败')


