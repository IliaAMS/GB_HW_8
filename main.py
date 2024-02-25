# День добрый!
# Запарился делать красоту с отступами)))
# Буду честен, кое что, по мелочи, подглядел. До флага сам допёр - проходил в другом месте)
# Есть ощущение, что с удалением контакта можно как-то подругому, без полного переписывания, но не понимаю как.

import os

def serch_pers_name():
  name = input('\nВведите имя: ').lower()
  with open('phone_book.txt', 'r') as file:
    flag = 0
    for line in file:
      if name in line.lower():
        print(line)
        flag += 1
    if not flag:
      print('Такого имени нет в телефонной книге\n')

def serch_pers_sur_name():
  surname = input('\nВведите фамилию: ').lower()
  with open('phone_book.txt', 'r') as file:
    flag = 0
    for line in file:
      if surname in line.lower():
        print(line)
        flag += 1
    if not flag:
        print('Такой фамилии нет в телефонной книге\n')

def serch_pers_number():
  number = input('\nВведите номер телефона: ')
  with open('phone_book.txt', 'r') as file:
    flag = 0
    for line in file:
      if number in line:
        print(line)
        flag += 1
    if not flag:
      print('Такого номера нет в телефонной книге\n')

def serch_coment():
  coment = input('\nВведите комментарий: ').lower()
  with open('phone_book.txt', 'r') as file:
    flag = 0
    for line in file:
      if coment in line.lower():
        print(line)
        flag += 1
    if not flag:
      print('Такого комментария нет в телефонной книге\n')

def add_pers():
  name = input('\nВведите имя: ')
  sur_name = input('Введите фамилию: ')
  number = input('Введите номер телефона: ')
  coment = input('Введите комментарий: ')
  with open('phone_book.txt', 'r') as file:
    for line in file:
      if name.lower() in line.lower() and sur_name.lower() in line.lower() and number in line:
        print('Такой контакт уже есть в телефонной книге\n')
    else:
      with open('phone_book.txt', 'a') as file:
        file.write(f'{name} {sur_name} {number} {coment}\n')
      print('Коантакт успешно добавлен!\n')

def delete_pers():
  pers = input('\nВведите имя, фамилию или номер телефона (через пробел): ').lower()
  with open('phone_book.txt', 'r') as file:
    for line in file:
      if pers in line.lower():
        ans = input('\nВы уверены что хотите удалить этот контакт? (y/n): ')
        if ans == 'y':
          with open('phone_book.txt', 'r') as file:
            lines = file.readlines()
          with open('phone_book.txt', 'w') as file:
            for line in lines:
              if pers not in line.lower():
                file.write(line)
          print('\nКонтакт успешно удален!\n')
          break
        elif ans == 'n':
          print('\nКонтакт не был удален!\n')
          break
        else:
          print('\nВыбранно неверное действие!\n')
          break
    else:
      print('Контакт не найден!\n')

def show_all_pers():
  with open('phone_book.txt', 'r') as file:
    for line in file:
      print(line)

if not os.path.exists('phone_book.txt'):
  with open('phone_book.txt', 'w') as file:
    file.write('\nЭто наша телефонная книга!\nЗдесь будут указанны  Имя, Фамилия, Номер абонентов и Комментарий к ним!\n')
while True:
  print('Выберите действие:\n1 - Поиск по имени\n2 - Поиск по фамилии\n3 - Поиск по номеру телефона\n4 - Поиск по комментарию\n5 - Добавить контакт\n6 - Удалить контакт\n7 - Показать всё содержимое телефонной книги\nq - Выход')
  com = input('=>').lower()
  if com == '1':
    serch_pers_name()
  elif com == '2':
    serch_pers_sur_name()
  elif com == '3':
    serch_pers_number()
  elif com == '4':
    serch_coment()
  elif com == '5':
    add_pers()
  elif com == '6':
    delete_pers()
  elif com == '7':
    show_all_pers()
  elif com == 'q':
    break
  else:
    print('\nВыбранно неверное действие!\n')