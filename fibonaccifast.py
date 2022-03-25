
seq = int(input("Fibonacci değerini giriniz:"))
def FibFast():
    dizi = []
    dizi.append(0)
    dizi.append(1)
    for i in range(2,seq):
        dizi.append(i)
        dizi[i] = dizi[i-1] + dizi[i-2]
    return dizi[i]

print(FibFast())
