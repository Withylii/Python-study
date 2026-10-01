
#*管理列表
#python提供了列表排序的方法



#?使用.sort()方法对列表进行永久排列
#.sort()方法会使列表中的元素按首字母顺序排序
#如果首字母大小写不一，.sort() 会默认把大写字母排在前面，小写字母排在后面。
#只有当列表里的元素全都是同一类型（比如全是字符串）时，才用 .sort()。
#!.sort()方法无返回值！不能直接print（变量.sort())，因为方法操作后没有值
#!.sort()方法默认是按 ASCII 码（字母顺序）排序。
list=['xrmisde','amiside','xudiaomao']
list.sort()
print(list)
#如果要按与字母顺序相反的顺序排列列表元素，需传递reverse=True即可
list=['xrmisde','amiside','xudiaomao']
list.sort(reverse=True)
print(list)



#?使用sorted()函数对列表进行临时排列
#要保留列表元素原来的排列顺序，并临时以特殊的顺序呈现它们，就可以用sorted()函数
#sorted() 默认也是按 ASCII 码（字母顺序）排序。
#!sorted()函数是有返回值的
#同样如果要按与字母顺序相反的顺序排列列表元素，需传递reverse=True即可
#标准语法是：sorted(列表, reverse=True)
list=['xrmisde','amiside','xudiaomao']
print(sorted(list,reverse=True))



#?反向打印列表
#要反转列表元素的排列顺序，可使用.reverse()方法
#注意，这里的反向，不是指字母大小顺序反向，而是指元素位置反向
#该方法会永久改变列表顺序。若要恢复原顺序，再次执行同一方法即可
#!.reverse()方法没有返回值
list=['xrmisde','amiside','xudiaomao']
list.reverse()
print(list)
#!原地修改（In-place Modification）的无返回值陷阱，仅能单独列出一步操作，不能直接打印或新变量赋值，否则输出为none！！！



#?确定列表的长度
#使用len（）函数，可以确定列表长度
#!这是一个有返回值的函数
list=['xrmisde','amiside','xudiaomao']
list=len(list)
print(list)

list=['xrmisde','amiside','xudiaomao']
print(len(list))