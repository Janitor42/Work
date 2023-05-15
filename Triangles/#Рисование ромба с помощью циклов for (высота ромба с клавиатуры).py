#Рисование ромба с помощью циклов for (высота ромба с клавиатуры)

 #int(input())
a=int(input("Введите высоту ромба"))
height=a//2
indent=height+1
x=""

for i in range(1,(height+1)+a%2,1):
    x=x+str("#")
    print(" "*(indent-i)+x+"#"*i)

for i in range(1,height+1,1):
    print(" "*i+"#"*(indent-i)+"#"*(indent-i))
