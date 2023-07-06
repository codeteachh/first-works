
"""
Created on Tue Mar  7 08:17:51 2023

PYTHON DARSLARI

@author: user
"""

#1    DEF OPERATOR
def maker_age(ism,yosh):
    """Foydalanuvchi tug'ilgan yilini hisoblovchi dastur"""
    print(f"{ism.title()} {2023-yosh}-yilda tug'ilgan.")
    
maker_age('sevdiyor',24)
maker_age('sherzod',25)
maker_age('Bobur',20)
maker_age('ayubxon',21)
maker_age('Marjona',16)  
#2
def numbers(son):
    """Istalganni sonni kvadrati va kubini hisoblovchi dastur"""
    print(f"{son} ning kvadrati {son**2} ga teng,kubi esa {son**3} ga teng")
    
numbers(3) 
numbers(-9)   
#3
def sonlar(son):
    """Sonning juft yoki toqligini aniqlovchi dastur"""
    if son%2:
        print("Bu son toq son!")
    else:
        print('Bu son juft son!')
        
sonlar(222888)        

#4
def data(son,son_1):
    """Bu dastur sonni katta kichikligini aniqlaydi"""
    if son<son_1:
        print(f"{son} soni kichkina {son_1} dan.")
    elif son==son_1:
        print(f"{son} soni {son_1} soniga teng!")
    elif son>son_1:
        print(f"{son_1} soni kichkina {son} sonidan.")
    else:
        print('Iltimos ikkita istalgan son kiriting!')
        
data(-6,6) 
 
#5
def user_number(x,y):
    """Foydalanuvchi kiritgan sonni (x**y) kvadratini xisoblovchi dastur"""
    print(f"{x**y}")
    
user_number(3,4)    

#6

def user_number(x,y=2):
    """Foydalanuvchi kiritgan sonni (x**y) kvadratini xisoblovchi dastur"""
    print(f"{x**y}")
    
user_number(3)    

#7
def recruiter(x):
    """Kiritilgan sonni 2 dan 10 gacha qoldiqsiz bo'linishini tekshirish"""
    for n in range(2,11):
     if not x%n:
            print(f"{x} {n} ga qoldiqsiz bo'linadi.")
            
recruiter(87)
#LESSONS
def full_name(ism,familiya):
     """To'liq ism qaytaruvchi funksiya"""
     full_n=f"{ism} {familiya}"
     return full_n

talaba=full_name("sevdiyor","ergashev")
talaba_1=full_name("sherzod","anvarov")
print(f"Darsga kelmagan talabalar:{talaba} va {talaba_1}")
print(f"{talaba} darsga kechikib keldi.")

def full_name(ism,familiya,otasining_ismi=' '):
     """To'liq ism qaytaruvchi funksiya"""
     if otasining_ismi:
           full_name=f"{ism} {otasining_ismi} {familiya}"
     else:
        full_name=f"{ism} {familiya}"
     return full_name.title()
 
talaba=full_name("sevdiyor","ergashev","zafarjonivich")
talaba_1=full_name("sherzod","anvarov")
print(f"Darsga kelmagan talabalar:{talaba} va {talaba_1}")
print(f"{talaba} darsga kechikib keldi.")
    

def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'korobka':korobka,
          'yil':yili,
          'narh':narhi}
    return avto

avto_1=avto_info('GM','Malibu','qora','avtomat',2018)
avto_2=avto_info('GM','Gentra','Oq','Mehanika',2016,15000)
avtolar=[avto_1,avto_2]
print("Onlayn bozordagi mavjud mashinalar.")
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']   
    else:
       narh='Noma\'lum'
    print(f"{avto['rang']} {avto['model']},Narhi:{narh}")
    
 def oraliq(min,max):
     sonlar=[]
     while  min<max:
         sonlar.append(min)
         min+=1
     return sonlar
     
 print(oraliq(0,12))
 print(oraliq(10,21))    
#####
def oraliq(min,max,qadam=''):
    sonlar=[]
    while  min<max:
        sonlar.append(min)
        min+=1
    return sonlar
    
print(oraliq(0,12,2))
print(oraliq(10,21))   
#3##
def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rangi,
          'korobka':korobka,
          'yil':yili,
          'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
avtolar=[]
while True:
    print("\n Quyidagi ma'lumotlarni kiriting",end=' ')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli:") 
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yil=input("Ishlab chiqarilgan yili: ")
    narh=input("Narhi: ")
   
    avtolar.append(avto_info(kompaniya,model,rangi,korobka,yil,narh ))
    javob=input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
      break
print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh="Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()},{korobka} korobka,Narhi:{narh}")
       
###111homework
def users(ism,familiya,tugilgan_yil,joy,email=" ",tel_number=None):
  """Mijoz haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi dastur"""
  user={'ism':ism,
          'familiya':familiya,
          'tugilgan_yil':tugilgan_yil,
          'joy':joy,
          'email':email,
          'tel_number':tel_number}
  return user
