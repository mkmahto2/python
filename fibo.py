def fiboIte(n):
    prevnum=0
    currentnum=1
    for i in range(1,n):
        prevprevnum = prevnum
        prevnum = currentnum
        currentnum = prevnum + prevprevnum
    return currentnum



def fiboRec(n):
    if n==0:
        return 0
    elif(n==1):
        return 1
    else:
        return fiboRec(n-1) + fiboRec(n-2)


if __name__ == "__main__":
    num = int(input("enter a number"))
    print(f"using recursion the value of fib({num}) is {fiboRec(num)}")
    print(f"using recursion the value of fib({num}) is {fiboIte(num)}")
#during the problem, the recursive take more time to calculate the fibonacci series. as iteration take less time to calculate.
