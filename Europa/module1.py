import random 

Riigids = {}
file=open("riigid.txt","r")
for line in file:
    k,v=line.strip().split("-")
    Riigids[k.strip()] = v.strip()

   
def main():
  global Riigids
  print("Добро пожаловать в Карту Европейских стран и столиц!")
  print()
  print(" 1 - Найти страну/столицу  \n 2 - Добавить новую страну \n 3 - Исправить ошибку  \n 4 - Проверка знаний.")
  valik=int(input("-> "))
  if valik not in [1,2,3,4]:
     print("ВЫбери от 1 до 4!")
  else:
    if valik==1:
      naiti(Riigids)
    if valik==2:
      dobavit()
    if valik==3:
        oshibka()
    if valik==4:
        test()

def naiti(r:dict):
  global Riigids
  print("Напиши Страну/Город")
  slovo=input("->")
  print(Riigids.get(slovo), "<-")


def dobavit():
 b=""
 c=""
 global Riigids
 print("Страна:  ")
 strana =str(input("-> "))
 print("Город:")
 stolitsa = str(input("-> "))
 b += str(strana) + "-" + str(stolitsa)
 c += str(stolitsa) + "-" + str(strana)
 file=open("riigid.txt","a")
 file.write(b+"\n")
 file.write(c+"\n")
 print("Сохранено!")


def oshibka():
    b=""
    c=""
    print("Страна:")
    a=str(input("-> "))
    print("Город:")
    b=str(input("-> "))
    if a not in Riigids and b not in Riigids:
        print("Такой страны или города нект в списке!")
    else:
        print("Страна:")
        strana=str(input("-> "))
        print("Город:")
        stolitsal=str(input("-> "))
        b += str(strana) + "-" + str(stolitsa)
        c += str(stolitsa) + "-" + str(strana)
        file=open("riigid.txt","a")
        file.write(b+"\n")
        file.write(c+"\n")

def test():
    p = 0
    l=[]
    for el in Riigids.keys():
        l.append(el)
    for i in range(12):
        r_el = random.sample(l,1)[0]
        print(r_el)
        t_write = input("-> ")
        i += 1
        if t_write == Riigids[r_el]:
            print("Правильно :)")
            p = p+1
        else:
            print("Неправильно ;( ")
    print("Хочешь узнать свои результаты?")
    print("1 - Да \n 2 - Нет")
    a=int(input("-> "))
    if a not in [1,2]:
        print("Напиши цифру от 1 до 2!!!")
    else:
        if a==1:
            pr=((p/12)*100)
            print("У тебя",pr,"Процентов")
        else:
            print("Ну ладно :((")
