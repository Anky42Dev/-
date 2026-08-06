# Задача 1
# Напиши функцию bmi(weight, height, name="Player"), которая считает индекс массы тела 
# по формуле weight / height ** 2 (height в метрах). Добавь условия:
# если height <= 0 — верни "Player: invalid height";
# если результат меньше 18.5 — добавь к строке ", underweight";
# если от 18.5 до 25 — добавь ", normal";
# если больше 25 — добавь ", overweight".
# Итоговый формат: "Player: BMI = 22.5, normal".
def find_bmi(weight,height, name = 'Player'):
    if height <=0:
            return f'{name}: invalid height'
    
    bmi =  weight / height ** 2
    
    if bmi < 18.5:
        return f'{name}: BMI:{bmi:.1f}, underweight'
    elif 18.5 <= bmi < 25:
        return f'{name}: BMI:{bmi:.1f}, normal'
    elif bmi>25:
        return f'{name}: BMI:{bmi:.1f},overweight'
    
print(find_bmi(70, 1.75))
print(find_bmi(45, 1.70, "Kira"))
print(find_bmi(90, 1.70, "Oleg"))
print(find_bmi(70, 0, "Sonya"))