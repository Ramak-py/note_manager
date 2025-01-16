title_list = []
title1 = 'q'
while title1 != '':
  title = input('Введите заголовок или оставте пустым для завершения:')
  if title != '':
      title_list.append(title)
  else:
      break
title1 = title
print(title_list)









