buah=('Durian','Mangga','Rambutan','Salak','Mangga')
print("jumlah element:", len (buah))
print("Jumlah buah Mangga:",buah.count('Mangga'))

#print(type(buah))
#print (dir(buah))
#buah.append("Mangga")

buah=('Durian','Mangga','Rambutan',('Nangka','Apel'))
print("jumlah buah",buah.count("Mangga"))
print("Buah[-1] [0]:",buah[-1],[0])

x_buah = list (buah)
x_buah[0] = "Melon"
buah = tuple (x_buah)
print("Tuple:",buah)
