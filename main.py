from random import  randint
import os
personajes=["Goku", "Saitama","Desconocido","X"]
vida =[randint(90,150),randint(90,150),randint(90,150),randint(90,150)]
ataque_especiales=["Kamehameha","Onepunch", "Golpe desconocido","Corte X"]
jugador1=None
jugador1id=None
jugador2id=None
jugador1vidainicial=None
jugador2vidainicial=None
jugador1vidaactual=None
jugador2vidaactual=None
jugador2=None
resp=0

def prueba(jugadornum1,jugadornum1id, jugadornum2,jugadornum2id):
    input("Elige tu ataque\n"
          "1. Golpe\n"
          "2. Patada\n"
          "3. {}\n".format(ataque_especiales[jugadornum1id-1]))


def vidabaja(id, ataque, jugador1vidaactual):
    if (id==1):
        jugador1vidaactual=jugador1vidaactual-ataque




while ((jugador2==None and jugador1==None) or ((jugador1id<0 or jugador1id>4) and (jugador2id<0 or jugador2id>4))):
    if (jugador1==None or jugador1id<0 or jugador1id>4):
        jugador1id=int(input("Jugador1 Elije un personaje del 1 al 4 \n"
                            "1.{}\n"
                            "2.{}\n"
                            "3.{}\n"
                            "4.{}\n".format("Goku","Saitama","Desconocido","X")))
        jugador1=personajes[jugador1id]
        jugador1vidainicial=vida[jugador1id]
        jugador1vidainicial=jugador1vidaactual
    if (jugador2 == None or jugador2id < 0 or jugador2id > 4):
        jugador2id= int(input("Jugador2 Elije un personaje del 1 al 4 \n"
                        "1.{}\n"
                        "2.{}\n"
                        "3.{}\n"
                        "4.{}\n".format("Goku", "Saitama", "Desconocido", "X")))
        jugador2 = personajes[jugador2id-1]
        jugador2vidainicial = vida[jugador2id-1]
        jugador2vidainicial = jugador2vidaactual
    while(resp!=1):
        resp=int(input("Estas listo para luchar?\n"
                       "1. Si\n"
                       "2 No\n"))
        input("eNTER")
        os.system("cls")
        comienza=randint(1,2)
        if comienza==1:
            print("Comienza Jugador1")
            prueba(1,jugador1id,2,jugador2id)
        else:
            print("Comienza Jugador2")
            prueba(2,jugador2id,1,jugador1id)








