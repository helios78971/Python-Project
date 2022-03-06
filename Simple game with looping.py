import random

print("Tebak Dadu")
print("Rulenya simple:")
print("1. Kamu punya 3 nyawa")
print("2. Tebak dadu sebanyak mungkin")

score = 0
nyawa = 3
kondisi = True

while kondisi:
  x = random.randint(1, 6)
  print("\nNyawa: ", nyawa)
  print("Score: ", score)
  angka = int(input("Masukan angka dadu: "))

  if (x == angka):
    score += 1
    print("Hebat! Tebakan kamu benar")

  else:
    nyawa -= 1
    print("Tebakan kamu benar-benar salah!")
  
  if (nyawa == 0):
    kondisi = False
    print("\nNyawa: ", nyawa)
    print("Score: ", score)
    print("\nGAME OVER")