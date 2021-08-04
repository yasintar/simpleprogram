import re

print("PENGURUTAN KATA")
lkata = []
with open('Artikel.txt', 'r') as fopen :
  for line in fopen:
    extract = '[a-zA-Z]+'
    temp = re.findall(extract, line)
    # temp = line.split() #ada koma2nya
    for kata in temp:
      lkata.append(kata.upper())
  lkata.sort(key=str.casefold)

with open('UArtikel.txt', 'w') as fout:
  lkata = list(dict.fromkeys(lkata))
  for kata in lkata:   
    fout.write(kata)
    fout.write('\n')
  print("Berhasil")