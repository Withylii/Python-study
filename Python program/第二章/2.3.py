#字符串
#字符串（string）就是一系列字符。在派桑中，用引号引起的都是字符串，其中引号可以是单引号，也可以是双引号。
#字符指的就是一系列乱七八糟的字母汉字数字符号，然后加个引号串起来，引号一串就叫做“字符串”，还挺生动形象“字符串”本身也是个字符串
#引号必须用英文输入！！！必须都是英文半角输入法！！！
"this is a string"
'this is also a string'
#单引号双引号随便互相包含，但是绝对不能单包单，双包双！！
#包含同种引号的方法：
#1，使用反斜杠\转义，即在同一引号前加反斜杠代表了这是“内部”的引号，转义了。在里面的单引号前面加一个反斜杠 \，告诉 Python：“这个单引号是字符串的内容，不是结束标志。”
s = "He said \"Hello\" to me"
print(s) # 输出：He said "Hello" to me

v='I\'m a hardworking student.'
print(v)
#2，使用“三引号”法，三引号 ''' 或 """ 强大得多，里面可以随意包含单引号或双引号，还能换行。
#三引号法，最两边的三引号不能够再接同一个引号！如果要引号表示和三引号连着的内容，必须用和三引号不同的引号！！！
s = '''He said: "I'm a robot"'''
print(s)  # 输出：He said: "I'm a robot"

k="""there is a famous saying,'the only "fear" is the fear 'itself.''"""
print(k)
