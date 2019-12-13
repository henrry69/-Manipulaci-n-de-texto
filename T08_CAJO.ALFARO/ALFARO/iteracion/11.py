refran="Más vale prevenir que lamentar"
vocales=""
#mostrar las vocales en una sola linea
for letra in refran:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        vocales+=letra+" "
print(vocales)
