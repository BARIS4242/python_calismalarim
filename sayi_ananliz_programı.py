def sayi_analizi():
    # girdi al
    sayilar = input("Sayıları aralarına boşluk koyarak giriniz: ")
    # girilen string'i sayılara çevir
    liste = [int(s) for s in sayilar.split()]
    

# en büyük enküçük sayıyı bulma    

    print(max(liste),"sayısı listedeki en büyük sayıdır ")
    print(min(liste),"sayısı listedeki en küçük sayıdır ")
    


#tek , çift sayıları bulma
    cift=0
    tek=0
    for i in liste:
        if i%2==0:
            cift+=1
        elif i%2==1:
            tek+=1
    print(f"tek sayıların sayısı:{tek},çift sayıların sayısı:{cift}")
#ortalama hesaplama
    toplam=0
    for i in liste:
        toplam+=i
    print(f"listedeki sayıların ortalaması:{toplam/len(liste)}'dir")
        
    
sayi_analizi()    
