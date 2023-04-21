#coding=utf8
def record_video():
    import cv2
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
    return True