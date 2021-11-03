def string_larga(*args):
    string = ""
    cant=0
    for i in args:
        if len(i)>cant:
            cant=len(i)
            string=i
    return string


def suma_list(*args):
    suma=0
    for i in args:
        suma=suma+i
    return suma
def es_impar(num):
    if num % 2 != 0:
        return True
    else:
        return False


print(string_larga("pruebassssssssssssssssssssssssssssfgkjfjhfjhfjhfhjss","asasasssssssssssa", "asasas"))
print(suma_list(1,2,3,4,5))
print(es_impar(12))


a = open("prueba.txt","w")
a.write("hola mundo tengo sueño")
a.close()
