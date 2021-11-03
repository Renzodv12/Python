import  string

numeros=[2,4,3,6,5,1,9,8,7,6,5,2]
np=numeros[0]
ng=numeros[0]
for n in numeros:
    if np>n:
        np=n
    if ng<n:
        ng=n
print(ng)
print(np)

letras=string.ascii_letters
print(letras)
for i in range(len(numeros)-1):
    for i in range(len(numeros)-1):
        if numeros[i]>numeros[i+1]:
            temp=numeros[i]
            numeros[i]=numeros[i+1]
            numeros[i+1]=temp



print(numeros)