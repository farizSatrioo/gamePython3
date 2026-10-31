import random

print("=" * 35)
print("       GAME TEBAK ANGKA")
print("=" * 35)

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("\nSaya sudah memilih angka dari 1 sampai 100.")
print("Bisakah kamu menebaknya?")
print("Ketik angka 0 untuk keluar.\n")

while True:
    try:
        tebakan = int(input("Masukkan tebakan: "))

        if tebakan == 0:
            print("Kamu keluar dari permainan!")
            break

        if tebakan < 1 or tebakan > 100:
            print("Masukkan angka antara 1 sampai 100!")
            continue

        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil! Coba lagi.\n")

        elif tebakan > angka_rahasia:
            print("Terlalu besar! Coba lagi.\n")

        else:
            print("\nSELAMAT! TEBAKAN KAMU BENAR!")
            print("Angka rahasianya:", angka_rahasia)
            print("Jumlah percobaan:", percobaan)
            break

    except ValueError:
        print("Masukkan angka yang benar!\n")

print("\nTerima kasih sudah bermain!")
