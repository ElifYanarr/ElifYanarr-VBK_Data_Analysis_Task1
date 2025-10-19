# VBK Veri Analizi Projesi: İlaç Detayları Analizi ve Modelleme Raporu

Bu README dosyası, VBK Proje & Yarışma Ekibi için hazırlanan "Task 1. Aşaması" kapsamındaki veri bilimi ödevinin analiz adımlarını ve bulgularını özetlemektedir.

## Analiz Adımları

### 1. Veri Keşfi ve EDA (Açıklayıcı Veri Analizi)
* Temel veri incelemesi ve özet istatistikler.
* Eksik değer analizi ve veri tiplerinin doğrulanması.

## 2. Temel Analizler ve Görselleştirmeler
Proje kapsamında veriyi anlamlandırmak için altı (6) farklı görselleştirme oluşturulmuştur:
* **Top 10 Medicine Manufacturers:** En çok ilaç üreten ilk 10 üreticiyi gösteren bar grafiği.
* **Most Common Usage Purposes:** En yaygın kullanım amaçlarını gösteren bar grafiği.
* **Review Percentages Correlation:** İnceleme yüzdeleri arasındaki korelasyonu gösteren ısı haritası (Heatmap).
* **Excellent Review Distribution:** Mükemmel inceleme puanlarının dağılımını gösteren histogram.
* **Target Class Distribution:** Hedef sınıfın dağılımını gösteren pasta grafiği (Pie Chart).
* **Name Length vs Review Score:** İlaç adının uzunluğu ile inceleme skoru arasındaki ilişkiyi gösteren dağılım grafiği (Scatter Plot).

###  Görselleştirmeler (6 Adet)
https://drive.google.com/drive/folders/1rVc5iVybOLJ6ZTeWBJUtsTgqbkCmei6_?usp=drive_link

### 3. Özellikler (Feature Engineering)
* **`name_length`:** İlaç isimlerinin uzunluğunu hesaplayan yeni bir özellik oluşturulmuştur.
* **`Is_Top_Use`:** En yaygın ilk 5 kullanım amacını gösteren ikili (Binary) hedef değişkeni oluşturulmuştur.

### 4. Makine Öğrenimi Modellemesi
* **Algoritma:** Logistic Regression (Lojistik Regresyon)
* **Özellik (Feature):** İlaç adı uzunluğu (`Medicine name length`)
* **Hedef (Target):** En yaygın 5 kullanım amacının sınıflandırılması (`Top 5 usage classification`)
* **Veri Bölme:** %70 Eğitim, %30 Test oranı.
* **Değerlendirme Metrikleri:** Doğruluk (Accuracy), Kesinlik (Precision), Hassasiyet (Recall), F1-Skoru (F1-Score).

---

## Model Sonuçları

Aşağıdaki metrikler, basit sınıflandırma modelinin test veri setindeki performansını göstermektedir:

Veri Seti: Medicine_Details.csv
Açıklama: İlaç detayları, incelemeleri ve kullanım bilgilerini içeren veri seti
Değişken Sayısı: 9
Gözlem Sayısı: 11825

Değişkenler ve Tipleri:
- Medicine Name: object
- Composition: object
- Uses: object
- Side_effects: object
- Image URL: object
- Manufacturer: object
- Excellent Review %: int64
- Average Review %: int64
- Poor Review %: int64

 VERİ TANIMA VE TEMEL EDA ÇIKTILARI

 İlk 5 Satır:
              Medicine Name  ... Poor Review %
0   Avastin 400mg Injection  ...            22
1  Augmentin 625 Duo Tablet  ...            18
2       Azithral 500 Tablet  ...            21
3          Ascoril LS Syrup  ...            35
4         Aciloc 150 Tablet  ...            29

[5 rows x 9 columns]

 Eksik Değerler (Null Count):
Medicine Name         0
Composition           0
Uses                  0
Side_effects          0
Image URL             0
Manufacturer          0
Excellent Review %    0
Average Review %      0
Poor Review %         0
dtype: int64

 Özet İstatistikler (Sayısal):
       Excellent Review %  Average Review %  Poor Review %
count        11825.000000      11825.000000   11825.000000
mean            38.516025         35.756364      25.727611
std             25.225343         18.268134      23.991985
min              0.000000          0.000000       0.000000
25%             22.000000         27.000000       0.000000
50%             34.000000         35.000000      22.000000
75%             51.000000         47.000000      35.000000
max            100.000000         88.000000     100.000000

Aykırı Değer Analizi (Excellent Review %):
Aykırı değer sayısı: 610
Aykırı değer oranı: 5.16%

## Ana Bulgular (Key Findings)

* Hedef değişkende belirgin bir sınıf dengesizliği (Class imbalance) gözlemlenmiştir.
* İlaç adı uzunluğu ile kullanım kalıpları arasında zayıf bir korelasyon bulunmaktadır.
* Pazarda baskın olan üreticiler ve en yaygın kullanım amaçları başarıyla tespit edilmiştir.
* İnceleme yüzdeleri, beklendiği gibi ters (inverse) ilişkiler göstermektedir.


## Önemli Notlar

* Script'e devam etmek için tüm görselleştirme pencerelerinin kapatıldığından emin olunmalıdır.
* Sonuçlar, kullanılan rastgele durum (random state) ve veri bölmelerine göre farklılık gösterebilir.
* Kurulan model, temel bir gösterim amaçlıdır ve daha karmaşık modellerle geliştirilebilir.

## Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen şu adımları takip edin:
1.  Projeyi çatallayın (`Fork the project`).
2.  Özellik dalınızı oluşturun (`git checkout -b feature/AmazingFeature`).
3.  Değişikliklerinizi kaydedin (`git commit -m 'Add some AmazingFeature'`).
4.  Dala gönderin (`git push origin feature/AmazingFeature`).
5.  Bir Pull Request açın.
