import random

def KucukElemanBulma(dizi):
    temp=0
    for i in range(len(dizi)):
        if i==0:
            temp = dizi[i]
        
        else:
            if dizi[i]<temp:
                temp=dizi[i]
    return temp


def BuyukElemanBulma(dizi):
    temp=0
    for i in range(len(dizi)):
        if i==0:
            temp = dizi[i]
        
        else:
            if dizi[i]>temp:
                temp=dizi[i]
    return temp
    
    
            
        
        




def RandomSayiUret():
    randomSayi = random.randint(0,5000000)
    return randomSayi

def main():
    deneme =0
    a=True
    sinifGenisligi=2000000
    while a ==True:
        if sinifGenisligi > 70000:
            dizi = []
            for i in range(50):
                gecici = RandomSayiUret()
                dizi.append(gecici)
            
            kucukEleman = KucukElemanBulma(dizi)
            buyukEleman =BuyukElemanBulma(dizi)
            sinifGenisligi = (buyukEleman-kucukEleman)/len(dizi)
            deneme +=1
        else:
            print(sinifGenisligi)
            print(deneme)
            break
            

            
    
    
    
    
if __name__ =="__main__":
    main()
    