print("\nSo'ralgan ma'lumotlarni kiriting:")
userlar=[]
while True:
    print("Assalomu aleykum!")
    ism=input('Ismingiz nima?')
    familiya=input("Familiyangizni ham kiriting:")
    tugilgan_yil=input("Tug'ilgan yilingizni ayting.")
    joy=input("Qayerda tug'ilgansiz?")
    email=input("emailingizni kiriting:")
    tel_number=input("Telefon nomeringizni yozing")
    userlar.append(users(ism,familiya,tugilgan_yil,joy,email,tel_number))
    javob=input("Yana ma'lumot qo'shasizmi?(yes/no)")
    if javob=='no':
        break
    print(userlar)
else:
     for user in userlar:
      print(  
         f"Siz {ism.title()} {familiya.title()}, {tugilgan_yil}-yilda {joy}da tug'ilgansiz va sizning telefon raqamingiz\
           {tel_number},{email}")      
         
#amaliyot
def katta_harf(ismlar):
    royhatlar=[]
    while ismlar:
        ism=ismlar.pop()
        royhatlar.append(ism.title())
    return royhatlar

talabalar=['ali','vali','salim','hasan','eldor','aziz','sevdiyor']
royhatlar=katta_harf(talabalar[:])
print(royhatlar)
print(talabalar)    

#AMALIYOT
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting\n<<<>>>")
        baholar[ism]=baho
    return baholar
talabalar=['ali','vali','salim','hasan','eldor','aziz','sevdiyor']
baholar=bahola(talabalar)
print(baholar)
#lesson
######  *ARGS (arguments) VA **KWARGS(keywords)
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi=0
    for son in sonlar:
        yigindi += son
    return yigindi    
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7,8))
print(summa(45,100,23,45,60,10))
#222
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7,8))
print(summa(45,100,23,45,60))
#333
def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7,8))
print(summa(45,100,23,45,60))
print(summa(4))

######  *ARGS (arguments) VA **KWARGS(keywords)
def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1=avto_info("GM","Malibu",rang='qora',yil=2020)
avto2=avto_info("kia","K5",rang='qizil',narh=35000,yil=2022)
    
##HOMEWORK
def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(multiply(4,5,6))

def summa(*sonlar):
   """Kiritilgan sonlarni ko'paytmasini qaytaruvchi dastur"""
   qiymat=1
   for son in sonlar:
      qiymat*=son
   return qiymat
  
print(summa(4,6))        
print(summa(2,3,4,5,6,7,8))

