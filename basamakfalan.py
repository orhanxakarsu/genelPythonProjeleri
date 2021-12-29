
def BasamakBulma(sayi):

    sayac=False
    basamak=0
    while sayac ==False:
        if -10<sayi <10:
            basamak+=1
            sayac = True
            break
        sayi=int(sayi/10)
        basamak+=1
    return basamak

def BasamakToplamiBulma(sayi):
    toplam=0
    sayac=False
    while sayac==False:
        if 0<=sayi<10:
            toplam+=sayi
            sayac=True
            break
        else:
            toplam+=sayi%10
            sayi=int(sayi/10)
    return toplam

def main():
    sayi=-1
    while sayi !=0:
        try:
            sayi=input("Bir sayi gir -->>>  ")
            sayi = int(sayi)
            basamak=BasamakBulma(sayi)
            toplam=BasamakToplamiBulma(sayi)
            print(f"Basamak Sayısı: {basamak}\nBasamak Toplamları :{toplam}")
            if sayi ==0:
                print("""Çıkmak İstiyor musunuz ? 
                      Evetse :0
                      Hayırsa :1
                      ------>>>>  
                      """)
                son=input()
                sayi=int(son)
        except ValueError:
            print("Lütfen geçerli bir değer gir !!!!! ")
            continue
  
if __name__== "__main__":
    main()
        