**Python Script to EXE Converter**

Bu proje, bir Python dosyasını seçip onu .exe dosyasına dönüştüren bir Tkinter tabanlı GUI uygulamasıdır. Aşağıda bu projenin nasıl kullanılacağını adım adım anlatan bir rehber bulunmaktadır.


**Gereksinimler**
Bu scriptin çalışabilmesi için aşağıdaki yazılımlar ve kütüphaneler gerekmektedir:

Python (3.x versiyonu)
PyInstaller
Tkinter
Eğer bu kütüphaneler sisteminizde yüklü değilse, aşağıdaki komutlarla yükleyebilirsiniz:

pip install pyinstaller
pip install tk
Kullanım Kılavuzu

**Adım 1: Python Dosyasını Seçin**
Programı çalıştırdıktan sonra, bir dosya seçici penceresi açılacak ve dönüştürmek istediğiniz Python (.py) dosyasını seçmeniz istenecektir. Seçimi yaptıktan sonra dosya yolu otomatik olarak programa dahil edilecektir.

**Adım 2: Python Dosyasını .exe Dosyasına Dönüştürün**
Python dosyasını seçtikten sonra, PyInstaller kullanarak bu dosya .exe dosyasına dönüştürülecektir. Program --onefile, --hidden-import=pyodbc, --hidden-import=pandas, ve --hidden-import=sqlalchemy parametrelerini kullanarak dönüştürme işlemini gerçekleştirecektir.

**Adım 3: Çıktı Klasörünü Açın**
Dönüştürme işlemi tamamlandıktan sonra, .exe dosyasının bulunduğu dist klasörü otomatik olarak açılacaktır. Bu klasörde dönüştürülmüş olan .exe dosyanızı bulabilirsiniz.

**Hata Yönetimi**
Herhangi bir hata oluşursa, hata mesajı ekrana yazdırılacaktır.
