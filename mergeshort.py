

def Merge(dizi):
    print("Bölünen dizi : "+str(dizi))
    if len(dizi) >1 : # Çünkü 1 elemana ulaştığında ayırmış oluyoruz.
        mid = len(dizi)//2
        
        solDizi = dizi[:mid]
        sagDizi = dizi[mid:]
        
        Merge(solDizi)
        Merge(sagDizi)
        MergeSort(dizi,solDizi,sagDizi)
        

def MergeSort(dizi,solDizi,sagDizi):# Burada da sıralama yapacağız.
    
    #Sol dizinin indisini tutan değişkene ihtiyacımız var
    i =0
    #Sağ dizinin indisini tutan değişken:
    j=0
    #Elemanları birleştirip aktardığımız değişkenin indisini tutan değişken:
    k =0
    
    while i < len(solDizi) and j < len (sagDizi):
        if solDizi[i]< sagDizi[j]:
            dizi[k]=solDizi[i]
            i = i+1
        else :
            dizi[k]=sagDizi[j]
            j = j+1
        k = k+1
    while i < len(solDizi):
        dizi[k]=solDizi[i]
        i = i+1
        k = k+1
    while j < len(sagDizi):
        dizi[j]=sagDizi[j]
        j = j+1
        k = k+1
    
    print(f"Birleştirilmiş dizi : {dizi}")
        




import random
dizii = []
for a in range(10):
    dizii.append(random.randint(0,500000))
Merge(dizii)
print(f"Birleştirilmişadsa dizi : {dizii}")
