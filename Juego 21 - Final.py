from random import sample
def contador(lista):
    if(len(lista)==0):
        return 0
    else:
        if(identificador(lista[0])=='J' or identificador(lista[0])=='Q' or identificador(lista[0])=='K'):
            return contador(lista[1:])+10
        if(identificador(lista[0])=='A'):
            return contador(lista[1:])+1
        else:
            return contador(lista[1:])+ identificador(lista[0])

def suma(lista):
    if(len(lista)==0):
        return 0
    if(contador(lista)>11):
        return contador(lista)
    else:
        if(identificador(lista[0])=='A'):
            return contador(lista)+10
        else:
            if(identificador(lista[0])=='J' or identificador(lista[0])=='Q' or identificador(lista[0])=='K'):
                return suma(lista[1:])+10
            else:
                return suma(lista[1:])+ identificador(lista[0])


def identificador(lista):
    return lista[0]

#Llena la lista con las 52 cartas y desordena la baraja    
def llenado():
    return sample([(x, y) for x in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] for y in ['Picas', 'Corazones', 'Diamantes', 'Treboles']], 52)

#retorna 2 cartas si la lista esta vacia y despues solo una
def entrega(baraja):
    return baraja[0]

def entregaTalla(player,talla,baraja):
    if(suma(player)>suma(talla)):
        return entregaTalla(player,talla+[entrega(baraja)],baraja[1:])
    else:
        if(suma(talla)<=21 and suma(talla)>=suma(player)):
            print("")
            print(">> Jugador >>")
            print(player)
            print("")
            print(">> Talla >>")
            print(talla)
            print("")
            print("La casa gana!")
            return baraja
            print("")
            print("------------------------------------------")
        else:
            print("")
            print(">> Jugador >>")
            print(player)
            print("")
            print(">> Talla >>")
            print(talla)
            print("")
            print("Usted ha ganado!")
            return baraja
            print("")
            print("------------------------------------------")


def entregaBaraja(jugador,talla,baraja):
    if(len(jugador)<=1):
        return entregaBaraja(jugador+[entrega(baraja)],talla,baraja[2:])
    else:
        if(len(talla)<=1):
            return entregaBaraja(jugador,talla+[entrega(baraja)],baraja[2:])
        else:
            return game(jugador,talla,baraja)

#Arreglar
def game(jugador,talla,baraja):
    print("")
    print(">> Jugador >>")
    print(jugador)
    print("")
    print(">> Talla >>")
    print(talla[1:])
    print("")
    print("------------------------------------------")
    if(len(jugador)==0):
        return entregaBaraja(jugador,talla,baraja)
    else:
        if(suma(jugador)<=21):
            if(input("Carta o se planta >> ")==1):
                return game(jugador +[entrega(baraja)],talla,baraja[1:])
            else:
                return entregaTalla(jugador,talla,baraja)
        else:
            print("")
            print(">> Talla >>")
            print(talla)
            print("")
            print("La casa Gana!")
            return jugador
            print("")
            print("------------------------------------------")

game([],[],llenado())

    
