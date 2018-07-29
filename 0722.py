# 编写一个函数，接收传入的字符串，统计大写字母的个数、
# 小写字母的个数、数字的个数、其它字符的个数，并以元组的方式返回这些数，然后调用该函数；
# import sys
# def hanshu(str):
#     list=[]
#     bigs=0
#     small=0
#     num=0
#     qita=0
#     for i in range(str.__len__()):
#         # a=ord(str[i])
#         if str[i].isupper():
#             bigs+=1
#             # return bigs
#         elif str[i].islower():
#             small+=1
#             # return small
#         elif str[i].isnumeric():
#             num+=1
#             # return num
#         else:
#             qita+=1
#             # return qita
#     list.append(bigs)
#     list.append(small)
#     list.append(num)
#     list.append(qita)
#     print(list)
#     return tuple(list)
# if __name__=="__main__":
#     str=input("请输入一段字符")
#     print(hanshu(str))

# 编写一个函数，计算传入的元组的最大值、最小值和平均值，并以列表的方式返回，然后调用该函数
# def value(mm):
#     list=[]
#     max=0
#     min=mm[0]
#     s=0
#     for i in range(7):
#         if mm[i]>max:
#             max=mm[i]
#         elif mm[i]<min:
#             min=mm[i]
#         s+=mm[i]
#     pj=s/len(mm)
#     list.append(max)
#     list.append(min)
#     list.append(pj)
#     print(list)
#     return list
#
# mm=[2,3,4,1,5,7,8]
# m=value(mm)
# print(m)
# 编写一个函数，输入三个数，作为三角形的三个边长，计算三角形的面积
# （p=(a+b+c)/2）
# S=sqrt[p(p-a)(p-b)(p-c)]
# =sqrt[(1/16)(a+b+c)(a+b-c)(a+c-b)(b+c-a)]
# =1/4sqrt[(a+b+c)(a+b-c)(a+c-b)(b+c-a)]
import math
def three(a,b,c):
    p = (a + b + c) / 2
    if a+b>c or b+c>a or a+c>b:
        z=p*(p - a)*(p - b)*(p - c)
        s = math.sqrt(z)
        print(s)
a,b,c=4,5,6
bi=three(a,b,c)
print(bi)

