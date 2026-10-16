#练习5.2
#检查两个字符串是否相等和不等
s1='baba'
s2='mama'
if s1 == s2:
    print(True)
else:
    print(False)
if s1 != s2:
    print(True)
else:
    print(False)
print(f'\n')
    
#使用lower（）方法的条件测试
s1='baba'
s2='Baba'
if s1 == s2.lower():
    print(True)
else:
    print(False)
if s1 != s2.lower():
    print(True)
else:
    print(False)
print(f'\n')

#涉及相等、不等、大于、小于、大于等于、小于等于的数值比较
a=1
b=2
c=3
d=4
if a > c:
    print(True)
else:
    print(False)
if a <= c:
    print(True)
else:
    print(False)
print(f'\n')

#使用关键字and和or的条件测试
a=1
b=2
c=3
d=4
if a+b == c or a+b == d:
    print(True)
else:
    print(False)
if a+b ==c and a+b == d:
    print(True)
else:
    print(False)
print(f'\n')

#测试特定的值是否在列表中
l=[1,2,3,4,5]
if 1 in l:
    print(True)
else:
    print(False)
if 1 not in l:
    print(True)
else:
    print(False)