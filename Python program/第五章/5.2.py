
#*5.2条件测试
#每条if语句的核心都是一个值为True或False的表达式，这种表达式称为条件测试。
#派森根据条件测试的值是True还是False来决定是否执行if语句中的代码。如果为真，则执行if语句后面的代码，如果为假，则忽略。



#?检查是否相等
#大多数条件测试讲一个变量的当前量与特定值进行比较
car='bmw'
if car == 'bmw':    #右边的是我们检查的标准条件，就是看你这个变量car是不是'bmw'，而左边才是挑战者，使我们定义的变量
    print(True)
else:
    print(False)
#一个等号=是赋值操作
#两个等号==才是询问“左边是否等于右边？”



#?如何在检查是否相等时忽略大小写
#在派森中，大小写不同的同一个值会被视为不相等
#如果你只是想检查变量的值是否相等，那么可以将变量的值转换为相同格式，再进行比较
car='Bmw'
if car.lower() == 'bmw':
    print(True)
else:
    print(False)
#这种操作不会改变变量的值，只是比较一下而已。



#?检查是否不等
#!要检查两个量是否不等，可以使用不等运算符（!=）
import random
wanted='塔露拉'
result=['塔露拉','迷迭香','浊心斯卡蒂','克莱门莎']
r=random.choice(result)
if r != wanted:     #这里就用了!=不等运算符。且这里左边一定得是随机变量r！因为这才是你抽取的结果，要是你写ranodm，那相当于再抽一遍！
    print(f'{r}\n又歪了。。。')
else:
    print(f'{r}\n我没歪！')
#注意，if语句中的变量一定要与随机变量保持同名，不然就是你随机抽出一个元素，判断完tf后，再给你随机整个元素当对象，相当于名字和结果两次随机，无法对应



#?数值比较
#==
#!=
#<
#>
#<=
#>=
import random
n=48
m=random.choice(range(1,101))
if m >= n:
    print(f'\nTrue')
else:
    print(f'\nFalse')
print(f'{m}并没有大于等于48')



#?检查多个条件
#你可能想要同时检查多个条件。比如，有时候需要再两个条件同时为True时才能执行相应操作，而有时又只要求两者有一个为True即可，and和or就能助你一臂之力
    #*1，使用and检查多个条件
#要检查两个条件是否都为True，可以用and将两个条件测试合而为一
import random
n1=random.choice(['如月千早','天海春香','星井美希','三浦梓'])
n2=random.choice(range(72,78))
if n1 == '如月千早' and n2==72:
    print(f'\nTrue')
else:
    print(f'\nFalse')
print(f'{n1} {n2}')

    #*2，使用or检查多个条件
import random
n1=random.choice(range(1,54))
n2=random.choice(range(72,78))
if n1 <=23 or n2>=76:
    print(f'\n{n1}或者{n2}中有一个数满足了小于等于23或者大于等于76')
else:
    print(f'\n{n1}和{n2}两个数都不满足小于等于23或者大于等于76的条件')



#?检查特定的值是否在列表中



#?检查特定的值是否不在列表中



#?布尔表达式