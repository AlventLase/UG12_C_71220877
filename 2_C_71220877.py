angka = int(input("Masukkan angka :"))
hit = int(input("Masukkan angka yang dihitung :"))
sum = 0
for b in angka:
    if b == hit:
        sum +=1
print(sum)
