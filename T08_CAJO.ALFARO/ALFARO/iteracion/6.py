palabra="consultorio"
m,n,p,q,r=0,0,0,0,0
#mostrar la vocales de la palabra consultorio sin repetirlas
for letra in palabra:
    if letra=="a":
        m+=1
        if m==1:
            print(letra)
    if letra=="e":
        n+=1
        if n==1:
            print(letra)
    if letra=="i":
        r+=1
        if r==1:
            print(letra)
    if letra=="o":
        p+=1
        if p==1:
            print(letra)
    if letra=="u":
        q+=1
        if q==1:
            print(letra)
