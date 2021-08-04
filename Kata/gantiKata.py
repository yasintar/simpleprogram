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