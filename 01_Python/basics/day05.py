# #文件写入
# file=open("test.txt","w")
# file.write("Hello AI Engineer")
# file.close()

# #文件写入（推荐）
# with open("test.txt","w") as file:
#     file.write("Hello AI")

# #读取文件
# with open("test.txt","r") as file:
#     content=file.read()
# print(content)

# #异常处理
# try:
#     age=int(input("请输入年龄："))
# except:
#     print("输入无效，请输入一个整数。")

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
#     with open("bmi_records.txt", "a") as file:
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