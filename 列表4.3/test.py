# coding=utf-8
# author:GCS
#打印1-20：
#for num in range(1,21):
#    print(num)

#打印1-1000000
#for num in range(1,1000001):
#    print(num)

#计算1-1000000的总和：
#a = list(range(1,1000001))
#print(min(a))
#print(max(a))
#print(sum(a))

#打印1-20中的奇数：
#a = list(range(1,21,2))
#for num in a:
#    print(num)

#创建一个列表包含3-30中能被3整除的数字：
#a = list(range(3,31,3))
#for num in a:
#    print(num)

#使用列表解析生成一个列表，包含前10的整数的立方
a = [num**3 for num in range(1,11)]
print(a)
