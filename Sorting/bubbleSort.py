def bubbleSort(uList):
    for a in range(0,len(uList)):
        for t in range(0,len(uList)-1-a):

            if uList[t] > uList[t+1]:
                temp = uList[t]
                uList[t] = uList[t+1]
                uList[t+1]=temp       

    return uList

if __name__ == "__main__":
    ulist=[34,3,6,4,2,1,12,3]
    print(bubbleSort(ulist))