#输入一个数字列表，回车键结束，删除列表中指定的数字——4
#num_array[] = input("imput nums:")
#NumArray=[1,3,6,4,8,3,1,4,0,2]
num_in = input("用空格来间隔:")
NumArray = [int(n) for n in num_in.split()]
d = int(input("输入你想删除的数字："))
while d in NumArray:
    NumArray.remove(d)
print(NumArray)