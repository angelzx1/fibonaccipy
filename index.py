n = int(input("Type how many terms: "))
def fibo(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("Please the integrer positive!")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
    while count < n:
        print(n1)
        nsm = n1 + n2
        n1 = n2
        n2 = nsm
        count += 1
fibo(n)
