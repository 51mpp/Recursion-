def staircase(n,s=""):
    #print(s)
    #print(len(s))
    if n==0:
        return "Not Draw!"
    #print(n-(len(s)//(n+1))-1,(len(s)+1)%(n+1))
    if n>0:
        if len(s)== n*n+n :
            return s
        if (len(s)+1)%(n+1) > n-(len(s)//(n+1))-1:
            s+= "#"
            #print(len(s),n)
            #print(len(s)%(n+1),n)
            #print(len(s)%(n+1) ==n)
            if len(s)==n*n+n:
                print(len(s))
                return s
            if len(s)==n :
                s+= "\n"
            elif len(s)%(n+1) == n :
                s+= "\n"
            return staircase(n,s)
        else:
            s+= "_"
            #print(len(s),n)
            #print(len(s)%(n+1),n)
            if len(s)==n*n+n:
                #print(len(s))
                return s
                #print(len(s),n)
            if len(s)==n :
                s+= "\n"
            elif len(s)%(n+1) == n and len(s)>n+1:
                s+= "\n"

        return staircase(n,s)

    else:
        x = n*-1
        if len(s)== x*x+x:
            return s
        #print((len(s)//(x+1)),(len(s)+1)%(x+1))
        if (len(s)+1)%(x+1)> (len(s)//(x+1)):
            s+= "#"
            #print(len(s),n)
            #print(len(s)%(n+1),n)
            #print(len(s)%(n+1) ==n)
            if len(s)==x*x+x:
                #print(len(s))
                return s
            if len(s)==x :
                s+= "\n"
            elif len(s)%(x+1) == x :
                s+= "\n"
            return staircase(n,s)
        else:
            s+= "_"
            #print(len(s),n)
            #print(len(s)%(n+1),n)
            if len(s)==x*x+x:
                print(len(s))
                return s
                #print(len(s),n)
            if len(s)==x :
                s+= "\n"
            elif len(s)%(x+1) == x and len(s)>x+1:
                s+= "\n"

        return staircase(n,s)
        
    


print(staircase(int(input("Enter Input : "))))
