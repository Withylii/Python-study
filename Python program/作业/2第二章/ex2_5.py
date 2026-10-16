#练习2.5
fn='albert'
ln='einstein'
n=f'{fn} {ln}'
sentence=f'{n.title()} once said,"A person who never made a mistake never tried anything new."'
print(sentence)
#f字符串大括号内如果加上引号，那就是文本变量，不是变量，会直接输出文本。只有在大括号外加引号，才能起到拼接引号的作用