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




# #BMI分析器v2.0

# def bmi(weight,height):
#     value=weight/(height**2)
#     return value
# def bmi_category(bmi_value):
#     if bmi_value<18.5:
#         return "偏瘦"
#     elif bmi_value<24:
#         return "正常"
#     elif bmi_value<28:
#         return "偏胖"
#     else:
#         return "肥胖"

# weight=float(input("请输入体重(kg)："))
# height=float(input("请输入身高(m)："))
# result=bmi(weight,height)
# print("您的BMI指数为：", result)
# print("您的BMI分类为：", bmi_category(result))



# #BMI分析器v3.0
# def calculate_bmi(weight,height):
#     return weight/(height**2)

# def bmi_category(bmi):
#     if(bmi<18.5):
#         return "偏瘦"
#     elif(bmi<24):
#         return "正常"
#     elif(bmi<28):  
#         return "偏胖"
#     else:
#         return "肥胖"

# def save_record(data):
#     with open("01_Python\\projects\\bmi_health_system\\bmi_records.txt", "a") as file:
#         file.write(f"{data['name']},{data['weight']},{data['height']},{data['bmi']},{data['category']}\n")

# def main():
#     try:
#         name=input("请输入您的姓名：")
#         weight=float(input("请输入体重(kg)："))
#         height=float(input("请输入身高(m)："))

#         bmi_value=calculate_bmi(weight,height)
#         category=bmi_category(bmi_value)
#         print(f"您的BMI值为：{bmi_value:.2f}")
#         print(f"您的体重状况为：{category}")
#         save_record({
#             "name": name,
#             "weight": weight,
#             "height": height,
#             "bmi": bmi_value,
#             "category": category
#         })
#     except ValueError:
#         print("输入无效，请输入有效的数字。")
# if __name__ == "__main__":
#     main()

#bmi分析器v4.0
from bmi import calculate_bmi,bmi_category
from file_manager import save_record

def main():
    name=input("姓名:")
    weight=float(input("体重(kg):"))
    height=float(input("身高(m):"))
    bmi=calculate_bmi(weight,height)
    category=bmi_category(bmi)
    print(bmi)
    print(category)
    save_record({
        "name": name,
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    },"01_Python/projects/bmi_health_system/bmi_records.txt")
if __name__=="__main__":
    main()