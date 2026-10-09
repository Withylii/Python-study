
#*4.1遍历整个列表
#如果需要对列表中的每一个元素都进行相同的操作，可使用python中的for循环



#?深入研究循环
#使用for循环，需要定义一个新变量，即：for 新变量 in 列表变量
#!格式：for 新变量 in 列表变量:
#新变量可以取任意名称。但建议取与列表相关的名称，以便明白操作对象性质。以单复数形式命名，可有助判断代码段处理的是单个列表元素还是会整个列表
lists=['haruka','chihaya','miki']
for list in lists:                  #这里的list就是一个新变量，或者说是临时变量，就是用来指代列表里的每一个元素的
    print(list)
#!注意空格缩进！！！还有最后的冒号！！！



#?在for循环中执行更多的操作
#!for循环实质上，是依次对于列表中的每一个元素进行缩进里的操作，当对列表第一个元素执行完缩进里的操作后，就会对第二个列表元素进行缩进里的操作。因此，for语句下缩进的操作是一个“流水线模具”，是对所有列表元素都会进行的操作，可以省去大量重复操作！！
lists=['haruka','chihaya','miki']
for girl in lists:
    print(f'{girl.title()},you are the most beautiful girl that I have ever seen,really!\nBy the way,would you marry me,please?\n')
    


#?在for循环结束后执行一些操作
#如果想要输出总结性内容，而非对列表各个内容进行操作，只需跳出缩进，取消空格，直到与for循环同等级的缩进，输出print即可
lists=['haruka','chihaya','miki']
for girl in lists:
    print(f'{girl.title()}，你身为小偶像，需要再多加练习才行呀！\n')
print(f'好了，{lists[0].title()},{lists[1].title()},{lists[2].title()},你们跟我走，去舞蹈室练习吧。')