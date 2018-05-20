# RFID G�venlik Sistemi
**Haz�rlayan: �rem KARABUDAK**

***

Bu klas�rde, RFID G�venlik Sistemi projesinin kodlar�na, projede yararlan�lan k�t�phane linklerine, ve medya i�eriklerine yer verilmi�tir.

***

_**Projede Kullan�lan Malzemeler:**_

*Arduino Pro(Atmega328P / 5v 16MHz)
*Protoboard
*3.7V 860mAh Li-Ion Battery
*RF433MHz Tx mod�l�
*TP4056 Battery Charger(5V 1A)
*Switch
*Step-Up mod�l�(Output:5V)
*AMS1117 Voltage Regulator(Output:3.3V)
*Arduino Logic Level Converter(3.3V-5V)
*RFID-RC522 mod�l�(13.56 MHz)
*S50 1K 13.56MHz RFID Kart x2
*NTAG213 13.56MHz IC NFC Tag(MIFARE Ultralight)
*Proje Kutusu(54mmx84mmx32mm)
*220ohm Diren� x3
*RGB Led
*CP2102 USB to TTL Converter mod�l�

_**Projede Al�c� Devresi ��in Kullan�lan Malzemeler:**_

*Arduino Nano(Atmega328P / 5v 16MHz)
*Mini Breadboard x2
*RF433MHz Rx mod�l�
*220ohm Diren�
*Ye�il Led
*Jumper kablolar

_**Yaz�l�m�n �al��t�r�lma �ekli:**_

*Yaz�l�m�n �al��t�r�lmas� i�in gerekli olan k�t�phaneler a�a��daki linkten indirilerek(versiyonuna dikkat edilmeli) Arduino IDE'deki "libraries" klas�r�ne at�l�r. Daha sonra Arduino, CP2102 USB to TTL mod�l� yard�m�yla bilgisayara ba�lan�r ve "RFIDSecuritySystem.ino" uzant�l� kod, "i�lemci", "kart" ve "port" bilgileri(Atmega328P/Arduino Pro/COM...) se�ildikten sonra y�klenir. Sistemin yaz�l�m�n�n y�klenmesi tamamlanm�� olur.

_**Edinilmesi Gereken K�t�phaneler ve Linkleri:**_

*MFRC522.h - https://github.com/miguelbalboa/rfid
*RCSwitch.h(version: 2.6.2) - https://github.com/sui77/rc-switch

***

Sistemin kodu RFIDSecuritySystem.ino, al�c� kodu ise RF_Receiver.ino dosyas�ndad�r.

***

_**Donan�m�n Ba�lant�s� ve �al��ma �ekli:**_

*Sistem elemanlar� protoboard �zerine yerle�tirilmi� ve lehimlenmi�tir. Bu elemanlar�n GND pinleri birle�tirilmi�tir.
*Proje 3.7V bir Li-Ion bataryadan g�c�n� almaktad�r. 
*Batarya TP4056 destekli �arj ve koruma devresine ba�l�d�r ve koruma devresinin ��k��lar� da bir switch yoluyla 5V step-up mod�l�n�n giri�ine ba�lanm��t�r. 5V step-up mod�l�n�n ��k��� hem Arduino Pro (5v 16Mhz) hem 433Mhz RF Tx mod�l� hem de AMS1117-3.3V LDO'yu beslemektedir.LDO'nun 3.3V ��k��� da RFID mod�l�n�n g�� pinine ba�lanm��t�r. 
*RFID mod�l�n�n, Tx mod�l�n�n ve RGB ledin Arduino ile olan ba�lant� �ekli kodun �st k�sm�ndaki a��klama b�l�m�nde verilmi�tir.

_**Projenin Kullan�m �ekli:**_

*Olu�turulan g�venlik sisteminin aktif hale gelebilmesi i�in switch sola �ekilerek ON konumuna getirilir. Sistem �al��t�r�ld���nda ilk al�nan geri bildirim, ledin rengidir. Led, kullan�c�ya �nceki �al��madaki son durum verisini(k�rm�z�(off)/ye�il(on)) bildirmektedir.
*De�i�im kart� bir kez okutulur, 500ms boyunca mavi geri bildirim ledi yanar. Daha sonra sisteme eklenmek istenen kart okutulur. E�er sisteme ilk kez kart okutuluyorsa, 800ms; ikinci bir kart okutuluyorsa, 1600ms boyunca bildirim ledi(mavi) yanar ve kart ekleme i�lemi tamamlan�r.
*Sistem, 2 kart slotuna sahiptir. ���nc� bir kart sisteme eklenmek istendi�inde, sistem tan�ms�z kart olarak alg�lar ve k�sa aral�klarla(300ms) 3 kez bildirim ledi yan�p s�ner.
*De�i�im kart� arka arkaya 2 kez okutuldu�unda, sistemdeki tan�ml� kartlar silinir. K�sa aral�klarla(100ms) 8 kez bildirim ledi yan�p s�ner.
*Sistemde tan�ml� olan bir kart okutuldu�unda a�/kapat kontrol i�lemini yapar. Ye�il(ON) ve k�rm�z�(OFF) led ile 1sn boyunca geri bildirim al�n�r ve bu s�rada RF verici mod�l� ile a�ma ve kapatma sinyali 10ms aral�kla 2 defa g�nderilir. Kar��da bir al�c� devresi oldu�u taktirde bir ba�ka cihaz�n da end�striyel anahtarlama kontrol� ayn� �ekilde sa�lanabilir.






