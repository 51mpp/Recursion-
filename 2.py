def length(txt):     
    #Code Here
    global x
    try:
        x+=1
    except:
        x=1
    
    s =txt[0]
    txt = txt[1:]
    if x %2 ==1:
        m = "*"
    else:
        m = "~"
    if txt != "":
        return s+m + length(txt)
    else:
        return s+m

print(length(input("Enter Input : ")),sep="")
print(x)

#txt = input("Enter Input : ")
#print(length(txt))