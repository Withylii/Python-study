import random

print("🎮 欢迎来到猜数字游戏！")

while True:
    secret = random.randint(1, 100)
    count=0
    
    print("我已经想好了一个 1 到 100 之间的数字，猜猜看是多少？")

    while True:
         guess = int(input("请输入你的猜测："))
         count=count+1
         
         if guess < secret:
                     print("📉 太小了！再大一点试试？")
         elif guess > secret:
                     print("📈 太大了！再小一点试试？")
         else:
                     print("🎉 恭喜你，猜对了！")
                     print(f"你总共猜了 {count} 次。")
                     break
    
        
    again=input("Try again?(y/n)")
    if again !="y":
       print("拜拜了您内!")
       break
