import random

day=0
answer=0
correct_answer=0
false_answer=0

lis_day_en=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
list_day_ry=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

choise = random.randint(0, len(list_day_ry) - 1)
while correct_answer<20:
    print(list_day_ry[choise], " это - ")
    answer = input()
    if answer==lis_day_en[choise]:
        print("You are Correct ")
        choise = random.randint(0, len(list_day_ry) - 1)
        correct_answer+=1
    else:
        print("Not correct, trye agan")
        false_answer+= 1
print("Колличество ошибок = ",false_answer)

