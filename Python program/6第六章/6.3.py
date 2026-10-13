
#*遍历字典



#?遍历所有的键值对
#使用.items()方法实现键值对分组打印
#使用for循环来实现
idol={'red':'天海春香',
      'blue':'如月千早',
      'yellow':'星井美希',
      'mama':'三浦梓'
      }
for style,girl in idol.items():
    print(girl)
print(f'\n')
#.items()方法，.items() 就像是一个“快递分拣员”。它把字典里的每对键值打包成一个“包裹”（元组），然后交给你。你用两个变量去接，就是“拆包”；用一个变量去接，就是“直接拿走整个包裹”。
#!.items() 方法在底层，会把字典里的每一对“键值对”，打包成一个小元组交给你。
#当你的字典在遍历时，它实际吐出来的数据是这样的：
#('red', '天海春香')、('blue', '如月千早')...
#!当输入两个变量名时，派森会自动进行解包操作，将第一个元素赋给第一个变量，将第二个元素赋给第二个变量，以此类推每个键值对。
#!因此，前一个变量名一定是键名，第二个变量名一定是值名
#!如果你只赋予一个变量，那么就只会将整个键值对打包在一个变量里
#!标准写法永远是 for 键变量名, 值变量名 in 字典.items():
#!顺序不能颠倒：元组是有顺序的。第一个变量一定接的是“键”，第二个变量一定接的是“值”。如果你写反了（比如 for girl, style in ...），那 girl 就会拿到 'red'，style 就会拿到 '天海春香'，逻辑全乱。
#!数量必须匹配：for 后面的变量数量，必须和 .items() 吐出的元组长度一致。只能是 2 个。如果你写 for a, b, c in ...，会直接报错 ValueError: too many values to unpack（值太多无法解包）。
#!没有返回值修改（原地修改）：.items() 只是提供一种“视图”，它不会修改原字典（跟你之前在乎的 .sort() 原地修改完全不同，这里是只读的）。
#!不允许边遍历边改字典：如果你在 for ... in dict.items(): 循环体内部去 del 字典里的键，或者添加新键，Python 会立刻报错 RuntimeError: dictionary changed size during iteration（字典在迭代时改变大小）。如果你真需要修改，请遍历字典的副本（比如 list(idol.items())）。



#?遍历字典中的所有键
#!在不需要使用字典中的值时，.keys()方法很有用
#!也可以用两个变量，然后只打印第一变量
#.keys()方法会提取字典中的所有键，并将其赋给你定义的变量
idol={'red':'天海春香',
      'blue':'如月千早',
      'yellow':'星井美希',
      'mama':'三浦梓'
      }
for girl in idol:          #默认啥也不打，是和.key()方法有关的，和.items()无关
    print(girl)
print(f'\n')
#如果你不用.keys()方法，python则会默认遍历字典中的所有键
#所以，使用显式的key或是隐式，取决于你。
idol={'red':'天海春香',
      'blue':'如月千早',
      'yellow':'星井美希',
      'mama':'三浦梓'
      }
for girl in idol.keys():
    print(f'这是小偶像{idol[girl]}.')
    if girl == 'red' or girl == 'mama':       #说明这里girl还是一个键，只有 字典[键名] 才指代的是键的值
        fav=idol[girl]
        print(f'\t顺带一提，{fav}是我非常喜欢的偶像！')
print(f'\n')



#?按特定的顺序遍历字典中的所有键
#使用sorted()函数，按首字母排序，字符顺序大小排序。
#使用sorted()函数来获得按特定顺序排列的副本
#貌似这个只能按键名首字母来排序？？？！
idol={'red':'haruka',
      'blue':'chihaya',
      'yellow':'miki',
      'mama':'azusa'
      }
l=sorted(idol.values())
for type in l:
    print(f'这位是小偶像{type}')
print(f'\n')



#?遍历字典中的所有值
#使用.values()方法，会给你返回一个字典里所有值的列表
#如果你想剔除重复项，可以用set()函数
#set()函数会输出一个去掉重复键值的集合。注意！是一个集合！！！
#集合和字典很容易混淆，因为它们都是用一对花括号定义的。
#当花括号内没有键值对时，定义的很可能是集合
#不同于列表和字典，集合不会以特定的顺序存储元素。集合，是随机无序的！！！
idol={'red':'haruka',
      'blue':'chihaya',
      'yellow':'miki',
      'hoshii':'miki',
      'mama':'azusa'
      }
l=sorted(set(idol.values()))
for type in l:
    print(type.title())
#!使用set()函数，生成的内容是随机无序的！！
#列表（List）是有序的“排队”，字典（Dict，Python 3.7+）是按插入顺序排队，而集合（Set）是“随便扔进袋子里的”，不排队。
#按输入顺序，另寻方法
#按字母顺序，sorted（）函数
#集合