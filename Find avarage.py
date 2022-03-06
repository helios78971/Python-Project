umur = [2, 5, 5, 6, 7, 8, 10, 12, 4, 1, 9, 7]

umur.sort()

print("Urutan umur dari yang termuda hingga yang tertua: ", umur)

rata2 = sum(umur)/len(umur)

print("\nRata-rata umur sebelum penambahan data adalah ", rata2)

baru = int(input("\nMasukkan umur baru : "))

umur.append(baru)

print("\nUrutan umur dari yang termuda hingga yang tertua terbaru: ", umur)

rata2 = sum(umur)/len(umur)

print("\nRata-rata umur setelah penambahan data adalah ", rata2)