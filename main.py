import sys
from PyQt5 import QtWidgets
import requests
import mgrs
from PyQt5.QtWidgets import *
from rakim_hesaplama_ui import *
import rakim_hesaplama

uygulama = QApplication(sys.argv)
pencere = QWidget()
ui = Ui_Form()
ui.setupUi(pencere)
pencere.show()

def hesapla():
    bolge = int(ui.lineEdit_bolge_sayi.text()) if ui.lineEdit_bolge_sayi.text() else 36
    bolge_harf= str(ui.lineEdit_bolge_harf.text()) if ui.lineEdit_bolge_harf.text() else "SVK"
    sag_deger = int(ui.lineEdit_sag_deger.text()) if ui.lineEdit_sag_deger.text() else 86086
    yukari_deger = int(ui.lineEdit_yukari_deger.text()) if ui.lineEdit_yukari_deger.text() else 19432
    deneme = rakim_hesaplama.rakim_hesaplama(sag_deger, yukari_deger, bolge, bolge_harf)
    ui.label_sonuc.setText(str(deneme))

def sil():
    ui.lineEdit_bolge_harf.clear()
    ui.lineEdit_bolge_sayi.clear()
    ui.lineEdit_sag_deger.clear()
    ui.lineEdit_yukari_deger.clear()
    ui.label_sonuc.clear()

# Butonlar
ui.pushButton_hesapla.clicked.connect(hesapla)
ui.pushButton_sil.clicked.connect(sil)


uygulama.exec_()
