import re

def cariKata():
  print("PENCARIAN KATA")
  inputan = input("Masukkan Kata: ")
  
  with open('Artikel.txt', 'r') as fopen :
    txt = fopen.read()
    count = txt.count(inputan)

  if inputan in txt:
    print("Kata", inputan, "ditemukan sejumlah", count)
  else:
    print("Maaf tidak ditemukan kata ", inputan)


def gantiKata():
  print("PENGGANTIAN KATA")
  inputan = input("Masukkan Kata: ")
  ginput = input("Kata Ganti: ")

  with open('Artikel.txt', 'r') as fopen :
    txt = fopen.read()

    if inputan in txt:  
      txt = txt.replace(inputan, ginput)
      with open('GArtikel.txt', 'w') as fout:
        fout.write(txt)
      print("Berhasil")
    else:
      print("Maaf tidak ditemukan kata",inputan)


def urutKata():
  print("PENGURUTAN KATA")
  lkata = []
  with open('Artikel.txt', 'r') as fopen :
    for line in fopen:
      extract = '[a-zA-Z]+'
      temp = re.findall(extract, line)

      for kata in temp:
        lkata.append(kata.upper())
    lkata.sort()

  with open('UArtikel.txt', 'w') as fout:
    lkata = list(dict.fromkeys(lkata))
    for kata in lkata:   
      fout.write(kata)
      fout.write('\n')
    print("Berhasil")


def main():
  print("1. PENCARIAN KATA\n2. PENGGANTIAN KATA\n3. PENGURUTAN KATA")
  pilih = int(input("Pilihan: "))

  if pilih == 1:
    cariKata()
  elif pilih == 2:
    gantiKata()
  elif pilih == 3:
    urutKata()
  else:
    print("Masukkan pilihan angka")
    return main()

if __name__ == "__main__":
  main()