#coding=utf8

from russian_names import RussianNames
import recognition
import time

def check_name(text):
    #генератором созадаем базу имен
    rn = RussianNames(count=999, patronymic=False, name=True)
    batch = rn.get_batch()
    #print(batch)
    name_2 = []

    for i in batch:
        name_2.append(i)

    name_2 = ' '.join(name_2)
    name_2 =name_2.lower()
    name_2 = name_2.split()
    text = text.lower()
    text = text.split()


    # проверяем на наличие совпадений. Необходимо для выделения имнеи дальнейшей работы с ним.
    lst_name = list(set(name_2) & set(text))

    lst_name = ''.join(lst_name[0:len(lst_name)])

    name = 'ваше имя'+ ' ' + ',' + lst_name  + "верно?"

    engin=recognition.init_engine()
    #recognition.recognition_un()
    recognition.sound(engin, name)
    #time.sleep(2)
    ansver = recognition.recognition_un()
    ansver = ansver.split()
    print(ansver)
    validation_approval = ['да', 'именно', 'верно', 'корректно', 'истина', "верное", "утверждение", "конечно"]
    if list(set(validation_approval)& set(ansver)) != []:
        user_name = lst_name
        print(user_name)
        # возвращаем имея пользователя
        return user_name



#check_name('меня зовут Михаил')



