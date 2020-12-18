'''
Programın İşleyişi:
1- Program Başladığı zaman önünüze bir menü gelicek;
   Bu menü de kullanabiliceğiniz özellikler
   Ürünleri Listele
   Ürün Ekle
   Ürün Sil
2-Kullanıcı Ürünleri Listelemeyi seçerse eklenen tüm ürünler kullanıcıya gösterilicek.
   Kullanıcı Ürün Ekleyi seçerse Kullanıcıdan ürün adı,fiyatı,ve kaç tane stokta bulunduğunu sormalı ve kaydetmeli.
   Kullanıcı ürün silmeyi seçerse kullanıcıdan silmek istediği ürünün numarasını isteyecek ve yazdığımızda ürün silinicek.
'''
#Program Başlıyor...
urunadilist = []
urunfiyat = []
urunStokListesi = []
UygulamaCalisiyor = True
print("****************Python ile Yazılmış Basit Stok Programı******************")
while(UygulamaCalisiyor):
 print("İşlem Listesi:\n-Ürünleri Listele\n-Ürün Ekle\n-Ürün Sil\n-Uygulamadan çıkmak için x'e basınız.")
 islem1 = input("İşlem Numarasını Giriniz:")

 # NOT: if içerisinde sayıları çift tırnak içerisinde yazmamızın nedeni input içinden gelen değerin string olmasıdır. 

 if(islem1 == "1"):
   for urun in urunadilist:
       print("-:",urun)

 elif(islem1 == "2"):
     urunadi = input("Ürünün Adını Giriniz:")
     urunfiyati = input("Ürünün Fiyatını Giriniz:")
     urunNo = input("Ürünün Stok Sayısını Giriniz:")  

     urunadilist.append(urunadi)
     urunfiyat.append(urunfiyati)     
     urunStokListesi.append(urunNo)
     print(urunNo,urunadi,"Stoğa Başarıyla Eklendi")

 elif(islem1 == "3"):
      if len(urunadilist) == 0: #len komutu lenghten geliyor ve len'in içinde yani arrayin içindeki verileri gösterir.
       print("Herhangi bir ürün bulunamadığından silme işlemi Gerçekleşmemektedir")
      else:
       sıradegiskeni = 0
       for urun in urunadilist:
        print("-",sıradegiskeni,urun)
        sıradegiskeni += 1
        urunKod = input("Silmek İstediğiniz Ürün Kodunu Giriniz:")
        urunKod = int(urunKod)
       
       urunadilist.pop(urunKod)
       urunfiyat.pop(urunKod)     
       urunStokListesi.pop(urunKod)

       print("Silmek istediğiniz ürün başarıyla silindi")

 elif islem1 == "x":
    print("Programdan Çıkış Yapılıyor...")
    break  
 else:
    print("Hatalı İşlem Numarası Girdiniz")


