

def GCD(n1,n2):
    if n1<0:
        n1 = n1*-1
    if n2<0:
        n2 = n2*-1
    if n1==0:return n2
    if n2==0: return n1
    if n1>n2:
        return GCD(n1%n2,n2)
    else:
        return GCD(n1,n2%n1)




lst = list(map(int, input("Enter Input : ").split(' ')))

if lst[0] ==0 and lst[1] ==0:
    print("Error! must be not all zero.")
elif lst[0] <0 and lst[1] <0:
    if lst[0]>lst[1]:
        print("The gcd of",lst[1],"and",lst[0],"is :",GCD(lst[0],lst[1]))
    else:
        print("The gcd of",lst[0],"and",lst[1],"is :",GCD(lst[0],lst[1]))

else:
    if lst[0]>lst[1]:
        print("The gcd of",lst[0],"and",lst[1],"is :",GCD(lst[0],lst[1]))
    else:
        print("The gcd of",lst[1],"and",lst[0],"is :",GCD(lst[0],lst[1]))

