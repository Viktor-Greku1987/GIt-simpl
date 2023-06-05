from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.Qt import QUrl
from PyQt5 import QtWidgets # все графи ческие элементы
from radioUI import Ui_MainWindow # полтянули весь дизайн
import sys
class radio(QtWidgets.QMainWindow): # родитель нашенгго класса шаблон окна (чтобы подтянулось готовое окошко)
    def __init__(self, name_radio):
        super(radio, self).__init__() # вызов самого серовго окошка (стандартное окно)
        self.UI = Ui_MainWindow() # созадали обект нашего класса
        self.UI.setupUi(self)

        self.pleer = QMediaPlayer(self)  # содание обекта плеера
        # словарь хронящий ключ-назване радиоволны, значение- адрес (https....) онлайн воспроизведения
        self.radio_volna = dict()
        self.create_radio_wave()
        current_wave = self.radio_volna.get(name_radio)
        if current_wave != None:
            # вызываем ф-цию воспроизвдения выбранного радио
            self.radio_play(current_wave)
        else:
            exit()
    # функция остановки радио
    def radio_stop(self):
        self.pleer.stop()
    # ф-ция восрпоизвдения радио
    def radio_play(self, current_wave):



        # задаем плееру что воспроизвести
        self.pleer.setMedia(QMediaContent(QUrl(current_wave)))
        # задать громкость плеера от 0 до 100
        self.pleer.setVolume(50)
        self.pleer.play() # запуск воспроизведения (pause() - пауза), stop() - остнавить воспроизведение

    # функция создвания словая радиволн
    def create_radio_wave(self):
        #self.radio_volna['европа плюс']="http://europaplus.hostingradio.ru:8014/ep-top256.mp3"
        with open('radio.txt', 'r') as file:
            while True:
                line = file.readline()
                if line == '':
                    break
                if line[-1] == '\n':
                    line = line[0:len(line)-1]
                key_radio, URL_radio = line.split('; ')
                self.radio_volna[key_radio] = URL_radio


#app = QtWidgets.QApplication([])
#app1 = radio("европа плюс") # создаем объект класса. Вызов метода init  что выполянет созадние объекта класса.
#app1.show()
#sys.exit(app.exec())
