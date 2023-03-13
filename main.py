# n=int(input("First cifra"))
# n2=int(input("Second cigra"))

# op= int (input("1.+"  "2.-"  "3.*"  "4./"))
# if op==1:
#     rez= (n+n2)
#     print(f' {n} + {n2}= {rez}') 

# elif op==2:
#     rez=(n-n2)
#     print(f'{n} - {n2}= {rez}')

# elif op==3:
#     rez=(n*n2)
#     print(f'{n} * {n2}={rez}')

# elif op==4:
#     if n2==0:
#         print("Incorrect")
#     else:
#         rez=(n/n2)
#         print(f'{n} / {n2}={rez}')
 
# else:
#     print("Not found")


# problem1
# num1 = 2**3
# num2 =3**2
# if num1>num2:
#     print("num1>num2")

# elif num1<num2:
#     print("num1<num2")
    

# problem2
# num=int(input("Vvedite cifru"))

# if 0<num<=22:
#     print("Correct")

# elif 57<=num<=100:
#     print("Correct!")
# else:
#     print("Not correct")


# problem3-1
# num=int(input("Vvedite cifru"))
# if num%2==0:
#     print("Cifra chetnaya")


# problem3-2
# num=int(input("Vvedite cifru"))
# if num%3==0:
#     print("OK ")

# problem3-3
# num=int(input("Vvedite cifru "))
# rez=num**2
# if rez>1000:
#     print(f'{num} ** 2 = {rez} more than 1000')

# else:
#     print(f'{rez} less than 1000')


# problem4:
# if True:
#     print("True")

# problem5
# a=10//5 
# b=10/5

# if a==b:
#     print(a+b) 

# elif a!=b:
#     print("Not equals")


# problem6
# num=int(input("Num"))
# if num>0:
#     print(0-num)
# elif num<0:
#     print(num)


#  problem7
# a=10
# b=5
# if(a>0 and b>0):
#     print("More")
# else:
#     print("Not")


# #problem8
# num=int(input("Введите первую цифру"))
# num1=int(input("Введите вторую цифру"))

# if num>num1:
#     print(num+2)
# elif num<num1:
#     print(num1-2)
# else:
#     print("Not")

# problem9
# num=int(input("Введите число"))

# if num>0:
#     print("Положительное")

# else:
#     print("Отрицательное")

# problem 10
# num=int(input("Введите возраст"))
# if num>=18:
#     print("Совершенолетний")
# elif num<=4:
#     print("Ребенок")
# else:
#     print("Несовершеннолетий")
    
# problem11
# num =45
# num1=6
# if num%num1==0:
#     print("Делится")
# else:
#     print("Не делится")

# problem 12
# yr=int(input("Введите год"))

# y=2023 

# if yr==2023:
#     print("Текущий год")
# elif(yr<y):
#     print("Год прошел")
# else:
#     print("Год не наступил")

# problem 13
# a=int(input("Введите числа"))
# b=int(input())
# c=int(input())

# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# elif c>a and c>b:
#     print(c)

# problem14
# if a<b and a<c:
#     print(a)
# elif b<a and b<c:
#     print(b)
# elif c<a and c<b:
#     print(c)
 
# problem15
# num1 =17391
# num2= 546
# num3= 934 

# if 17391%17>546%17 and 17391%17>934%17:
#     print(num1)
# elif 546%17>17391%17 and 546%17>934%17:
#     print(num2)
# elif 934%17>17391%17 and 934%17>546%17:
#     print(num3)

# калькулятор

# n=int(input("Введите первое число"))
# n1=int(input("Введите второе число"))

# op=int(input("1.+  2.-  3.*  4./"))
# if op==1:
#     rez=n+n1
#     print(f'{n}+{n1}={rez}')

# elif op==2:
#     rez=n-n1
#     print(f'{n}-{n1}={rez}')

# elif op==3:
#     rez=n*n1
#     print(f'{n}*{n1}={rez}')

# elif op==4:
#     if n1==0:
#         print("Incorrect")
# else: 
#     rez=n/n1
#     print(f'{n}/{n1}={rez}')



  
# name=input("введи имя")
# print(name.lower()) #В нижний регистр
# print(name.title()) #все начальные буквы в верхнем регистре
# print(name.upper()) #все буквы в верхнем регистре
# print(name.swapcase()) #меняет
# print(name.capitalize())

