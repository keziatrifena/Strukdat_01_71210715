def pilihan():
    print("Pilih menu")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

print(pilihan())
ch = input("Pilihan Anda: ")
while ch != "Q":
    if ch == "1":
        kal1 = int(input("Masukkan angka pertama: "))
        kal2 = int(input("Masukkan angka kedua: "))
        print("hasil:", kal1+kal2)
        ch = input("Pilihan Anda: ")
    if ch == "2":
        kal1 = int(input("Masukkan angka pertama: "))
        kal2 = int(input("Masukkan angka kedua: "))
        print("hasil:",kal1-kal2)
        ch = input("Pilihan Anda: ")
    if ch == "3":
        kal1 = int(input("Masukkan angka pertama: "))
        kal2 = int(input("Masukkan angka kedua: "))
        print("hasil:",kal1*kal2)
        ch = input("Pilihan Anda: ")
    if ch == "4":
        kal1 = int(input("Masukkan angka pertama: "))
        kal2 = int(input("Masukkan angka kedua: "))
        print("hasil:",kal1/kal2)
        ch = input("Pilihan Anda: ")
    else:
        break
