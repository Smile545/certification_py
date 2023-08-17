import csv
import datetime as dt
import os




def switch(i):
    if i == 1:
        read_csv()
    if i == 2:
        add_csv()
    if i == 3:
        edit_csv()
    if i == 4:
        delet_csv()
    if i == 5:
        conclusion()


def read_csv():
    with open("note.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(f'Id - {row[0]} Название заметки -  {row[1]} Заметка - {row[2]} Дата создания заметки - {row[3]} Дата изменения - {row[4]}')
            count += 1
        print(f'Всего в файле {count} строк.')



def add_csv():
    name = input("Введите название записи: ")
    telo = input("Напишите заметку: ")
    date_create = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date_change = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c=0
    field={}
    with open('note.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            field[c]=row
            c=c+1
    row=len (field[0])
    column=len(field)
    Id = column + 1
    with open("note.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow([Id, name, telo, date_create, date_change])
        
    
    
    
    


def edit_csv():
    with open("note.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(f'Id - {row[0]} Название заметки {row[1]}')
            count += 1
    s =int(input('Введите Id, какой заметки Вы хотите редактировать '))
    r = csv.reader(open("note.csv"))
    lines = list(r)
    x = input('''Введите соответсвующее число, чтобы изменить необходимую информацию
              1 - Для изменения названия
              2 - Для изменения тела записи
              : ''')
    h = input("Напишите на что меняем:  ")
    date_change = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines[s-1][int(x)] = h
    lines[s-1][4] = date_change
    writer = csv.writer(open('note.csv', 'w', newline=''))
    writer.writerows(lines) 


def delet_csv():
    with open("note.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(f'Id - {row[0]} Название заметки {row[1]}')
            count += 1
    s = input('Введите Id, какой заметки Вы хотите редактировать:  ')      
    inpu = open('note.csv', 'r')
    output = open('notes.csv', 'w', newline='')
    writer = csv.writer(output)
    for row in csv.reader(inpu):
        if row[0] != s:
            writer.writerow(row)
    output.close()
    inpu.close()
    os.remove("note.csv") 
    file_oldname = os.path.join("notes.csv")
    file_newname_newfile = os.path.join( "note.csv")
    os.rename(file_oldname, file_newname_newfile)
    
def conclusion():
    with open("note.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                print(f'Id - {row[0]} Название заметки {row[1]}')
            count += 1
    s =int(input('Введите Id, какой заметки Вы хотите вывести:  '))
    r = csv.reader(open("note.csv"))
    lines = list(r)
    print(lines[s-1])
  


stop = 0

while stop != 1:
    i = int(input('''Добрый день, для выполнений действий введите необходимую цифру:
          1 - Прочесть файл
          2 - Сделать запись в файл 
          3 - Редактировать запись  
          4 - Удалить запись
          5 - Вывести конкретную запись
          0 - Выйти из программы   
          :'''))
    if i == 0:
        break   
    switch(i)

