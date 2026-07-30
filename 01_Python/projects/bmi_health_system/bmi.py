def calculate_bmi(weight,height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "偏瘦"
    elif 18.5 <= bmi < 24.9:
        return "正常"
    elif 25 <= bmi < 29.9:
        return "偏胖"
    else:
        return "肥胖"