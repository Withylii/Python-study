#练习4.11
pizza=['菠萝披萨','烤肉披萨','金枪鱼披萨','土豆片披萨','夏威夷披萨']
copy=pizza[:]
pizza.append('1')
copy.append('2')
for n in pizza:
    print(n)
for m in copy:
    print(m)