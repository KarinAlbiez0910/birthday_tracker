##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random

my_email = 'myalbiez@gmail.com'
my_password = 'KarineProg1'
recipient = 'kalbiez@yahoo.com'

with open('birthdays.csv') as birthdays:
    birthday_list = birthdays.readlines()
    birthday_list = [item.strip().split(',') for item in birthday_list]
    birthday_list.pop(0)
    print(birthday_list)

    today= dt.datetime.now()


    available_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    chosen_letter = random.choice(available_letters)


    for item in birthday_list:
        if int(item[4]) == today.day and int(item[3]) == today.month:
            with open(f'letter_templates/{chosen_letter}') as birthday_letter:
                my_letter = birthday_letter.read()
                letter_with_name = my_letter.replace('[NAME]', item[0])
            with smtplib.SMTP(host='smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(password=my_password, user=my_email)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=item[1],
                                    msg=f'Subject: Happy Birthday\n\n{letter_with_name}')







