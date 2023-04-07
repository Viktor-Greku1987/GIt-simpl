#coding=utf8
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
microphon = speech_recognition.Microphone()

def recognition_un():
    with microphon:
        data = ''
        # регулировка окружаюещго шума
        recognizer.adjust_for_ambient_noise(microphon, duration=2)
        try:
            # получим данные с миукрофона ввиде аудиопересменной
            print("прошу, произнесите ответ")
            audio = recognizer.listen(microphon, 5, 5)
        except Exception as ex:
            print('Я вас не расслышал. Посторите : ', ex)
            return ''
        # распознание аудио онлайн через гугл
        global name
        name = recognizer.recognize_google(audio, language='ru')
        name.lower()
    return name


def init_engine():
    # созжаем объект для воспроизведения речи
    global engin
    engin = pyttsx3.init('sapi5') # sapi5 - это настройки голосового движка от майкрасовт
    # из движка получаем все голоса
    voices = engin.getProperty('voices')

    #for i in voices:
        #print(i)

    # настраиваем голос на русский женский Татьяна
    engin.setProperty('voice', voices[0].id)
    # настроим громкость воспроизведения
    # volume = engin.getProperty('volume')
    # print(volume)
    engin.setProperty('volume', 0.8)
    # настройка скорости воспроизведения звука
    rate = engin.getProperty('rate')
    #print(rate)
    engin.setProperty('rate', 185)
    #help(engin)
    return engin

def sound(engin, name):
    # вызываем функцию синтеза тектста в речь
    engin.say(name)
    # воспроизводим полученное аудио
    engin.runAndWait()