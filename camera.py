#coding=utf8
import cv2
# работа с вебкой , изображение в реальном времени
def VideoCap():
    cap =cv2.VideoCapture(0)
    # зададим ширину кадра в видеопотоке
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
    #  зададим ывысоту кадров видеопотоке
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1480)
    #
    while True:
        ret, img = cap.read()
        #  преобразуем кадр в градацию серовго
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #этой настройкой можно мнять градацию цвета
        #cv2.imshow("camera", gray)
        cv2.imshow("camera", img)
        if cv2.waitKey(10) == 27:
           break
    cap.release()
    cv2.destroyAllWindows()
    global answer
    answer = 'камера включена'
    return True


"""
#  работа с вебкой в записи изображения ввиде ведеофайла
cap =cv2.VideoCapture(0)
#  укажем кодек для сокрадения и сжатия видео
#codec = cv2.VideoWriter_fourcc(*"XVID") # кодек для создания виде в формате AVI
codec = cv2.VideoWriter_fourcc(*"X264") # кодек для создания виде в формате MP4
# создадим переменную с настройками для создания видеофайла
# первый вхоной параметр имя будущего файла с расширением ; вторлй параметр - перемення с на тастройками кодека ; третья преременная - количество кадров в секунду ; четвертый парамер - кортеж с размерами изображений
#out = cv2.VideoWriter("sinima\Proba.avi", codec, 25.0, (640, 480))
out = cv2.VideoWriter("sinima\Proba.mp4", codec, 25.0, (640, 480))
while cap.isOpened():
    ret, img = cap.read()
    #if cv2.waitKey(1) & 0xFF == or ('q') or ret == False:
    if cv2.waitKey(1) == 27 or ret == False:
        break
    cv2.imshow("camera", img)
    # кадр записываем в файл
    out.write(img)
# звакрываем файл с выходным видео (именно в этот момент создастся файл на жестком диске)
out.release()
cap.release()
cv2.destroyAllWindows()
"""

