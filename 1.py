def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if fibonacci(numero):
    print("O número pertence à sequência de Fibonacci!")
else:
    print("O número não pertence à sequência de Fibonacci.")
