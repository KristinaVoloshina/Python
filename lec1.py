from msvcrt import SEM_NOGPFAULTERRORBOX


print ('hello world!')
a=123
b=1.23
print(a)
print(b)
#print(type(a))
#print(type(b))
#value=None
#print(type(value))
s='hello world'
print(s) #вывод строки
print(a,b,s)
print(f'{a}-{b}-{s}')
print('{1}-{0}-{2}'.format(a,b,s))

f=True
print(f)

list=['1','2','hello Kristina',1,7]
print(list)

# print, input
#print('Введите a');
#a=float(input())
#print('Введите b');
#b=float(input())
#print(a,b,a+b)#

a=7
b=1.3
c=round(a*b)
print(c)

a=3
a+=5
print(a)

a='seoul'
b='seoul'
print(a==b)

a=1<3<5
print(a)

f=1<2 or 4<6
print(f)

f=[1,2,3,4]
print(f)
print(7 in f)

f=[1,2,3,4]
is_odd=not f[0]%2
print(is_odd)

#a=int(input('Введите '))
#b=int(input('Введите '))
#if a>b:
 #   print(a)
#else:
 #   print(b)

#username=input('Напиши свое имя ')
#if username=='Ли Чон Сок':
 #   print('Я так тебя люблю!')
#elif username=='Ли Дон Ук':
 #   print('Я тебя долго ждала...')
#elif username=='Хван Ин Еп':
 #   print('Ты-топ!')
#else:
 #   print('Привет, ', username)

original=23
inverted=0
while original!=0:
    inverted=inverted*10+(original%10)
    original//=10
    print (original)
else:
    print('Пожалуй')
    print('хватит')
    print(inverted)

    list=[1,2,3,4,5]
    for i in list:
        print(i**2)

for i in range(1,7,2):
    print(i)




