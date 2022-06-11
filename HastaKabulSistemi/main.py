# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
#----------------------KÜTÜPHANE--------------------------#
#---------------------------------------------------------#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from formUI import *

Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_HastaKayitKabul()
ui.setupUi(penAna)
penAna.show()


#----------------------VERİTABANI OLUŞTUR-----------------#
#---------------------------------------------------------#
import sqlite3
global curs
global conn

conn=sqlite3.connect('veritabani.db')
curs=conn.cursor()
sorguCreTblHastaKayit=("CREATE TABLE IF NOT EXISTS HastaKayit(                 \
                 Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,    \
                 TCNo TEXT NOT NULL UNIQUE,                        \
                 HastaAdi TEXT NOT NULL,                          \
                 HastaSoyadi TEXT NOT NULL,                       \
                 Cinsiyet TEXT NOT NULL,                           \
                 HastaneBolum TEXT NOT NULL,                              \
                 Doktor TEXT NOT NULL,                           \
                 DTarihi TEXT NOT NULL,                            \
                 RTarihi TEXT NOT NULL)")
curs.execute(sorguCreTblHastaKayit)
conn.commit()


#----------------------KAYDET-----------------------------#
#---------------------------------------------------------#
def EKLE():
    try:
        _lneTCK=ui.lneTCK.text()
        _lneAd=ui.lneAd.text()
        _lneSoyad=ui.lneSoyad.text()
        _cmbCinsiyet=ui.cmbCinsiyet.currentText()
        _cmbHbolum=ui.cmbHBolum.currentText()
        _cmbDoktor=ui.cmbDoktor.currentText()
        _cwDTarihi=ui.cwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)
        _cwRTarihi=ui.cwRTarihi.selectedDate().toString(QtCore.Qt.ISODate)
            
        
                
        curs.execute("INSERT INTO HastaKayit \
                         (TCNo,HastaAdi,HastaSoyadi,Cinsiyet,HastaneBolum,Doktor,DTarihi,RTarihi) \
                          VALUES (?,?,?,?,?,?,?,?)", \
                          (_lneTCK,_lneAd,_lneSoyad,_cmbCinsiyet,_cmbHbolum,_cmbDoktor, \
                           _cwDTarihi,_cwRTarihi))
        conn.commit()
    except Exception as Hata:
        ui.statusbar.setText(str("Hata meydana geldi: ")+str(Hata))    
 
#----------------------LİSTELE-----------------------------#
#---------------------------------------------------------#  
def LISTELE():
    try:
        ui.tableWidget.clear()
        
        ui.tableWidget.setHorizontalHeaderLabels(('DB No','TCNo','HastaAdi','HastaSoyadi','Cinsiyet','HastaneBolum','Doktor','DTarihi','RTarihi'))
        
        ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        curs.execute("SELECT * FROM HastaKayit")
            
        
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
        ui.lneTCK.clear()
        ui.lneSoyad.clear()
        ui.lneAd.clear()
        
        curs.execute("SELECT COUNT(*) FROM HastaKayit")
        kayitSayisi=curs.fetchone()
        ui.label_2.setText(str(kayitSayisi[0]))
    except Exception as Hata:
        ui.statusbar.setText(str("Hata meydana geldi: ")+str(Hata)) 
    
def CIKIS():
    try:
        cevap=QMessageBox.question(penAna,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                             QMessageBox.Yes | QMessageBox.No)
        if cevap==QMessageBox.Yes:
            conn.close()
            sys.exit(Uygulama.exec_())
        else:
            penAna.show()
    except Exception as Hata:
        ui.statusbar.setText(str("Hata meydana geldi: ")+str(Hata))         

def TEMIZLE():
    try:
        ui.lneTCK.setText("")
        ui.lneAd.setText("")
        ui.lneSoyad.setText("")
        ui.cmbCinsiyet.setCurrentIndex(-1)
        ui.cmbHBolum.setCurrentIndex(-1)
        ui.cmbDoktor.setCurrentIndex(-1)        
    except Exception as Hata:
        ui.statusbar.setText(str("Hata meydana geldi: ")+str(Hata))  
