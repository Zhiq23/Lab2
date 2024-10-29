def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return -1
    elif 18.5 <= bmi <= 25.0:
        return 0
    else:
        return 1

bmi=calculate_bmi(weight=57, height=1.73)
classification = classify_bmi(bmi)

print(f"Calculated BMI = {bmi:.2f}")
print(f"Classification = {classification}")
