nombre="HENRRY"
x=len(nombre)
espacios=0
#hacer un triangulo invertido con el nombre "HENRRY"
for letra in nombre:
    espacios+=1
    print(" "*espacios+(letra+" ")*x)
    x-=1