#----------------------SİL-----------------------------#
#---------------------------------------------------------# 
def SIL():
    try:
        cevap=QMessageBox.question(penAna,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",\
                             QMessageBox.Yes | QMessageBox.No)
        if cevap==QMessageBox.Yes:
            secili=ui.tableWidget.selectedItems()
            silinecek=secili[0].text()
            try:
                curs.execute("DELETE FROM HastaKayit WHERE Id='%s'" %(silinecek))
                conn.commit()
                
                LISTELE()
                ui.statusbar.setText(str("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ..."))
            except Exception as Hata:
                ui.statusbar.setText(str("Şöyle bir hata ile karşılaşıldı:"+str(Hata)))
        else:
            ui.statusbar.setText(str("Silme işlemi iptal edildi...",10000))
    except Exception as Hata:
        ui.statusbar.setText(str("Hata meydana geldi: ")+str(Hata))       
#----------------------ARAMA-----------------------------#
#---------------------------------------------------------# 
   
def KAYIT_ARA():
    try:
        aranan1=ui.lneTCK.text()
        aranan2=ui.lneAd.text()
        aranan3=ui.lneSoyad.text()

        
        curs.execute("SELECT * FROM HastaKayit WHERE TCNo=? OR HastaAdi=? OR HastaSoyadi=? OR (HastaAdi=? AND HastaSoyadi=?)",  \
                     (aranan1,aranan2,aranan3,aranan2,aranan3))
        conn.commit()
        ui.tableWidget.clear()
        ui.tableWidget.setHorizontalHeaderLabels(('DB No','TCNo','HastaAdi','HastaSoyadi','Cinsiyet','HastaneBolum','Doktor','DTarihi','RTarihi'))
        
        ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for satirIndeks, satirVeri in enumerate(curs):
            for sutunIndeks, sutunVeri in enumerate (satirVeri):
                ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))
    except Exception as Hata:
        ui.statusbar.setText(str("Hata meydana geldi: ")+str(Hata))     
 
#----------------------DOLDUR-----------------------------#
#---------------------------------------------------------#
def DOLDUR():
    try:
        secili=ui.tableWidget.selectedItems()
        ui.lneTCK.setText(secili[1].text())
        ui.lneAd.setText(secili[2].text())
        ui.lneSoyad.setText(secili[3].text())
        ui.cmbCinsiyet.setCurrentText(secili[4].text())
        ui.cmbHBolum.setCurrentText(secili[5].text())
        ui.cmbDoktor.setCurrentText(secili[6].text())
        
        yil=int(secili[7].text()[0:4])
        ay=int(secili[7].text()[5:7])
        gun=int(secili[7].text()[8:10])
        ui.cwDTarihi.setSelectedDate(QtCore.QDate(yil,ay,gun))

        yil=int(secili[7].text()[0:4])
        ay=int(secili[7].text()[5:7])
        gun=int(secili[7].text()[8:10])
        ui.cwRTarihi.setSelectedDate(QtCore.QDate(yil,ay,gun))
    except:
        ui.statusbar.setText(str("Kabul Edilmeyen Bölge Seçildi"))

    
#----------------------GÜNCELLE-----------------------------#
#---------------------------------------------------------#
def GUNCELLE():
    cevap=QMessageBox.question(penAna,"KAYIT GÜNCELLE","Kaydı güncellemek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        try:
            secili=ui.tableWidget.selectedItems()
            _Id=int(secili[0].text())
            _lneTCK=ui.lneTCK.text()
            _lneAd=ui.lneAd.text()
            _lneSoyad=ui.lneSoyad.text()
            _cmbCinsiyet=ui.cmbCinsiyet.currentText()
            _cmbHbolum=ui.cmbHBolum.currentText()
            _cmbDoktor=ui.cmbDoktor.currentText()
            _cwDTarihi=ui.cwDTarihi.selectedDate().toString(QtCore.Qt.ISODate)
            _cwRTarihi=ui.cwRTarihi.selectedDate().toString(QtCore.Qt.ISODate)
                
            
                    
            curs.execute("UPDATE HastaKayit SET TCNo=?,HastaAdi=?,HastaSoyadi=?,Cinsiyet=?,HastaneBolum=?,Doktor=?,DTarihi=?,RTarihi=? WHERE Id=?" , \
                              (_lneTCK,_lneAd,_lneSoyad,_cmbCinsiyet,_cmbHbolum,_cmbDoktor, \
                               _cwDTarihi,_cwRTarihi,_Id))
            conn.commit()
             
            LISTELE()
            
        except Exception as Hata:
            ui.statusbar.setText(str("Şöyle bir hata meydana geldi:"+str(Hata)))
    else:
        ui.statusbar.setText(str("Güncellme iptal edildi",10000))

   


#----------------------SİNYAL-SLOT-----------------------------#
#---------------------------------------------------------#
ui.btnEkle.clicked.connect(EKLE)
ui.btnListele.clicked.connect(LISTELE)
ui.btnCikis.clicked.connect(CIKIS)
ui.btnSil.clicked.connect(SIL)
ui.btnAra.clicked.connect(KAYIT_ARA)
ui.btnGuncelle.clicked.connect(GUNCELLE)
ui.btnTemizle.clicked.connect(TEMIZLE)
ui.tableWidget.itemSelectionChanged.connect(DOLDUR)

sys.exit(Uygulama.exec_())