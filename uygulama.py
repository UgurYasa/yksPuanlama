def ders_puan():##neti ben hesaplıcam programla onun için doğru yanlış iste
    sınavlar = {"TYT":("Türkçe", "Matematik 1", "Sosyal", "Fen"),"AYT":("Matematik 2","Fizik 2","Kimya 2","Biyoloji 2")}
    katsayılar = [1.32,1.32,1.36,1.36,3,2.85,3.07,3.07]
    bölüm = input("Bölümünüzü giriniz : (1->Sayısal(MF),2->Eşit Ağırlık(TM),3->Sözel,4->Dil)--->")
    if bölüm == '2':
        sınavlar["AYT"] = ("Matematik","Edebiyat","Tarih-1","Coğrafya-1")
        katsayılar = [1.32, 1.32, 1.36, 1.36, 3, 3, 2.8, 3.33]
    elif bölüm =='3':
        sınavlar["AYT"] = ("Edebiyat", "Tarih -1", "Coğrafya -1", "Tarih -2","Coğrafya -2","Felsefe","Din Kültürü")
        katsayılar = [1.32, 1.32, 1.36, 1.36, 3, 2.8, 3.33, 2.91, 2.91, 3, 3.33]
    elif bölüm =='4':
       sınavlar["AYT"] =("İngilizce","Almanca","Arapça")
       katsayılar = [1.32, 1.32, 1.36, 1.36, 3, 3, 3]
    puanlar = {"TYT":0,"AYT":0,"YKS":0}
    i,kat = 0,0
    for sınav in sınavlar:
        for ders in sınavlar[sınav]:
                kat = katsayılar[i]
                i+=1
                print(f"{ders} dersi için ; ")
                d_sayisi=int(input("Doğru:"))
                y_sayisi = int(input("Yanlış : "))
                net = d_sayisi - (y_sayisi / 4)
                print(f"{ders} netiniz : ",net)
                dersten_gelen_puan = net*kat
                puanlar[sınav]=puanlar.setdefault(sınav,0)+dersten_gelen_puan
    okul_ortalaması = float(input("Diploma puanı : "))# Buraya Obp girme hakkı tanı
    puanlar["YKS"] = puanlar["TYT"] + puanlar["AYT"] + (okul_ortalaması*0.6) +100
    return puanlar


print(ders_puan())

