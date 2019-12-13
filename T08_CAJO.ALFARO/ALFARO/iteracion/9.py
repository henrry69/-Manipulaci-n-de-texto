refran="Haciendo y deshaciendo se va aprendiendo"
o,m,n,p,q,r=0,0,0,0,0,0
#mostrar el numero de vocales distintas del refran "Haciendo y deshaciendo se va aprendiendo"
for letra in refran:
    if letra=="a":
        m+=1
        if m==1:
            o+=1
    if letra=="e":
        n+=1
        if n==1:
            o+=1
    if letra=="i":
        r+=1
        if r==1:
            o+=1
    if letra=="o":
        p+=1
        if p==1:
            o+=1
    if letra=="u":
        q+=1
        if q==1:
            o+=1
print(o)
