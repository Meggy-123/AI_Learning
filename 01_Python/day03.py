# for循环
# for i in range(5):
#     print(i)
#     #从0到4的整数，依次输出
# for i in range(1, 6):
#     print(i)
#     #从1到5的整数，依次输出

# #循环列表
# scores=[90,85,95,88]
# for score in scores:
#     print(score)

# #计算平均成绩
# scores=[85,90,78,92,88]
# total=0
# for score in scores:
#     total+=score
# print("平均成绩为：",total/len(scores))

# # while循环
# count=0
# while count<5:
#     print(count)
#     count+=1

# #综合练习：AI学习打卡系统
# day=int(input("请输入你学习的天数："))
# for i in range(1,day+1):
#     print("Day",i,"完成学习")

#今日项目：学生成绩分析系统 v1.0
scores=[85,90,78,92,88]
sum=0
score_min=scores[0]
score_max=scores[0]
print("成绩列表")
for score in scores:
    print(score)
    sum+=score
    if score<score_min:
        score_min=score
    if score>score_max:
        score_max=score
print("最低成绩：", score_min)
print("最高成绩：", score_max)
print("平均成绩：", sum/len(scores))