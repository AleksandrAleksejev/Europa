from module1 import*

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