# command=input("Write helo")
# if command.lower=="hello":
#     print("True")
# else:
#     print("false")

# name=input("Введи имя ")
# print(name.isdigit()) все ли состоит из цифр

# name=input("Введи имя")
# print(name.isalpha()) все ли состоит из букв


# name=input("Введи имя")
# print(name.isidentifier()) все ли пишется слитно

# print(len.name)


# name=input("Write name: ")
# if name.isalpha:
#     if len(name)>4:
#         if name.istitle():
#             print("True name")
#         else:
#             print("Имя должно начинаться с верхнего регистра")
#     else:
#         print("Имя должно быть больше 5")
# else:
#     print("Имя долэно быть в буквах")
        

# text="Bratan"
# print(text.lstrip("B")) удаляет с правой или левой стороны




# text="Hello World"
# l=text.ljust(15,"*")
# r=text.rjust(15,"#")
# print(l+r)

# text="Hello world"
# r=text.rjust(15,"#")
# print(r.ljust(30, "*"))

# text="Hello world"
# print(f'{text} {text}' )

# print('{0},{1}'.format(False,"Hello world"))

# a="Hello  \n world"  #перевод в след строку
# print(a)

# text="Hello world"
# print(text.replace("o","Xtr"))

# text="Hello world"
# print(text.find("l"))
# print(text.index("l",5))

# print(text.count('o',5))

# print(text.split(','))


# text="Hello world"
# print(text.startswith('H'))

# text="hello world"
# print(text.endswith('d'))


# text="Hello world"
# print(text[1:12])

# print('|*|'.join.text)

# password=input("Введите пароль")
# password2=input("Введите заново")
# if password==password2:
#     if len(password)>=7:
#         if password.find("123"):
#             print("Простой пароль")
#         else:
#             print("Хороший пароль")
#     else:
#         print("Короткий пароль")
# else:
#     print("Пароль  не совпадают вход  не выполнен")




# LIST AND TUPLE

# l=[]
# t=()

# изменяемые
#   списки(list)
#   множества(set)
#   словари

#   неизменяемые
#     числа(int,float)
#     строки(str)
#     кортежи(tuple)


# #Lists
# lists=[1,2,3,4,5,6,7,8,9,"MMM",(),[],True,] 
# print(lists.index(6))

# list=[1,2,3,4,45,6,7,99,98,12,5,6,7,8,9,0,9,]
# print(list.count(3))

# a=[1,1,2,3,4,5,6,7,8,9,10,24,25]
# l=[1,2,3]
# a.sort()
# print(a)

# a=[1,1,2,3,4,5,6,7,8,9,10,24,25]
# l=[1,2,3]
# a.reverse()
# print(a)
# print(l[0])


# a=[]
# print(a)
# a.append(1)
# print(a)


# list_login=["Zhako"]
# list_password=['100055']


# login=input("Enter login")
# password=input("Enter password")

# if login in list_login:
#     if password in list_password:
#         a=['secret']
#         a.append(list_login)
#         print(a)
#     else:
#         print("Wrong password")
# else:
#     print("Wrong login")


# list_login = ['zhako']
# list_password = ['2005']

# input_login = input('Enter login: ')
# input_password = input('Enter password: ')

# if input_login in list_login:
#     if input_password in list_password:
#         secret_user = ['secret']

#         secret_user.append(input_login) # Добавляет элемент в конец списка
#         print(secret_user)
#     else:
#         print('Не правильный пароль')
# else:
#     print('такого пользователя нету')



# list1=[1,2,3,4,5,6,7,8]
# list1.insert(3,'hello')
# print(list1)


# list1=[1,2,3,4,5,6,7,8,9]
# list1.remove(1)
# print(list1)

# list1=[1,2,3,4,5,6,7,8,9]
# list1.pop(1)
# print(list1)


# list1=[1,2,3,4,5,6,7,8]
# list1.clear()
# print(list1)


# list1=['png','jpg','jpeg','gif','svg',]
# fname=input("Enter file name: ").split('.')[-1]
# if len(fname)>=2:
#     if fname.lower() in list1:
#         print('Расширение файла доступно')
#     else:
#         print("Расширение файла недоступно")
# else: 
#     print("Должно быть больше 2 символов")


# list1=(1,2,3,4,6,7,)
# print(list1.index(1))
# print(list1.index(2))
# print(list1.index(3))

