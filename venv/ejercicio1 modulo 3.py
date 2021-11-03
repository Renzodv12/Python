# Aqui comienza lo que hice con mi logica
def fibonashi(lista, cant):
    i=len(lista)-1
    if  len(lista)==1:
        b=lista[i]+1
        lista.append(b)
        fibonashi(lista, cant)
    elif len(lista) < cant:
        b = lista[i-1] + lista[i]
        lista.append(b)
        fibonashi(lista, cant)
    else:
        print(lista)


def Fibonacci1(f, *args,cant=int()):
   if args:
       if cant > 0:
          for i in args:
            f2 = i
          f3=f
          f=f2+f
          f2=f3
          cant2=cant-1
          print(f)
          Fibonacci1(f, f2, cant=cant2)
   else:
       print(f)
       Fibonacci1(f, 1, cant=7)


def Fibonacci2(f):
   f2=0
   for i in range(8):
       if f2 == 0:
           print(f)
           f2 = 1
       else:
           f3=f
           f=f2+f
           f2=f3
           print(f)

def potencia (a,cant=int()):
    potencia=1
    if cant:
        for i in range(cant):
            potencia=potencia*a
    else:
        potencia=a*a
    print(potencia)



 #Aqui termina lo que hice con mi logica

 #Aqui comienza lo que hice con la logica del curso
def Fibonacci_recursivo(n):
    if n<=1:
        return 1
    return  Fibonacci_recursivo(n-1) + Fibonacci_recursivo(n-2)
 #Aqui termina lo que hice con la logica del curso



def main(num):


    for i in range(10):
        print(Fibonacci_recursivo(i))




if __name__=="__main__":
    main(10)
