import time
i = 0
asal_sayilar = [2,3]

while True:
    #time.sleep(0.5)
    i+=6
    denetleyici_1=0
    denetleyici_2=0
    if 1==1:
        for asal_sayi in asal_sayilar:
            if (i-1) % asal_sayi == 0:
                denetleyici_1=1
                break
        if denetleyici_1 ==0:
            print(f"{i-1} asal sayıdır")
            asal_sayilar.append(i-1)
        if (i+1) % asal_sayi ==0 :
                denetleyici_2=1
        for asal_sayi in asal_sayilar:
            if (i+1) % asal_sayi ==0:
                denetleyici_2 = 1
                break
        if denetleyici_2 == 0:
            print(f"{i+1} asal sayıdır")
            asal_sayilar.append(i+1)
                
                