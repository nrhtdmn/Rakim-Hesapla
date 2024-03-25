# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rakim_hesaplama.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(297, 344)
        Form.setStyleSheet("/* Genel stil kuralları */\n"
"* {\n"
"  background-color: #333333; /* Mavi arka plan */\n"
"  color: #FFFFFF; /* Beyaz yazı */\n"
"}\n"
"\n"
"/* Sekmeler için stil kuralları */\n"
"QTabBar::tab {\n"
"  background-color: #333333; /* Sekmelerin arka plan rengi */\n"
"  color: #ffffff; /* Beyaz yazı rengi */\n"
"  margin-left: 5px; /* Solda 5px boşluk bırak */\n"
"  margin-right: 5px; /* Sağda 5px boşluk bırak */\n"
"  border-right: 1px solid #E0E0E0; /* Kalın separator */\n"
"  border-image: linear-gradient(to right, #E0E0E0 0%, #F5F5F5 50%, #E0E0E0 100%); /* Sekmelerin arasına gölge ekleme */\n"
"}\n"
"\n"
"/* Fare üzerine geldiğinde sekmelerin rengi değişir */\n"
"QTabBar::tab:hover {\n"
"  background-color: #0651ff; /* Fare üzerine gelince arka plan rengi */\n"
"}\n"
"\n"
"/* Seçili sekmenin rengi değişir */\n"
"QTabBar::tab:selected {\n"
"  background-color:#2980b9; /* Seçili sekmenin arka plan rengi */\n"
"}\n"
"\n"
"/* Açılır menü stil kuralları */\n"
"QComboBox, QComboBox::drop-down {\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */\n"
"  background-color: #ffffff; /* Açılır menünün arka plan rengi */\n"
"}\n"
"\n"
"/* Seçili öğenin arka plan rengi */\n"
"QComboBox::item:selected {\n"
"  background-color: #eee;\n"
"}\n"
"\n"
"/* Açılır menü ok simgesi */\n"
"QComboBox::down-arrow {\n"
"  image: url(:/siyah/asagi.png); /* Ok simgesi */\n"
"  width: 16px; /* Ok resminin genişliği */\n"
"  height: 16px; /* Ok resminin yüksekliği */\n"
"}\n"
"\n"
"/* Açılır menü öğelerinin hover ve pressed efektleri */\n"
"QComboBox::item:hover {\n"
"  background-color: #f9f9f9;\n"
"}\n"
"\n"
"QComboBox::item:pressed {\n"
"  background-color: #ddd;\n"
"}\n"
"\n"
"/* Giriş kutuları ve açılır menülerin genel stil kuralları */\n"
" QComboBox {\n"
"  background-color: #ffffff; /* Arka plan rengi beyaz */\n"
"  color: #333333; /* Yazı rengi */\n"
"}\n"
"QLineEdit {\n"
"  background-color: #ffffff; /* Başlangıçta arka plan rengi beyaz */\n"
"}\n"
"\n"
"QLineEdit:!enabled {\n"
"  background-color: #ffff00; /* İçeriği dolu olan QLineEdit\'in arka plan rengi sarı */\n"
"}\n"
"\n"
"/* Butonların stil kuralları */\n"
"QPushButton, QToolButton {\n"
"  background-color: #333333; /* Arka plan rengi kırmızı */\n"
"  color: #ffffff; /* Yazı rengi beyaz */\n"
"}\n"
"\n"
"/* Buton hover efekti */\n"
"QPushButton:hover, QToolButton:hover {\n"
"  background-color: #c0392b; /* Hover rengi */\n"
"}\n"
"\n"
"/* Butonların stil kuralları */\n"
"QPushButton, QToolButton {\n"
"  background-color:  #333333; /* Arka plan rengi */\n"
"  color: #ffffff; /* Yazı rengi beyaz */\n"
"  border: 1px solid #b3ff26; /* Kenarlık */\n"
"  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */\n"
"  padding: 8px 16px; /* Buton içeriği için dolgular */\n"
"}\n"
"\n"
"/* Buton hover efekti */\n"
"QPushButton:hover, QToolButton:hover {\n"
"  background-color: #2980b9; /* Hover rengi */\n"
"  border-color: #2980b9; /* Kenarlık rengi */\n"
"}\n"
"\n"
"/* Buton basılma efekti */\n"
"QPushButton:pressed, QToolButton:pressed {\n"
"  background-color: #1f618d; /* Basılma rengi */\n"
"  border-color: #1f618d; /* Kenarlık rengi */\n"
"}\n"
"\n"
"/* Radyo düğmelerinin stil kuralları */\n"
"QRadioButton {\n"
"  color: #white; /* Yazı rengi */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"  width: 16px; /* Gösterge genişliği */\n"
"  height: 16px; /* Gösterge yüksekliği */\n"
"  border: 2px solid #3498db; /* Kenarlık rengi */\n"
"  border-radius: 8px; /* Gösterge köşeleri yuvarlatma */\n"
"  background-color: #ffffff; /* Arka plan rengi */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  background-color: #3498db; /* Seçili arka plan rengi */\n"
"  border-color: #3498db; /* Seçili kenarlık rengi */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"  border-color: #2980b9; /* Hover kenarlık rengi */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"  background-color: #2980b9; /* Seçili hover arka plan rengi */\n"
"  border-color: #2980b9; /* Seçili hover kenarlık rengi */\n"
"}\n"
"\n"
"/* QLineEdit stil kuralları */\n"
"QLineEdit {\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */\n"
"  /*padding: 6px; /* İçerik dolgusu */\n"
"  background-color: #ffffff; /* Arka plan rengi */\n"
"  color: #333333; /* Yazı rengi */\n"
"}\n"
"\n"
"/* QLineEdit hover efekti */\n"
"QLineEdit:hover {\n"
"  border-color: #3498db; /* Kenarlık rengi */\n"
"}\n"
"\n"
"/* QLineEdit odaklandığında */\n"
"QLineEdit:focus {\n"
"  border-color: #3498db; /* Kenarlık rengi */\n"
"}\n"
"\n"
"/* Etiketlerin (QLabel) stil kuralları */\n"
"\n"
"/* Etiketlerin hover efekti */\n"
"QLabel:hover {\n"
"  color: yellow; /* Hover rengi */\n"
"}\n"
"\n"
"/* Tablo Widget stil kuralları */\n"
"QTableWidget {\n"
"  alternate-background-color: #f5f5f5; /* Alternatif satır arka plan rengi */\n"
"  background-color: #333333; /* Arka plan rengi */\n"
"  color: #ffffff; /* Yazı rengi */\n"
"  selection-background-color: #3498db; /* Seçili arka plan rengi */\n"
"  selection-color: #ffffff; /* Seçili yazı rengi */\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */\n"
"  gridline-color: white;\n"
"  gridline-width: 1px; /* Satır ve sütun çizgilerinin kalınlığı */\n"
"}\n"
"\n"
"/* Tablo Widget satır hover efekti */\n"
"QTableWidget::item:hover {\n"
"  background-color: #f0f0f0; /* Satır üzerine gelindiğinde arka plan rengi */\n"
"}\n"
"\n"
"/* Tablo Widget başlık stil kuralları */\n"
"QHeaderView::section {\n"
"  background-color: #333333; /* Başlık arka plan rengi */\n"
"  color: #ffffff; /* Başlık yazı rengi */\n"
"  padding: 4px; /* Başlık dolgusu */\n"
"  border: none; /* Başlık kenarlığı yok */\n"
"  font-weight: bold; /* Kalın yazı tipi */\n"
"  font-size: 11pt; /* 11 punto yazı boyutu */\n"
"}\n"
"\n"
"/* Tablo Widget hücre içeriği */\n"
"QTableWidget QTableWidget::item {\n"
"  font-family: Arial; /* Yazı tipi */\n"
"  font-size: 11pt; /* 11 punto yazı boyutu */\n"
"}\n"
"\n"
"/* Tablo Widget\'in içeriğini sığdırma */\n"
"QTableView {\n"
"  font-size: 11pt; /* Yazı boyutu */\n"
"  alternate-background-color: #f5f5f5; /* Alternatif satır arka plan rengi */\n"
"  background-color: #333333; /* Arka plan rengi */\n"
"  color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"/* Tablo Widget başlık hover efekti */\n"
"QHeaderView::section:hover {\n"
"  background-color: #2980b9; /* Başlık üzerine gelindiğinde arka plan rengi */\n"
"}\n"
"\n"
"/* QGroupBox stil kuralları */\n"
"QGroupBox {\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 6px; /* Kenarlık köşeleri yuvarlatma */\n"
"  padding: 6px; /* İçerik dolgusu */\n"
"  background-color: #333333; /* Arka plan rengi */\n"
"  color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"/* QGroupBox başlık stil kuralları */\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin; /* Başlık başlangıç noktası */\n"
"  subcontrol-position: top left; /* Başlık pozisyonu */\n"
"  left: 10px; /* Sol boşluk */\n"
"  padding: 0 6px; /* Başlık içeriği için dolgu */\n"
"  background-color: #333333; /* Arka plan rengi */\n"
"  color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"/* İç içe tablar için stil kuralları */\n"
"QTabWidget::pane {\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  background-color: #ffffff; /* Arka plan rengi */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"  alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  border-top-left-radius: 4px;\n"
"  border-top-right-radius: 4px;\n"
"  min-width: 8ex;\n"
"  padding: 4px;\n"
"  border: 1px solid grey; /*#ccc;*/ /* Kenarlık rengi ve kalınlığı */\n"
"  background-color: #f5f5f5; /* Arka plan rengi */\n"
"  color: #333333; /* Yazı rengi */\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"  background-color: #333333; /* Seçili sekmenin arka plan rengi */\n"
"  color: #ffffff; /* Seçili sekmenin yazı rengi */\n"
"}\n"
"\n"
"/* Tablodaki satırlar ve sütunlar arası çizgilerin rengini beyaz ve ince yapma */\n"
"QTableWidget QTableView {\n"
"  gridline-color: white; /* Satır ve sütun çizgilerinin rengi */\n"
"  gridline-width: 1px; /* Satır ve sütun çizgilerinin kalınlığı */\n"
"}\n"
"\n"
"/* QLineEdit içeriğinde yazı varken arka plan rengini sarı yapma */\n"
"/*QLineEdit {\n"
"  background-color: #ffffff; /* Başlangıçta arka plan rengi beyaz }*/\n"
"\n"
"\n"
"/*QLineEdit:focus {\n"
"  background-color: #ffff00; /* İçeriğe odaklandığında arka plan rengi sarı }*/\n"
"\n"
"\n"
"/* QLineEdit içeriği doluyken arka plan rengini sarı yapma */\n"
"\n"
"/* Combobox stil kuralları */\n"
"QComboBox {\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */\n"
"  background-color: #ffffff; /* Arka plan rengi */\n"
"}\n"
"\n"
"/* Combobox üzerine gelindiğinde */\n"
"QComboBox:hover {\n"
"  background-color: #ffff00; /* Sarı arka plan rengi */\n"
"}\n"
"\n"
"/* LineEdit stil kuralları */\n"
"QLineEdit {\n"
"  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */\n"
"  background-color: #ffffff; /* Arka plan rengi */\n"
"}\n"
"\n"
"/* LineEdit üzerine gelindiğinde */\n"
"QLineEdit:hover {\n"
"  background-color: #ffff00; /* Sarı arka plan rengi */\n"
"}\n"
"\n"
"/* GroupBox stil kuralları */\n"
"QGroupBox {\n"
"  border: 2px solid grey;/*#ccc;*/ /* Kenarlık rengi ve kalınlığı */\n"
"  border-radius: 6px; /* Kenarlık köşeleri yuvarlatma */\n"
"  padding: 6px; /* İçerik dolgusu */\n"
"  background-color: #333333; /* Arka plan rengi */\n"
"  color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"/* GroupBox üzerine gelindiğinde */\n"
"QGroupBox:hover {\n"
"  background-color: #ffff00; /* Sarı arka plan rengi */\n"
"color:#ffffff /* Yazı rengi */\n"
"}\n"
"\n"
"/* CheckButton ve RadioButton stil kuralları */\n"
"QCheckBox, QRadioButton {\n"
"  color: #ffffff; /* Yazı rengi */\n"
"}\n"
"\n"
"/* CheckButton ve RadioButton üzerine gelindiğinde */\n"
"QCheckBox:hover, QRadioButton:hover {\n"
"  background-color: #ffff00; /* Sarı arka plan rengi */\n"
"  color: black; /* Yazı rengi */\n"
"  border-radius: 3px; /* Kenarlık köşeleri yuvarlatma */\n"
"  /*padding: 1px; /* İçerik dolgusu */\n"
"}\n"
"\n"
"/*--------------------------------------------------------------------*/\n"
"\n"
"/* StackedWidget ileri ve geri butonlarının stil kuralları */\n"
"QStackedWidget > QAbstractButton {\n"
"  background-color: #333333; /* Arka plan rengi ile aynı renk */\n"
"  border: none; /* Kenarlık yok */\n"
"  width: 0; /* Genişlik sıfır */\n"
"  height: 0; /* Yükseklik sıfır */\n"
"}\n"
"\n"
"/* İleri ve geri butonlarının üzerine gelindiğinde */\n"
"QStackedWidget > QAbstractButton:hover {\n"
"  background-color: #333333; /* Arka plan rengi ile aynı renk */\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_bolge_sayi = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_bolge_sayi.setFont(font)
        self.lineEdit_bolge_sayi.setText("")
        self.lineEdit_bolge_sayi.setObjectName("lineEdit_bolge_sayi")
        self.gridLayout.addWidget(self.lineEdit_bolge_sayi, 0, 1, 1, 1)
        self.lineEdit_bolge_harf = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_bolge_harf.setFont(font)
        self.lineEdit_bolge_harf.setObjectName("lineEdit_bolge_harf")
        self.gridLayout.addWidget(self.lineEdit_bolge_harf, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_sag_deger = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_sag_deger.setFont(font)
        self.lineEdit_sag_deger.setObjectName("lineEdit_sag_deger")
        self.gridLayout.addWidget(self.lineEdit_sag_deger, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_yukari_deger = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_yukari_deger.setFont(font)
        self.lineEdit_yukari_deger.setObjectName("lineEdit_yukari_deger")
        self.gridLayout.addWidget(self.lineEdit_yukari_deger, 2, 1, 1, 2)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_sil = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sil.setFont(font)
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.horizontalLayout.addWidget(self.pushButton_sil)
        self.pushButton_hesapla = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_hesapla.setFont(font)
        self.pushButton_hesapla.setObjectName("pushButton_hesapla")
        self.horizontalLayout.addWidget(self.pushButton_hesapla)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_sonuc = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_sonuc.setFont(font)
        self.label_sonuc.setObjectName("label_sonuc")
        self.verticalLayout.addWidget(self.label_sonuc)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Bölge"))
        self.label_2.setText(_translate("Form", "Sağ Değer"))
        self.label_3.setText(_translate("Form", "Yukarı Değer"))
        self.pushButton_sil.setText(_translate("Form", "Sil"))
        self.pushButton_hesapla.setText(_translate("Form", "Hesapla"))
        self.label_sonuc.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))