####2-homework
def summa(ism,familiya,**malumotlar):
    """Talaba haqidagi malumot yig'uvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1=summa('sevdiyor','ergashev',kurs='4-kurs',fakultet='neft va gaz')
talaba2=summa('aziz','sultonov',kurs='3-kurs')
        
##Takrorlash
def avto_info(kompaniya,model,rang,korobka,yil,narh=None):
    avto={'kompaniya':kompaniya,
          'model':model,
          'rang':rang,
          'korobka':korobka,
          'yil':yil,
          'narh':narh}
    return avto    

print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting:",end=' ')
    kompaniya=input("Ishlab chiqaruvchi:")
    model=input("Modeli:")
    rang=input("Rangi:")
    korobka=input("Korobka:")
    yil=input("Ishlab chiqarilgan yili: ")
    narh=input("Narhi:")
    avtolar.append(avto_info(kompaniya,model,rang,korobka,yil,narh))
    javob=input("Yana avto mashina qo'shasizmi ? (ha/yo'q):")
    if javob=='yo\'q':
      break

print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh=avto['narh']
    else:
        narh="Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()},{korobka} korobka. Narhi:{narh}")    
        
### remaining lesson


import math
x=400    
print(math.sqrt(x))##sqrt()=sonning ildizini hisoblaydi.
print(math.pow(5,3))##pow-bu power degani yani sonning bir ma'lum bir darajasi.
print(math.pi)
print(math.log2(8))
print(math.log10(100))
##randint
import random as r
son=r.randint(1,50)
print(son)
##choice()
ismlar=['olim','anvar','aziz','bobur']
ism=r.choice(ismlar)
print(ism)

##tanlangan ismni ichidan harf tanlash uchun buu
print(r.choice(ism))
###sonlar
x=list(range(0,51,5))
print(x)
print(r.choice(x))


import random as r
#shuffle()-aralashtirib tashlash degani.
x=list(range(11))
print(x)
r.shuffle(x)
print(x)

##Homework 23-dars Modullar
FUNKSIYA-FUNKSIYA TARIFI.
CEIL(X)-X DAN KATTA YOKI TENG BOLGAN ENG KICHIK BUTUN SONNI QAYTARADI.
FABS(x)-X NING ABSOLYUT QIYMATINI QAYTARADI.
FLOOR(X)-X DAN  KICHIK YOKI TENG BOLGAN ENG YAQIN BUTUN SONNI QAYTARADI.
EXP(X)-X**E NI QAYTARUVCHI FUNKSIYA.
COS(x)-COS(X) NI QAYTARUVCHI FUNKSIYA.
SIN(X)-SIN(X) NI QAYTARUVCHI FUNKSIYA.
TAN(x)-TAN(X) NI QAYTARUVCHI FUNKSIYA.
DEGREES(X)-X BURCHAKNING RADIAN QIYMATINI DARAJAGA KONVERTASIYA QILISH.
RADIANS(X)-X BURCHAKNING DARAJA QIYMATINI RADIANGA KONVERTASIYA QILISH.
E-MATEMATIK KONSTANTA  (2.71828).

ismlar=['aziz','sevdiyor','obid','eldor','siroj']
import random as r
son=r.choice(ismlar)
print(son)
s=r.choice(son)
print(s)
from math import e
print(e)
import math
print(math.log2(8))
print(math.log10(100))


import random as r
son=r.randint(0,100)
print(son)

## 24-dars FUNKSIYALAR SO'NGSO'Z

import math
uzunlik=lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))   
kvadrat=lambda x, y :x**y
print(kvadrat(3,4)) 
def daraja(n):
    return lambda x:x**n
kvadrat=daraja(2)
kub=daraja(3) 
print(f"3-ning kvadrati {kvadrat(3)}ga ,"
      f"kubi esa {kub(3)}.")

from math import sqrt
sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))
print(ildizlar)
def daraja2(x):
    """Berilgan sonni kvadratini hisoblaydigan funksiya"""
    return x*x

print(list(map(daraja2,sonlar)))


### Lambda orqali 
kvadratlar=list(map(lambda x:x*x,sonlar))
print(kvadratlar)

a= [4,5,6]
b=[7,8,9]
a_plus_b=list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

import random as r
sonlar=r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
    return  x%2==0
juft_sonlar=list(filter(juftmi,sonlar))

###  LAMBDA FUNKSIYASI ORQALI
juft_son=list(filter(lambda x:x%2==0,sonlar))
print(juft_son)
              

### STARTSWITH(X) bu me'tod matn x soni bilan boshlanadimi yo'qmi tekshiradi.
mevalar=['olma','anor','nok','anjir',"o'rik",'shaftoli']
harf='a'
mevalar_b=list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevalar_b)
mavalar2=list(filter(lambda meva:len(meva)<=5,mevalar))
print(mavalar2)
## ENDSWITH(X) matnni oxirgo harfi x bn boshlanganini topish uchun.

list(filter(lambda meva:(meva.startswith("a") and meva.endswith('r')),mevalar))
###homework-1
f1=lambda x:x*10
print(f1(10))
f2=lambda x,y:x**y
print(f2(5,4))

###222
from math import sqrt
sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))
print(ildizlar)


def daraja2(x):
    """Berilgan sonni kvadratini qaytaruvchi funksiya """
    return x*x
kvadrat=list(map(daraja2,sonlar))
kvadratlar=list(map(lambda x:x*x,sonlar))

from random import sample
from math import sqrt
x=list(range(0,1001))
y=sample(x,13)
print(y)
ildizlar=list(map(lambda n:sqrt(n),y))
print(ildizlar)
toq_sonlar=list(filter(lambda n:n%2,y))
print(toq_sonlar)

##333-HOMEWORK

###             TUB SONLAR
def tubmi(x):
    if x%2==0 or x<2:
        return False
    if x==2 or x==3:
        return True 
    for i in range(3,x):
        if x%i == 0:
            return False
        return True
    
tub_sonlar=list(filter(tubmi,range(30))) 
print(tub_sonlar)   

### SON TOPUVCHI DASTUR
import random as r
def son_top(x):
   """Son topuvchi dastur"""
   i=1
   y=r.randint(1,x)
   javob=int(input(f"Men 1 dan {x} gacha son o'yladim topishga harakat qiling.\n<<<>>>"))
   while True:
        i+=1
        if javob<y:
          javob=int(input("Men o'ylagan son bu sondan katta.\n<<>>> "))
          
        elif javob>y:
          javob=int(input("Men o'ylagan son bu sondan kichikroq.\n<<<>>>"))
       
        if javob==y:
           break
   print(f"Siz {i} marta urinishda to'g'ri topdingiz.") 
   return i
print(son_top(10))

import random as r
def son_top_c(x):
    """Son topuvchi funksiya"""
    i=1
    input(f"Istalgan 1 dan {x} gacha son o'ylang men topaman.\n<<<>>>")
    quyi=1
    yuqori=x
    while True:
        i+=1
        if quyi != yuqori:
            son=r.randint(quyi,yuqori)
        else:
            son=quyi
        javob=input(f"Siz {son} sonini o'yladingiz:to'g'ri (t),"
                    f"men o'ylagan son bundan kattaroq (+),yoki kichikroq (-)\n<<<>>>".lower())  
        if javob=="-":
            yuqori=son-1
        elif javob=="+":
            quyi=son+1
        else:
            break
    print(f"Men {i} marta taxmin bilan topdim.") 
    return i

print(son_top_c(10))        

def play(x=10):
    yana=True
    while yana:
        i_user=son_top(x)
        i_pc=son_top_c(x)
        if i_user>i_pc:
            print("Men yutdim.")
        elif i_user<i_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana=int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))
        
        
        
        
        

       























