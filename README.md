# 📄 PDF Birleştirici (Python PDF Merger)

Bu uygulama, birden fazla PDF dosyasını tek bir dökümanda birleştirmek için geliştirilmiş, **Tkinter** tabanlı, kullanıcı dostu bir masaüstü aracıdır.

---

## ✨ Özellikler

* **Toplu Dosya Seçimi:** Birden fazla PDF dosyasını tek seferde arayüze ekleyebilirsiniz.
* **Sıralı Birleştirme:** Dosyaları ekleme sıranıza göre `PyPDF2` motoru ile birleştirir.
* **Dosya Kaydetme:** Birleştirilen dosyayı dilediğiniz isimle ve klasöre kaydetme imkanı sunar.
* **Hata Yönetimi:** Geçersiz dosya veya birleştirme hatalarına karşı kullanıcıyı bilgilendiren uyarı pencereleri içerir.

---

## 🛠 Teknik Mimari

Proje, Python'un güçlü kütüphanelerini kullanarak nesne yönelimli (OOP) mantığıyla kodlanmıştır:



* **Tkinter:** Uygulamanın grafik arayüzünü ve dosya seçim pencerelerini yönetir.
* **PyPDF2 (PdfMerger):** PDF verilerini okuma, arka planda birleştirme ve yeni dosya oluşturma işlemlerini gerçekleştirir.

---

## 🚀 Kurulum ve Çalıştırma

1.  Gerekli kütüphaneyi bilgisayarınıza yükleyin:
    ```bash
    pip install PyPDF2
    ```
2.  Uygulamayı çalıştırın:
    ```bash
    python pdf_merger.py
    ```

---

## 📋 Nasıl Kullanılır?

1.  **PDF Ekle:** Butona basarak birleştirmek istediğiniz dosyaları seçin.
2.  **Listeyi Kontrol Et:** Seçilen dosyalar ekrandaki listede görüntülenecektir.
3.  **Birleştir ve İndir:** Butona tıkladıktan sonra dosyanın kaydedileceği konumu seçin ve işlemi tamamlayın.
