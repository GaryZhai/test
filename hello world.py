import sys
def deal_char(li):
    list=[]

    # list.append(float(max(li)))
    # list.append(float(min(li)))
    upper=0
    lower=0
    num=0
    other=0
    # str.__len__()
    for i in  range(li.__len__()):
        if li[i].isupper():
            upper+=1
        elif li[i].islower():
            lower+=1
        elif li[i].isnumeric():
            num+=1
        else:
            other+=1
    list.append(upper)
    list.append(lower)
    list.append(num)
    list.append(other)

    print("list:",list)
    return tuple(list)
if __name__=="__main__":
    # print("请输入一个序列：")
    # while
    ll=input("please input some char(or a string):",)

    # print(type(lll))
    deal=deal_char(ll)
    print("tuple contain count with upper char,lower char ,number and others:",deal) 