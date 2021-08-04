print("PENCARIAN KATA")
inputan = input("Masukkan Kata: ")

with open('Artikel.txt', 'r') as fopen :
  txt = fopen.read()
  count = txt.count(inputan)

if inputan in txt:
  print("Kata", inputan, "ditemukan sejumlah", count)
else:
  print("Maaf tidak ditemukan kata ", inputan)