sayi = input("Bir sayı giriniz: ")

bas1 = int(sayi[0]) ** 4
bas2 = int(sayi[1]) ** 4
bas3 = int(sayi[2]) ** 4
bas4 = int(sayi[3]) ** 4

toplam = bas1 + bas2 + bas3 + bas4

kosul = bool(int(sayi) == toplam)

print(kosul)