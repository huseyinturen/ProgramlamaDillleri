# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HastaKayitKabul(object):
    def setupUi(self, HastaKayitKabul):
        HastaKayitKabul.setObjectName("HastaKayitKabul")
        HastaKayitKabul.resize(982, 685)
        self.layoutWidget = QtWidgets.QWidget(HastaKayitKabul)
        self.layoutWidget.setGeometry(QtCore.QRect(680, 30, 82, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnEkle = QtWidgets.QPushButton(self.layoutWidget)
        self.btnEkle.setObjectName("btnEkle")
        self.verticalLayout_6.addWidget(self.btnEkle)
        self.btnSil = QtWidgets.QPushButton(self.layoutWidget)
        self.btnSil.setObjectName("btnSil")
        self.verticalLayout_6.addWidget(self.btnSil)
        self.btnAra = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAra.setObjectName("btnAra")
        self.verticalLayout_6.addWidget(self.btnAra)
        self.verticalLayoutWidget = QtWidgets.QWidget(HastaKayitKabul)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(680, 130, 82, 116))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnGuncelle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.verticalLayout_4.addWidget(self.btnGuncelle)
        self.btnListele = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnListele.setObjectName("btnListele")
        self.verticalLayout_4.addWidget(self.btnListele)
        self.btnCikis = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCikis.setObjectName("btnCikis")
        self.verticalLayout_4.addWidget(self.btnCikis)
        self.btnTemizle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnTemizle.setObjectName("btnTemizle")
        self.verticalLayout_4.addWidget(self.btnTemizle)
        self.groupBox = QtWidgets.QGroupBox(HastaKayitKabul)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 650, 428))
        self.groupBox.setObjectName("groupBox")
        self.cwRTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwRTarihi.setGeometry(QtCore.QRect(328, 228, 312, 190))
        self.cwRTarihi.setObjectName("cwRTarihi")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 206, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(328, 206, 77, 16))
        self.label_8.setObjectName("label_8")
        self.cwDTarihi = QtWidgets.QCalendarWidget(self.groupBox)
        self.cwDTarihi.setGeometry(QtCore.QRect(10, 228, 312, 190))
        self.cwDTarihi.setObjectName("cwDTarihi")
        self.lneAd = QtWidgets.QLineEdit(self.groupBox)
        self.lneAd.setGeometry(QtCore.QRect(130, 60, 133, 22))
        self.lneAd.setMaxLength(10)
        self.lneAd.setObjectName("lneAd")
        self.lneTCK = QtWidgets.QLineEdit(self.groupBox)
        self.lneTCK.setGeometry(QtCore.QRect(130, 30, 133, 22))
        self.lneTCK.setMaxLength(11)
        self.lneTCK.setObjectName("lneTCK")
        self.lneSoyad = QtWidgets.QLineEdit(self.groupBox)
        self.lneSoyad.setGeometry(QtCore.QRect(130, 90, 133, 22))
        self.lneSoyad.setMaxLength(10)
        self.lneSoyad.setObjectName("lneSoyad")
        self.lneTCK_2 = QtWidgets.QLabel(self.groupBox)
        self.lneTCK_2.setGeometry(QtCore.QRect(11, 27, 75, 16))
        self.lneTCK_2.setObjectName("lneTCK_2")
        self.lneAd_2 = QtWidgets.QLabel(self.groupBox)
        self.lneAd_2.setGeometry(QtCore.QRect(11, 57, 16, 16))
        self.lneAd_2.setObjectName("lneAd_2")
        self.lneSoyad_2 = QtWidgets.QLabel(self.groupBox)
        self.lneSoyad_2.setGeometry(QtCore.QRect(11, 87, 32, 16))
        self.lneSoyad_2.setObjectName("lneSoyad_2")
        self.lneCinsiyet = QtWidgets.QLabel(self.groupBox)
        self.lneCinsiyet.setGeometry(QtCore.QRect(11, 117, 42, 16))
        self.lneCinsiyet.setObjectName("lneCinsiyet")
        self.cmbCinsiyet = QtWidgets.QComboBox(self.groupBox)
        self.cmbCinsiyet.setGeometry(QtCore.QRect(130, 120, 131, 21))
        self.cmbCinsiyet.setObjectName("cmbCinsiyet")
        self.cmbCinsiyet.addItem("")
        self.cmbCinsiyet.addItem("")
        self.cmbHBolum = QtWidgets.QComboBox(self.groupBox)
        self.cmbHBolum.setGeometry(QtCore.QRect(130, 147, 131, 22))
        self.cmbHBolum.setObjectName("cmbHBolum")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.cmbHBolum.addItem("")
        self.lneHbolum = QtWidgets.QLabel(self.groupBox)
        self.lneHbolum.setGeometry(QtCore.QRect(11, 147, 81, 16))
        self.lneHbolum.setObjectName("lneHbolum")
        self.lneDoktpr = QtWidgets.QLabel(self.groupBox)
        self.lneDoktpr.setGeometry(QtCore.QRect(11, 177, 39, 16))
        self.lneDoktpr.setObjectName("lneDoktpr")
        self.cmbDoktor = QtWidgets.QComboBox(self.groupBox)
        self.cmbDoktor.setGeometry(QtCore.QRect(132, 177, 131, 22))
        self.cmbDoktor.setObjectName("cmbDoktor")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.cmbDoktor.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(HastaKayitKabul)
        self.tableWidget.setGeometry(QtCore.QRect(20, 450, 951, 192))
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.label = QtWidgets.QLabel(HastaKayitKabul)
        self.label.setGeometry(QtCore.QRect(10, 640, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(HastaKayitKabul)
        self.label_2.setGeometry(QtCore.QRect(100, 641, 71, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.statusbar = QtWidgets.QLabel(HastaKayitKabul)
        self.statusbar.setGeometry(QtCore.QRect(0, 661, 981, 20))
        self.statusbar.setText("")
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(HastaKayitKabul)
        self.cmbCinsiyet.setCurrentIndex(-1)
        self.cmbHBolum.setCurrentIndex(-1)
        self.cmbDoktor.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(HastaKayitKabul)

    def retranslateUi(self, HastaKayitKabul):
        _translate = QtCore.QCoreApplication.translate
        HastaKayitKabul.setWindowTitle(_translate("HastaKayitKabul", "Widget"))
        self.btnEkle.setText(_translate("HastaKayitKabul", "KAYIT EKLE"))
        self.btnSil.setText(_translate("HastaKayitKabul", "KAYIT SİL"))
        self.btnAra.setText(_translate("HastaKayitKabul", "KAYIT ARA"))
        self.btnGuncelle.setText(_translate("HastaKayitKabul", "GÜNCELLE"))
        self.btnListele.setText(_translate("HastaKayitKabul", "KAYIT LİSTELE"))
        self.btnCikis.setText(_translate("HastaKayitKabul", "ÇIKIŞ"))
        self.btnTemizle.setText(_translate("HastaKayitKabul", "TEMİZLE"))
        self.groupBox.setTitle(_translate("HastaKayitKabul", "Hasta Bilgileri"))
        self.label_7.setText(_translate("HastaKayitKabul", "Doğum Tarihi"))
        self.label_8.setText(_translate("HastaKayitKabul", "Randevu Tarihi"))
        self.lneTCK_2.setText(_translate("HastaKayitKabul", "T.C. Kimlik No"))
        self.lneAd_2.setText(_translate("HastaKayitKabul", "Ad"))
        self.lneSoyad_2.setText(_translate("HastaKayitKabul", "Soyad"))
        self.lneCinsiyet.setText(_translate("HastaKayitKabul", "Cinsiyet"))
        self.cmbCinsiyet.setItemText(0, _translate("HastaKayitKabul", "Kadın"))
        self.cmbCinsiyet.setItemText(1, _translate("HastaKayitKabul", "Erkek"))
        self.cmbHBolum.setItemText(0, _translate("HastaKayitKabul", "İç Hastalıkları"))
        self.cmbHBolum.setItemText(1, _translate("HastaKayitKabul", "Yoğun Bakım"))
        self.cmbHBolum.setItemText(2, _translate("HastaKayitKabul", "Kardiyoloji"))
        self.cmbHBolum.setItemText(3, _translate("HastaKayitKabul", "Göğüs Hastalıkları"))
        self.cmbHBolum.setItemText(4, _translate("HastaKayitKabul", "Nöroloji"))
        self.cmbHBolum.setItemText(5, _translate("HastaKayitKabul", "Psikiyatri"))
        self.cmbHBolum.setItemText(6, _translate("HastaKayitKabul", "Fiziksel Tıp ve Rehabilitasyon"))
        self.cmbHBolum.setItemText(7, _translate("HastaKayitKabul", "Genel Cerrahi"))
        self.cmbHBolum.setItemText(8, _translate("HastaKayitKabul", "Üroloji"))
        self.cmbHBolum.setItemText(9, _translate("HastaKayitKabul", "Göz Hastalıkları"))
        self.cmbHBolum.setItemText(10, _translate("HastaKayitKabul", "Kulak-Burun-Boğaz Hastalıkları"))
        self.cmbHBolum.setItemText(11, _translate("HastaKayitKabul", "Radyoloji"))
        self.cmbHBolum.setItemText(12, _translate("HastaKayitKabul", "Ağız, Diş, Çene Hastalıkları ve Cerrahisi"))
        self.lneHbolum.setText(_translate("HastaKayitKabul", "Hastane Bölüm"))
        self.lneDoktpr.setText(_translate("HastaKayitKabul", "Doktor "))
        self.cmbDoktor.setItemText(0, _translate("HastaKayitKabul", "Cemil ÇALIŞKAN"))
        self.cmbDoktor.setItemText(1, _translate("HastaKayitKabul", "Muhtar Sinan ERSİN"))
        self.cmbDoktor.setItemText(2, _translate("HastaKayitKabul", "Murat ZEYTÜNLÜ"))
        self.cmbDoktor.setItemText(3, _translate("HastaKayitKabul", "Özer MAKAY"))
        self.cmbDoktor.setItemText(4, _translate("HastaKayitKabul", "Recep Gökhan İÇÖZ"))
        self.cmbDoktor.setItemText(5, _translate("HastaKayitKabul", "Zekeriya Erhan AKGÜN"))
        self.cmbDoktor.setItemText(6, _translate("HastaKayitKabul", "Alper UĞUZ"))
        self.cmbDoktor.setItemText(7, _translate("HastaKayitKabul", "Levent YENİAY"))
        self.cmbDoktor.setItemText(8, _translate("HastaKayitKabul", "Murat ÖZDEMİR"))
        self.cmbDoktor.setItemText(9, _translate("HastaKayitKabul", "Taylan Özgür SEZER"))
        self.cmbDoktor.setItemText(10, _translate("HastaKayitKabul", "Sibel BOYVADA ÖZALP"))
        self.label.setText(_translate("HastaKayitKabul", "Kayıt Sayısı:"))