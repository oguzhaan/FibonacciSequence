sayi = int(input("Sayı giriniz: "))

def Fibonacci(sayi):
    if sayi <=1:
        return sayi
    else:
        return Fibonacci(sayi-1) + Fibonacci(sayi-2)

print(Fibonacci(sayi))        