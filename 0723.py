#
#
# class shili(object):
#     __getinstance=None
#     def __new__(cls):
#         if not cls.__getinstance:
#             cls.__getinstance=object.__new__(cls)
#         return cls.__getinstance
#     def __init__(self):
#         print("nihao")
#     def say(self):
#         print("shuoh")
# n=shili()
# n.say()
# print(id(n))
# m=shili()
# print(id(m))
# .编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生

# class Student:
#     count=0
#     def __init__(self,name,age,banji):
#         self.name=name
#         self.age=age
#         self.banji=banji
#         Student.count+=1
#     def say(self):
#         print("niaho",self.name)
# a=Student("李明",23,"三班")
# b=Student("小黄",23,"三班")
# c=Student("小红",23,"三班")
# print(Student.count)
# a.say()
# b.say()
# c.say()
# 编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
# class B(object):
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def handle(self):
#         print("我的名字{}，我今年{}".format(self.name,self.age))
# class A(B):
#     def __init__(self,n,a,w):
#         super().__init__(n,a)
#         self.wo=w
#     def handle(self):
#         print("我的名字{}，我今年{},我的工资{}".format(self.name,self.age,self.wo))
# a=A("李小花",23,5000)
# a.handle()
# 编写程序, 如下有三点要求：
#
# 自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
# 定义用户类，定义方法db，例如 执行obj.db可以拿到用户数据结构
# 在该类中实现登录、退出方法, 登录成功将状态(status)修改为True, 退出将状态修改为False(退出要判断是否处于登录状态).
# 密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于30秒即不允许登录)
import json
import time

# class User:
#     def __init__(self):
#         self.user_dic=self.read()
#         self.username=""
#     def wirte(self):
#         with open("dic","w") as f:
#             json.dump(self.user_dic,f)
#     def read(self):
#         with open("dic" ,"r") as f:
#             user_dic=json.load(f)
#         return user_dic
#     def db(self):
#         print("shuju",self.user_dic)
# a=User()
# a.db()
# user={
#     "egon":{"password":123,'status':False,'timeout':0},
#     "alex":{"password":456,'status':False,'timeout':0},
# }
# def zeng(user):
#     zj={}#用花括号
#     xuehao=input("输入学号")
#     if xuehao not in user:
#         zj["name"]=input("请输入名字")#zj["name"]这里是zj
#         zj["age"]=input("请输入年龄")
#         zj["sex"]=input("请输入性别")
#         zj["address"]=input("请输入地址")
#         user[xuehao]=zj#这里是user
#         print(zj)

# a.zhuce()
# a.deng_lu()
user=[{'name': 'lisi', 'mima': '123'},{'name': 'li', 'mima': '12345'}]
# n=input("shuru")
for n in user:
    print(n)
# class loginn:
#     def login(self):
#         i=0
#         while True:
#             name=input("请输入姓名")
#             if name in user:
#                 pa=int(input("输入密码"))
#                 if pa==user[name]["password"]:
#
#                     print("登录成功")
#                     break
#                 else:
#                     i+=1
#                     if i == 2:
#                         self.wait_time()
#                     print("登录失败")
#                     again=input("输入1继续，按任意键退出")
#                     if again =="1":
#                         continue
#                     else:
#                         break
#             else:
#                 i+=1
#                 if i == 2:
#                     self.wait_time()
#                 print("姓名输入错误")
#                 again = input("输入1继续，按任意键退出")
#                 if again == "1":
#                     continue
#                 else:
#                     break
#     def wait_time(self):
#         print("输入错误，请等待...")
#         return time.sleep(5)
#
# lo=loginn()
# lo.login()

# with open("ttzz.txt","r") as f:
#     user=eval(f.read())
#     # print(user)
# n=input("输入用户名")
# for i in range(1,4):
#     if n == user[i]["name"]:
#         mi=int(input("输入密码"))
#         if mi ==user[i]["mima"]:
#             print("登录成功")
#         else:
#             break
##注册登录
# class zhuce_denglu:
#     def zhuce(self):
#         with open("ttzz.txt","r",encoding="utf-8") as f:
#             file=eval(f.read())
#             list={}
#             num=len(file)+1
#             if num not in file:
#                 # print("1111")
#                 list["name"]=input("输入名字")
#                 list['password']=input("输入密码")
#                 file[num]=list
#                 with open("ttzz.txt","w") as f:
#                     file1=f.write(str(file))
#             else:
#                 print('已有该用户')
#     def deng_lu(self):
#         with open("ttzz.txt","r") as f:
#             user=eval(f.read())
#             # print(user)
#         n=input("输入用户名")
#         for i in range(1,4):
#             if n == user[i]["name"]:
#                 mi=input("输入密码")
#                 if mi ==user[i]["mima"]:
#                     print("登录成功")
#                 else:
#                     print("登录失败")
#     def wait_time(self):
#         print("输入错误，请等待...")
#         return time.sleep(5)
# a=zhuce_denglu()
# a.deng_lu()


#按照一下要求定义一个游乐园门票类，并尝试计算2个成人+1个小孩子平日票价
# 1.平日票价100元
# 2.周末票价为平日票价120%
# 3.儿童半价
# class piao():
#     pingr=100
#     week=pingr+pingr*0.2
#     def jisuan(self,day,man,child):
#         # print(day,man,child)
#         if 0<day<7:
#             pj=self.pingr
#             erpj=self.pingr*0.5
#             s=man*pj+child*erpj
#         elif day==7:
#             pj=self.week
#             erpj=self.week*0.5
#             s = man * pj + child * erpj
#         else:
#             print("星期输入错误")
#         return s
# a=piao()
# print("2个成人+1个小孩子平日票价为：",a.jisuan(5,2,1))



