<!-- # Bulunduğunuz Konumun Rakımını bulun.


Hakkında

Bu depo, arayüzlü rakım hesaplamanızı sağlar.

Bu depo şunları içerir:

    Mgrs'yi coğrafiye çeviren kodlar. 
    Arayüz oluşturacak kodlar ve .ui yi .py ye dönüştüren kodlar
    

Kurulum

    Bu depoyu klonlayın.
    Gerekli bağımlılıkları yüklemek için klonlanan depodan şu komutları çalıştırın:



pip install -r  requirements.txt


Kullanımı
main.py dosyasını çalıştırın.
Açılan arayüzde Bölge ye (birinci boşluk 36 gibi) (ikinci boşluk SVK) gibi değer, sağ ve yukarı değerlerini girerek hesapla butonuna basınız.
internetin bulunduğu ortamda belirtilen konumun deniz seviyesinden yüksekliği (rakım) gözükecektir. 
Doldurmadan doğrudan hesaplaya tıklanması durumunda Anıtkabir'in rakımı verilecektir. 
Sil butonuna tıklandığında tüm uygulamadan veriler silinecek bir sonraki sorgulama için hazır olunacaktır.

##############################################################################################################

# Determine the Elevation of Your Location.

About

This repository enables you to calculate elevation with a user-friendly interface.

This repository includes:

    Codes converting Mgrs to geography.
    Codes creating the interface and converting .ui to .py
    

Installation

    Clone this repository.
    Run the following commands from the cloned repository to install the necessary dependencies:



pip install -r requirements.txt


Usage
Run the main.py file.
Enter values such as Zone (first blank, e.g., 36) and Quadrant (second blank, e.g., SVK), as well as right and upward values into the interface, and click on the Calculate button.
The elevation (altitude above sea level) of the specified location will be displayed in an environment with internet access.
If clicked without filling out, the elevation of Anıtkabir will be provided.
Clicking the Clear button will erase all data from the application, making it ready for the next query.