# SET={1,2,3,1}
# LIST=[1,2,3,4,4,5,5,5,6,7,7,7]
# print(list)
# g=set(LIST)
# print(list(g))

# a={1,2,3,4,5,6,7,8,9}
# b={1,2,3,4,5}
# #print(a<=b)
# print(a.issubset(b))

# #print(a>=b)
# print(a.issuperset(b))


# print(a.isdisjoint(b)) #пересекаются

# print(a.union(b))

# print(a.intersection(b)) #пересекаются

# print(a.difference(b)) #разница

# print(a.symmetric_difference(b))

# a.update(b)
# print(a)

# a.difference_update(b)
# print(a)


# a.add('world')
# print(a)

# a.remove('world')
# print(a)

# a.discard(5)
# print(a)

# -------------------------------------------------------------------------




# a={1,2,3,4,5}
# b=a
# b.add(40)
# print(a)
# print(b)


# a={1,2,3,4,5}
# b=a.copy()

# b.add(40)
# print(a)
# print(b)

# -------------------------DICT--------------------------



# users={
#     'name': 'John',
#     'age':'18',
#     1:22,
# }


# [
#     {
#                 'name': 'John',
#                 'age':'18',
#     }
# ]

# print(users.get('name'))

# print(users.items())
# print(users.values())
# print(users.keys())


# users={
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4,
#     'e':5,
# }
# print(users.pop('a'))
# users.clear()
# print(users)
# print(users.popitem)


# menu={
#     'beshbarmak':130,
#     'lagman':120,
#     'borsh':110,
# }

    


# menu.update(lagman='150')
# print(menu)
# menu.pop('borsh')
# print(menu)
# menu["drinks"]='cola','sprite','fanta'
# print(menu)



# set_methods={'add','clear','copy','difference','discard','intersection','isdisjoint'}
# dictionary_methods= {'add','copy','intersection','discard','values','updates','popitem'}
# common_methods=set_methods.intersection(dictionary_methods)
# print(common_methods)


# users={}
# l=input()
# p=input()
# p2=input()
# if p==p2:
#     users[l]=p2
#     print(users)
# else:
#     print('Пароли не совпадают')


# job={
#     'Arman':'electric',
#     'Olzhas':'voditel',
#     'Baizhan':'operator',
#     'Zhako':'oper',
#     'Miras':'prokuror',

# }
# print(f'hello {job["Arman"]}')

# sum=int(input("Введите числа "))
# s = {2,}
# s.add(sum)
# print(s)

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia','Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries.remove('Suriname')
# print(south_american_countries)
#-------------------------------------------------------------------------------------------------




# print()
# input()
# len()
# range(start,stop,step)

# start=1
# stop=10
# for  i in range(start,stop):
#     print(i)



# start=1
# stop=10
# step=2
# for  i in range(start,stop,step):
#     print(i)

# a=0
# for i in range(30):
#     a+=1
#     print(i)
#     print(a)

# lists=[1,23,4,55,66]
# print(min(lists))
# print(max(lists))
# print(sum(lists))
# print(sorted(lists))



#FILTER

# n=[1,2,3,4,5,6,7,8,9,33,45,66]
# def even(n):
#     return n%2==0
# a=list(filter(even,n))
# print(a)

# n=[2,3,4,6,8,10]
# r=all( i%2==0 for i in n)
# print(r)


# n=[2,4,6,8,10]
# r=all( i%2==0 for i in n)
# print(r)

# n=[2,4,6,8,10]
# r=any(i%2==0 for i in n)
# print(r)

# n=list( i for i in range(100) if i%2==0)
# print(n)

# name={
#     'Zhalgas':'Suetolotg'
# }
# for k,v  in name.items():
#     print(print(f'ПРивет {k}, Отличная професия {v}'))


# v=0
# a = ['Жексен', 'Dias', 'Marselle']
# for i in a:
#     print(i)

#     for j in i:
#         print(j)

#         if j == 'е' or j == 'e':
#             v += 1
#             # break
# print(v)


#111

# num=int(input("Введите число"))
# start=1
# stop=101
# for i in range(start,stop):
#     print(i)


#222
# num=int(input("Введите число"))
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)

#333

# num=int(input("Введите число"))
# for i in range(1,num+1):
#     print(i)


#444
# 

#555

# name=input("Введите слово ")
# print(len(name))

#666
word=input("Введите слово")
print(word[:1])





