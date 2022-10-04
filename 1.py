def Min(n,lst,mIN = None):
    #print(mIN)
    #print(n+1 == len(lst))
    if n+1 == len(lst):
        mIN = int(lst[n])
    if n <0:
        return mIN
    else:

        if int(lst[n])< mIN:
            mIN = int(lst[n])
        #print("sfksf")
        return Min(n-1,lst,mIN)







lst = input('Enter Input : ').split(' ')
print("Min : ",end="")
print(Min(len(lst)-1,lst))