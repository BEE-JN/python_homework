#打印消息 "The first three items in the list are:" 再使用切片打印列表前三个元素
#打印消息 "Three items from the middle of the list are:" 再使用切片来打印列表中间的三个元素
#打印消息 "The last three items in the list are:" 再使用切片来打印列表末尾三个元素
a = ["The ","first ","three ","items ","in ","the ","list ","are",":","\n"]
for word in a:
    print(word,end="")
print(a[:3])
b = ["Three ","items ","from ","the ","middle ","of ","the ","list ","are",":","\n"]
for word in b:
    print(word, end="")
print(b[3:6])
c = ["The ","last ","three ","items ","in ","the ","list ","are",":","\n"]
for word in c:
    print(word, end="")
print(c[-5:-2])

#复制一个列表（不能直接用变量复制，需要用切片）
a = [1,2,3,4,5,6]
b = a[:]
print(a)
print(b)
a.append(8) #为了验证a和b是否为同一个数组
b.append(9)
print(a)
print(b)    #输出a和b验证，若两者不同则说明复制成功