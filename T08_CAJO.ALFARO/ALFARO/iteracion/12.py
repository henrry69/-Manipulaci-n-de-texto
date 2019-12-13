nombre="Piero"
x=1
espacios=0
consonantes=0
#hacer un triangulo con el nombre "Piero"
for letra in nombre:
    consonantes+=1
    if x<=len(nombre):
        espacios=len(nombre)-consonantes
        print(" "*espacios+(letra+" ")*x)
    x+=1
