## Merge Sort Tekrar

def Merge(dizi):
    if len(dizi)>1:
            
        mid = len(dizi)//2
        
        sagDizi = dizi[mid:]
        solDizi = dizi[:mid]
        
        Merge(sagDizi)
        Merge(solDizi)
        MergeSort(dizi,sagDizi,solDizi)
        

def MergeSort(dizi,sagDizi,solDizi):
    i =0
    j=0
    k=0
    
    while i <len(sagDizi) and j<len(solDizi):
        if solDizi[j]<sagDizi[i]:
            dizi[k] = solDizi[j]
            j = j+1
        else :
            dizi[k]= sagDizi[i]
            i = i+1
        k = k+1
    
    while j <len(solDizi):
        dizi[k] = solDizi[j]
        k = k+1
        j=j+1
    
    while i < len(sagDizi):
        dizi[k] = sagDizi[i]
        i = i+1
        k = k+1
    
    
    
def main():
    dizi = [6,8,1,2,-10,0,500,-500,3,2,5,7,32,5,35,235,235,236,32412,4,2316,523623,-100]
    Merge(dizi)
    print(dizi)
    
    
    
    
if __name__ =="__main__":
    main()
    