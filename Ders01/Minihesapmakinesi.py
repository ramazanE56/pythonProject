print("Hesap Makinesine Hoşgeldiniz")

num1 = float(input("İlk sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

print("Yapmak istediğiniz işlemi seçin:")
print("1: Toplama")
print("2: Çıkarma")
print("3: Çarpma")
print("4: Bölme")

choice = input("Seçiminiz (1/2/3/4): ")

if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Geçersiz giriş")