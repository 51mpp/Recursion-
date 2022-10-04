
def pantip(k, n, arr, path):
    if k == 0:
        if path != [] :
            #print( str(path)[1:-1])
            print(' '.join(map(str, path)))
            global l
            l+=1
        path = []
    prev = 0
    if n < len(arr):
        if prev != arr[n]:
            path.append(arr[n])
            pantip(k - arr[n], n+1, arr, path)
            path.pop()
            prev = arr[n]
        n += 1
        
        pantip(k, n, arr, path)


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]

l =0
pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], l))
