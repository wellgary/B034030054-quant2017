def multiplication_table(m, n):
    for j in range(1,10):
        for i in range(m,n+1):
            if i*j<10:
                print(('%s x %s = %s '% (i,j,j*i)),end="  ")
            else:
                print(('%s x %s = %s'% (i,j,j*i)),end="  ")
        print("")
    print("")

def pyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i) + (i*2-1)*"*")
