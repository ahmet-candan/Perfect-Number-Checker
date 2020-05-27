def mukemmel(sayı):
    
    toplam = 0
    
    for i in range(1,sayı):
        
        if (sayı % i == 0):
            toplam += i
            
    return toplam == sayı

def mukemmel2(sayi):

    
    toplam =0
    for i in range(1,sayi):
        if (sayi % i ==0):
            toplam +=i
    if ( sayi == toplam):
        print("Mükemmel Sayıdır")
    else:
        print ("Mükemmel Sayı Değildir")
            
while True:

    print("""*****************************************************************************
                         MÜKEMMEL SAYI TESPİT EDİCİ

     1-) 1'den 1000' Kadar Olan Mükemmel Sayıları Görmek İçin 1'i Tuşlayın
     2-) Girdiğiniz Sayının Mükemmel Olup Olmadığını Görmek İçin 2'yi Tuşlayın
     3-) Çıkmak İçin 3'ü Tuşlayın

    *****************************************************************************""")
    secim = int(input("Seçiminizi Girin:"))
    
    if (secim == 1):
        for i in range(1,1001):
            if (mukemmel(i)):
                print("Mükemmel Sayı:",i)
        input("Devam etmek için Enter'a basın")

    elif (secim == 2):
        a=int(input("Sayı Girin"))
        mukemmel2(a)
        input("Devam etmek için Enter'a basın")

    elif (secim == 3):
        print("Çıkış Yapılıyor")
        break
    
    else:
        print("Doğru Seçimi Yapın")
        

    
    