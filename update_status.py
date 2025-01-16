status = {'1':'Выполнено','2':'В процессе','3':'Отложено'}
status_now = '0'
print('Возможные статусы заметкок 1-Выполнено 2-В процессе 3-Отложено')
while True:
   status_now = str(input('Введите статус заметки "цифрой"'))
   if status_now == '1':
       print(status[status_now])
       break
   elif status_now == '2':
       print(status[status_now])
       break
   elif status_now == '3':
       print(status[status_now])
       break
   else:
        print('Некоректный ввод')








