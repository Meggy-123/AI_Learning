# # 数字运算
# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**2) #a的2次方

# # 字符串处理
# text="Artificial Intelligence"

# print(text)
# print(len(text))
# print(text.upper()) #将所有字母转为大写
# print(text.lower()) #将所有字母转为小写

# # 列表
# scores=[90,85,95,88]
# print(scores)
# print(scores[0])
# scores.append(100) #在队列尾添加一个值为100的数
# print(scores)
# scores.remove(85)  #删除值为85的数
# print(scores)
# result=scores.pop(2)      #将序号为2的数删除，并记录到result中
# print(scores,",",result)
# del scores[1] #删除序号为1的数
# print(scores)
# del scores[0:1]
# print(scores) #删除在0到1序号之间的数，不包括1
# scores.clear() #清空整个列表
# print(scores)

# #列表练习
# scores=[85,90,78,92,88]
# a=sum(scores)
# ave=a/len(scores)
# print(a)
# print(ave)

# #条件判断
# score=85
# if score>=90:
#     print("优秀")
# elif score>=60:
#     print("及格")
# else:
#     print("需要努力")

# #AI学习等级评估器
# hours=int(input("请输入学习时间:"))#input输入的是字符串，需要将其强转为int类型
# if hours>=3:
#     print("优秀")
# elif hours>=1:
#     print("继续努力")
# else:
#     print("需要加强")

# #BMI计算器 v1.0
# high=float(input("请输入您的身高(m):"))
# weight=float(input("请输入您的体重(kg):"))
# BMI=weight/(high**2)
# print("你的BMI",BMI)
# if BMI<18.5:
#     print("偏瘦")
# elif BMI<24:
#     print("正常")
# elif BMI<28:
#     print("偏胖")
# else:
#     print("肥胖")