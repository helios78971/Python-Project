import random

print("GAME TEBAK ANGKA\n")
print("Rulenya simpel:")
print("1. Kamu hanya perlu menyamakan angkamu dengan komputer dari -6 hingga 6")
print("2. Kalo bisa nebak 5 kali kamu hebat!")
print("3. Kalo nebak lebih dari 5 kamu lemah")

counter = 1
total_j = 0
total_k = 0
kondisi = True

while (kondisi):
    nilai = random.randint(-6, 6)
    print("\nTebakan ke-", counter)
    jawaban = int(input("Masukkan nilaimu: "))

    total_k += nilai
    total_j += jawaban

    if (total_k != total_j):
        counter += 1
        print("Total komputer: ", total_k)
        print("Total jawaban: ", total_j)
    else:
        if (counter <= 5):
            print("Kamu hebat!")
        else: 
            print("Kamu lemah!")
        kondisi = False