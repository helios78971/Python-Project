password = "batu bergoyang"

kunci = input("Masukkan Password: ")

while password != kunci:
    kunci = input("Password Salah! Silahkan coba lagi\nMasukkan Password: ")
else: print("Selamat! Anda berhasil Login")

print("Program Mencari Luas Kerucut")

r = float(input("Masukkan nilai r: "))
t = float(input("Masukkan nilai t: "))

kerucut = (1/3)*3.14*r*r*t

print("Luas kerucut adalah " +str(kerucut))