from datetime  import datetime
today = datetime.now()

while True:
    try:
        user_date = input('Введите дату дедлайна  в формате "день-месяц-год" , например 19-01-2025: ')
        deadline_date = datetime.strptime(user_date, '%d-%m-%Y')

        time_difference = deadline_date - today
        days_difference = time_difference.days
        if days_difference < 0:
            print('Внимвние! Дедлай истёк', abs(days_difference), 'дней назад.')
        elif days_difference == 0 :
            print('Дедлайн сегодня.')
        else:
            print('До дедлайна осталось' , days_difference,'дней.')
        break

    except ValueError:
        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
        print("Пример: 25-12-2024")
































