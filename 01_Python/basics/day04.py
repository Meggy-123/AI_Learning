#第一个函数
# def hello():
#     print("Hello, World!")

# hello()

# #函数参数
# def greet(name):
#     print("Hello,", name)

# greet("Alice")
# greet("Bob")
# greet("Charlie")

# #多个参数
# def area(length,width):
#     result=length*width
#     print(result)
# area(5,10)

# #return返回值
# def add(a,b):
#     return a+b

# result = add(5, 10)
# print(result)

# #练习函数
# def calculate_average(scores):
#     total=sum(scores)
#     average=total/len(scores)
#     return average

# scores=[85,90,78,92,88]
# result=calculate_average(scores)
# print("平均成绩为：", result)

#今日项目:BMI分析器v2.0

def bmi(weight,height):
    value=weight/(height**2)
    return value
def bmi_category(bmi_value):
    if bmi_value<18.5:
        return "偏瘦"
    elif bmi_value<24:
        return "正常"
    elif bmi_value<28:
        return "偏胖"
    else:
        return "肥胖"

weight=float(input("请输入体重(kg)："))
height=float(input("请输入身高(m)："))
result=bmi(weight,height)
print("您的BMI指数为：", result)
print("您的BMI分类为：", bmi_category(result))

