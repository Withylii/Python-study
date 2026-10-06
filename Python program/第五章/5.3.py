
#*5.3 if语句



#?简单的if语句
#注意缩进



#?if-else语句
#如果if语句条件测试为False，那么就会去执行else语句，总共就两种情况



#?if-elif-else语句
#如果你需要检查两个以上的情形，那么可以用此情形
#python会依次检查每个条件测试，直到遇到通过了的条件测试
import random
chizi=['年','令','白铁','能天使','凯尔希']
n=random.choice(chizi)
if n == '年':
    print(f'好耶，我抽到了岁家限定{n}！')
elif n == '令':
    print(f'好耶，我抽到了岁家限定{n}！')
else:
    print(f'不要啊，怎么歪了{n}啊！！')





#?使用多个elif语句
#其实就是多个条件，多打几个elif，只要保证头是if，尾是else，中间是elif，就ok



#?省略elif代码块
#其实也可以最后结尾只写elif来囊括所有可能范围。
#不过因为else包罗万象，比如你要是范围是数字，输入为文本，他也给你放else里。所以elif可以把补集定义清楚，避免乱七八糟的情况
import random
chizi=['年','令','白铁','能天使','凯尔希']
n=random.choice(chizi)
if n == '年':
    print(f'好耶，我抽到了岁家限定{n}！')
elif n == '令':
    print(f'好耶，我抽到了岁家限定{n}！')
elif n== '白铁' or n== '能天使' or n== '凯尔希':
    print(f'不要啊，怎么歪了{n}啊！！')



#?测试多个条件
#有时候，必须要检查你所关心的所有条件，这时应使用一系列不包含elif和else代码块的简单if语句
#在可能有多个条件为True，且需要在每个条件为True时都采取相应措施时，适合使用这种方法
#因为如果用elif或else语句，其中一个为True，那么派森会省略其余元素的条件测试
l=['令','年','夕']
if '令' in l:
    print(f'太好了，我有了{l[0]}')
if '年' in l:
    print(f'太好了，我有了{l[1]}')
if '夕' in l:
    print(f'太好了，我有了{l[2]}')
print(f'好了，我集齐了三姐妹')
#!总之，如果你想只运行一个代码块，那就用if-elif-else语句；如果要运行多个代码块，那就要使用一系列独立的if语句