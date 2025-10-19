# GEREKLİ KÜTÜPHANELERİN YÜKLENMESİ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression   
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score 

# VERİ SETİNİN OKUNMASI 
df = pd.read_csv('/Users/elifyanar/Desktop/VBK-Task1/Medicine_Details.csv')

# --- 1 & 2. VERİ TANIMA (EDA) ÇIKTILARI ---
print("=" * 50)
print("1 & 2. VERİ TANIMA VE TEMEL EDA ÇIKTILARI")
print("=" * 50)
print(" İlk 5 Satır:")
print(df.head())

print("\n Eksik Değerler (Null Count):")
print(df.isnull().sum()) 

print("\n Özet İstatistikler (Sayısal):")
print(df.describe())

# --- GÖRSELLEŞTİRME VE MODEL İÇİN ÖN HAZIRLIK ---
# Özellik Mühendisliği (Model ve Görsel için)
df['name_length'] = df['Medicine Name'].apply(lambda x: len(str(x)))

# Hedef (Target) Belirleme (Model ve Görsel için)
top_uses = df['Uses'].value_counts().nlargest(5).index.tolist()
df['Is_Top_Use'] = df['Uses'].apply(lambda x: 1 if x in top_uses else 0)


# --- 3. VERİ GÖRSELLEŞTİRME (6 ADET AYRI PENCERE) ---
print("\n" + "=" * 50)
print("3. VERİ GÖRSELLEŞTİRME (6 ADET AYRI PENCERE AÇILACAK)")
print("Lütfen her pencereyi kapattığınızdan emin olun.")
print("=" * 50)

# -------------------------------------------------------------
# GÖRSEL 1: Üretici Dağılımı 
plt.figure(figsize=(12, 6))
top_manufacturers = df['Manufacturer'].value_counts().nlargest(10)
sns.barplot(x=top_manufacturers.index, y=top_manufacturers.values, palette="viridis")
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title('1. En Çok İlaç Üreten İlk 10 Firma', fontsize=16)
plt.ylabel('İlaç Sayısı')
plt.tight_layout()
plt.show() # Pencere 1 açılır

# -------------------------------------------------------------
# GÖRSEL 2: Kullanım Amacı Dağılımı 
plt.figure(figsize=(12, 6))
top_uses_counts = df['Uses'].value_counts().nlargest(10)
sns.barplot(x=top_uses_counts.index, y=top_uses_counts.values, palette="rocket")
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.title('2. En Yaygın İlk 10 Kullanım Amacı', fontsize=16)
plt.ylabel('İlaç Sayısı')
plt.tight_layout()
plt.show() # Pencere 2 açılır

# -------------------------------------------------------------
# GÖRSEL 3: İnceleme Yüzdeleri Korelasyonu 
plt.figure(figsize=(7, 6))
review_cols = ['Excellent Review %', 'Average Review %', 'Poor Review %']
correlation_matrix = df[review_cols].corr()
correlation_matrix.columns = ['Exc %', 'Avg %', 'Poor %']
correlation_matrix.index = ['Exc %', 'Avg %', 'Poor %'] 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"fontsize": 12})
plt.title('3. İnceleme Yüzdeleri Arası Korelasyon', fontsize=16)
plt.tight_layout()
plt.show() # Pencere 3 açılır

# -------------------------------------------------------------
# GÖRSEL 4: Mükemmel İnceleme Dağılımı 
plt.figure(figsize=(8, 6))
sns.histplot(df['Excellent Review %'], kde=True, color='darkgreen')
plt.title('4. Mükemmel İnceleme Yüzdesi Dağılımı', fontsize=16)
plt.xlabel('Yüzde (%)')
plt.tight_layout()
plt.show() # Pencere 4 açılır

# -------------------------------------------------------------
# GÖRSEL 5: Modelin Hedef Sınıf Dağılımı 
plt.figure(figsize=(7, 7))
target_counts = df['Is_Top_Use'].value_counts()
plt.pie(target_counts, labels=['Diğer Kullanımlar (0)', 'Top 5 Kullanım Amacı (1)'], 
        autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('5. Model Hedef Sınıflarının Dağılımı', fontsize=16)
plt.axis('equal') 
plt.tight_layout()
plt.show() # Pencere 5 açılır

# -------------------------------------------------------------
# GÖRSEL 6: İsim Uzunluğu vs. İnceleme 
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['name_length'], y=df['Excellent Review %'], alpha=0.5, color='purple')
plt.title('6. İlaç Adı Uzunluğu vs. Mükemmel İnceleme Yüzdesi', fontsize=16)
plt.xlabel('İlaç Adı Uzunluğu', fontsize=12)
plt.ylabel('Mükemmel İnceleme Yüzdesi', fontsize=12)
plt.tight_layout()
plt.show() # Pencere 6 açılır


# --- 5. BASİT MODEL KURULUMU VE DEĞERLENDİRME ---

# Veri Bölme
X = df[['name_length']] 
y = df['Is_Top_Use']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modeli Kurma ve Eğitme
model = LogisticRegression()
model.fit(X_train, y_train)

# Modelin Başarısını Ölçme
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0) 
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)


# --- 6. SONUÇLARIN YORUMLANMASI İÇİN ÇIKTILAR ---
print("\n" + "=" * 50)
print("6. MODEL SONUÇLARI VE YORUMLANMASI")
print("=" * 50)
print(" MODEL PERFORMANS METRİKLERİ:")
print(f"Accuracy (Doğruluk): {accuracy:.4f}")
print(f"Precision (Kesinlik): {precision:.4f}")
print(f"Recall (Hassasiyet): {recall:.4f}")
print(f"F1 Skoru: {f1:.4f}")

# Basit Sınıf Dağılımını Gösterme (Raporlama için)
target_counts = df['Is_Top_Use'].value_counts(normalize=True) * 100
print("\n HEDEF SINIF DAĞILIMI:")
print(f"Diğer Kullanımlar (0): {target_counts.iloc[0]:.1f}%")
print(f"Top 5 Kullanım Amacı (1): {target_counts.iloc[1]:.1f}%")
print("Yorum: Accuracy, Recall, Precision ve F1 skorları düşük çıktı. Görsel 5'teki sınıf dengesizliği ve Görsel 6'daki özellik (isim uzunluğu) ile hedef arasındaki zayıf ilişki, modelin başarısızlığının ana nedenleridir.")
print("=" * 50)
print("ANALİZ TAMAMLANDI! ")
print("=" * 50)