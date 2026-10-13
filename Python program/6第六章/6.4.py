
#*嵌套
#嵌套，比如说，可以在列表中嵌套字典，也可以在字典中嵌套列表，甚至在字典中嵌套字典。



#?字典列表/在列表中存储字典
aliens=[]
for alien_number in range(30):
    new_alien={'color':'blue'}
    aliens.append(new_alien)
print(f'\n')
#!随机变量1里的new_alien绝不等于随机变量2里的new_alien!!!!
#!第 1 次循环里的 new_alien，和第 2 次循环里的 new_alien，绝对不是同一个对象。它们不仅值一样，连名字也一样，但它们在计算机内存里是完全独立的两个字典。
idols=[]
for n in range(10):
    idol={'name':'haruka',          #这是一个缩进内新建的变量，也是个字典，这有这样才相当于连续多次重复打印相同的字典！！
          'style':'passion',
          'color':'red'
         }
    idols.append(idol)
for m in idols[:5]:                 #idols是一个列表，而列表里的元素是字典
    print(m)
print(f'\n')
#以这种方式，每个相同的字典其实都是互相独立的，只有这样我们才能独立的修改其中某一字典的值！
#如果我们要修改其中的元素，可以用在for语句中用if条件，反正是列表呗，直接索引指定位置


idols=[]
for n in range(10):
    idol={'name':'haruka',
          'style':'passion',
          'color':'red'
         }
    idols.append(idol)
for m in idols[:3]:                    #批量更改列表字典
    if m['color']=='red':              #这就是对于前三个字典中，要是有一个键的值符合这个if条件，那么就会毫不留情执行下面的代码
        m['name']='chihaya'
        m['style']='sorrow'
        m['color']='blue'
idols[0]={'name':'miki',
          'style':'cute',
          'color':'yellow'
         }
for s in idols[:6]:
    print(s)
print(f'\n')




#?在字典中存储列表












#?在字典中存储字典