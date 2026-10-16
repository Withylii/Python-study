#练习5.6
import random
age=random.choice(range(1,101))
if age < 2:
    print(f'This is a {age} years old infant!')
elif age >=2 and age <4:
    print(f'This is a {age} years old baby!')
elif age >=4 and age <13:
    print(f'This is a {age} years old children!')
elif age>=13 and age <18:
    print(f'This is a {age} years old teenager!')
elif age>=18 and age <65:
    print(f'This is a {age} years old young and middle-aged people!')
else:
    print(f'This is a {age} years old man!')
