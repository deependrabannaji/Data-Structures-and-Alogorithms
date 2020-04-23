def selectionSort(uList):
    for a in range(0,len(uList)):
        min=uList[a]
        swp=a
        for t in range(a+1,len(uList)):
            if min > uList[t]:
                min = uList[t]
                swp = t
        if uList[swp] != uList[a]:
            temp = uList[a]
            uList[a] = uList[swp]
            uList[swp]=temp

 
                

    return uList

if __name__ == "__main__":
    ulist=[34,3,6,4,2,1,12,3]
    print(selectionSort(ulist))