Capitals = dict(Россия= 'Москва', Украина= 'Киев', Америка= 'Вашингтон')
print(Capitals)

#поиск элемента (получение значения элемента по ключу)
print(Capitals["Россия"])

#Добавление нового элемента в словарь
Capitals["Германия"]="Берлин"
print(Capitals)

#Удаление по ключу ( с проверкой что такое существует)
if "Америка" in Capitals:
    del Capitals["Америка"]
print(Capitals)

#Идем по всем элементам словоря items()
for key,value in Capitals.items():
    print("ключ: ", key,"\n" "Значение: ", value)

#Домашнее задание:
list1=[1,2,3,4,5]
list2=["a",'b','c','d','f']

print(list1)
print(list2)
print(len(list1))
print(len(list2))

dict={}
for i in range(len(list1)):
    dict[list1[i]]=list2[i]
print(dict)