# 1、写一个函数，传入一个字符串，将字符串追加写入test.txt 文件内
# def txt(str):
#     with open("test.txt","a") as file:
#         file.write(str)
#         look=file.read(255)
#         return look
# str=input("请输入字符")
# t=txt(str)
# print(t)
# 2、写一个函数，传入一个文件名，根据传入的文件名，读取文件内容并返回给调用者
# def name(nm):
#     with open(nm,"r") as file:
#         look=file.read(255)
#         return look
# n=name("test.txt")
# print(n)

# 3、写一个函数，生成1--100内的所有奇数，并写入到文件
# def jishu(nm):
#     with open(nm , "w") as file:
#         for i in range(1,101):
#             if i % 2 != 0:
#                 look=file.write(str(i),end=" ")
#         return look
# nm="test.txt"
# z=jishu(nm)
# print(z)
# def jishu(nm):
#     with open(nm , "w") as file:
#         lo=[i for i in range(1,101) if i %2!=0]
#         # print(lo)
#         look=file.write(str(lo))
#         return look
# nm="test.txt"
# z=jishu(nm)
# print(z)

# 4、定义一个函数，传入两个参数file_name和string，将string的内容追加到file_name文件内
# def Append(file_name,string):
#     with open(file_name,"a")as file:
#         xieru=file.write(string)
#         return xieru
# file_name="test.txt"
# string=input("请输入一串字符")
# a=Append(file_name,string)
# print(a)


# 5、定义一函数，传两个数 file_name,new_file_name，读取file_name 文件的内容，过滤文件文件所有的数字和空格，
# 将过滤后的内容写入new_file_name 文件 如果 new_file_name 文件不存在则创建
# def chuandi(file,newfile):
#     with open(file,"r") as file:
#         readfile=file.read(255)
#
#     with open(newfile,"w") as new:
#         # print(readfile)
#         newwrite=new.write(readfile)
#         return newwrite
# file="test.txt"
# newfile="ttzz.txt"
# c=chuandi(file,newfile)
# print(c)

# 6、写一个函数，传入两个参数file1和file2 将file1文件的内容和file2文件的内容合并后返回给调用者
# def hebing(file1,file2):
#     list=[]
#     with open(file1,"r") as f1:
#         look1=f1.read(255)
#     with open(file2,"r") as f2:
#         look2=f2.read(255)
#     list.append(look1)
#     list.append(look2)
#     return list
# n1="test.txt"
# m2='ttzz.txt'
# c=hebing(n1,m2)
# print(c)



# # 7、写一个函数，统计test.txt. 文件内，一共有多少行内容
# def hanshu(n):
#     count=len(open(n,"r").readlines())
#     return count
# n="test.txt"
# print(hanshu(n))

# count = len(open("test.txt",'rU').readlines())
# print (count)
#另一种方法
# count = 0
# thefile = open("test.txt", 'r')
# while True:
#     buffer = thefile.read()
#     if not buffer:
#         break
#     else:
#         count = 1
#     count += buffer.count('\n')
# thefile.close()
#
# print(count)

# 8、写一个函数，提取出test.txt 文件内所有的大写字母
# def tiqu(file):
#     list=[]
#     with open(file,"r") as f1:
#         all=f1.read(255)
#         for i in all:
#             if i.isupper():
#                 list.append(i)
#         return list
# file="test.txt"
# z=tiqu(file)
# print(z)
# 文件管理系统 （尽量使用函数实现）
#
# import os
# import os.path
# |  1、查看目录列表（列出目录下所有的文件和目录）
# 显示出是文件还是目录
# def look(dir):
#     # list=[""]
#     list1=[]
#     list=os.listdir(dir)
#     for i in list:
#         if os.path.isdir(list):
#             print(i)
#
# dir="D:\Python空间"
# lo=look(dir)
# print(lo)







# |  2、创建目录
# |  3、删除文件或目录
# 需要检查文件或目录是否存在
#   可以删除文件也可以删除目录
# 4、重命名文件或目录
# 需要检查文件或目录是否存在
# |  5、为文件添加前缀
#   为当前目录下的所有文件，添加文件名前缀，前缀需要用户输入
# |  6、删除文件前缀
#       删除当前目录下所有文件名的前缀，前缀需要用户输入
# |  7、切换目录
# 切换目录后，显示目录下所有文件和目录



# 写一个函数，实现传入不定个数的字符串，拼接第一个和最后一个字符串
# def chuanru(a):
#     # list=[]
#     s=len(a)-1
#     # print(s)
#     list=a[0]+a[s]
#     return list
# n="abcd","abde","dded"
# z=chuanru(n)
# print(z)

# 5、定义一个函数，检查用户传入的对象（序列类型）是否包含空元素
# def chuanru(list):
#     n=1
#     for i in list:
#         if i.isspace():
#             n=0
#     return n
# list=" abd   defg"
#
# print(chuanru(list))

# 6、写函数，检查传入列表的元素长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def two(list):
#     le=len(list)
#     if le>2:
#         z=list[:2]
#     else:
#         z=list
#     return z
# list=["a","b","cde"]
# tt=two(list)
# print(tt)

# 7、写函数，检查获取传入列表或元组对象中的的所有奇数，并将其作为新列表返回给调用者。
# def jishu(lo):
#     list=[]
#     for i in lo:
#         if i%2!=0:
#             # ji=i
#             list.append(i)
#     return list
# lo=[1,2,5,6,7,8,9]
# so=jishu(lo)
# print(so)

class People():
    tax=0
    def __init__(self,n,a,w,s):
        self.name=n
        self.age=a
        self.work=w
        self.salary=s
        self.__energy=100
    def eat(self,money):
        self.__energy+=10
        self.salary-=money

        return self.__energy,self.salary
    def working(self,tax):
        s=self.salary*0.2
        tax=tax+s
        self.__energy-=30
        return self.salary,self.__energy
    def sleep(self):
        self.__energy+=60
        return self.__energy
    def say(self):
        a=("我叫{}，今年{}，我的职业是{}，工资是{}".format(self.name,self.age,self.work,self.salary))
        return a
    def get_energy(self):
        self.__energy<=100
        self.__energy>=0
        return self.__energy
class Woman(People):
    def __init__(self, n, a, w, s,mon):
        People.__init__(self,n,a,w,s)
        self.money=mon

    def shoping(self,money):
        self.salary-=self.money
        return self.salary
class Man(People):
    def __init__(self, n, a, w, s):
        People.__init__(self,n,a,w,s)
    def say(self):
        s=("我叫{}，今年{}，我的职业是{}，工资是{}".format(self.name, self.age, self.work, self.salary))
        b=("hahaha")
        return s,b
a=People("李思思",23,"主持人",50000)
print(a.tax)
print("working",a.working(0))
print("eat",a.eat(20))
print("sleep",a.sleep())
print(a.say())
print(a.get_energy())
wo=Woman("李思思",23,"主持人",50000,4000)
print(wo.shoping(50000))
ma=Man("李思思",23,"主持人",50000)
print(ma.say())





