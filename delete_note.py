all_note = [{'username': 'Алексей', 'title': 'Домашнее задание ', 'description': 'сдлеать ДЗ'}, {'username': 'Алина', 'title': 'Покупки', 'description': 'купить продукты домой'}]
count = 0
for elements in all_note:
    print(count+1, '.', end='')
    print('Имя:', all_note[count].get('username'))
    print('Заголовок:', all_note[count].get('title'))
    print('Описание:', all_note[count].get('description'))
    count += 1
e = 0
r = len(all_note)
q = input('Введите имя пользователя или заголовок для удаления заметки: ')
for elements in all_note:
    if q == all_note[e].get('username') or q == all_note[e].get('title'):
        all_note.pop(e)
    e += 1

a = len(all_note)
w = 0
if a != r:
    for elements in all_note:
        print(w+1, '.', end='')
        print('Имя:', all_note[w].get('username'))
        print('Заголовок:', all_note[w].get('title'))
        print('Описание:', all_note[w].get('description'))
        w += 1
else:
    print('Заметок с таким именем пользователя или заголовком не найдено')