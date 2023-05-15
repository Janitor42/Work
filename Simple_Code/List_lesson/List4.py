#создание базы данных используя массивы
last_name = ["Яковлев","Астахов","Иванов","Эмильен"]
name= ["Як","Александр","Иван"]
second_name=["Яковлевич","Александрович ","Иванович"]
date_of_birth=["19.01.1992", "21.2.2004","01.01.1999" ]
group=["ЭЭГ","СПГ","ААП","пвап"]

#Выравнивание массивов по длине

for i in range(len(last_name)):
   if len(last_name)>len(name):
       name.append("None Name")
   elif len(last_name)>len(second_name):
       second_name.append("None Second Name")
   elif len(last_name)>len(date_of_birth):
       date_of_birth.append("None Date")

student_names=[]


#Присваивание в массив студентов данные других массивов
for i in range (len(last_name)):
  a=last_name[i]+" "+name[i]+" "+second_name[i]+" "+date_of_birth[i]+" "+ group[i]
  student_names.append(a)
  print(student_names[i])