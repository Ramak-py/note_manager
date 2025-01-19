all_note = []
while True:
    print('Добро пожаловать в "Менеджер заметок"! Введите данный новой заметки ')
    note = {}
    note['username'] = (input('Введите своё имя: '))
    note['title'] = (input('Введите заголовок заметки: '))
    note['description'] = (input('Введите описание заметки: '))
    note['status '] = (input('Введите сатаус заметки  (новая, в процессе, выполнено): '))
    note['creation_date'] = (input('Введите дату создания заметки в формате "день-месяц-год": '))
    note['deadline'] = (input('Введите дату истечения заметки  в формате "день-месяц-год": '))
    all_note.append(note)
    print(all_note)
    q = input('Хотите сделать ещё одну заметку да/нет: ')
    if q == 'нет':
        break
count = 0
for elements in all_note:
    print(count+1, '.', end='')
    print('Имя:', all_note[count].get('username'))
    print('Заголовок:', all_note[count].get('title'))
    print('Описание:', all_note[count].get('description'))
    print('Статус:', all_note[count].get('status '))
    print('Дата создания:', all_note[count].get('creation_date'))
    print('Дедлайн:', all_note[count].get('deadline'))
    count += 1
