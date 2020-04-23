def insertionSort(uList):
    for a in range(0,len(uList)):
        for t in range(a-1,-1,-1):
            if ulist[t] > ulist[t+1]:
                temp=ulist[t]
                ulist[t]=ulist[t+1]
                ulist[t+1]=temp
            else:
                break

    return uList

if __name__ == "__main__":
    ulist=[34,3,6,4,12,1]
    print(insertionSort(ulist))

