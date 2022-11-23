import random
lista=['piedra','papel','tijera']
a=1
cont=0
while a>0:
    opcion=int(input(''' Juego piedra, papel, tijera
    
    elije una opcion 
    1.piedra, 2.papel, 3.tijera
    
    cual elijes: '''))

    print(random.choice(lista))

    if opcion==1 and lista[0] :
        print("Hemos empatado, resultado bot(piedra) vs tu(piedra)")
        print("Llevas ",cont," puntos")

    elif opcion==1 and lista[1]:
        print("Has perdido, resultado bot(papel) vs tu(piedra)")
        cont-=1
        print("Llevas ",cont," puntos")

    elif opcion==1 and lista[2]:
        print("Has ganado,resultado bot(tijera) vs tu(piedra)")
        cont+=1
        print("Llevas ",cont," puntos")

    elif opcion==2 and lista[0]:
        print("Has Ganado, resultado bot(piedra) vs tu(papel)")
        cont+=1
        print("Llevas ",cont," puntos")
    
    elif opcion==2 and lista[1]:
        print("Has empatado, resultado bot(papel) vs tu(papel)")
        print("Llevas ",cont," puntos")

    elif opcion==2 and lista[2]:
        print("Has perdido, resultado bot(tijera) vs tu(papel)")
        cont-=1
        print("Llevas ",cont," puntos")

    elif opcion==3 and lista[0]:
        print("Has perdido,resultado bot(piedra) vs tu(tijera)")
        cont-=1
        print("Llevas ",cont," puntos") 

    elif opcion==3 and lista[1]:
        print("Has ganado,resultado bot(papel) vs tu(tijera)")
        cont+=1
        print("Llevas ",cont," puntos")

    elif opcion==3 and lista[2]:
        print("Has empatado,resultado bot(tijera) vs tu(tijera)")
        print("Llevas ",cont," puntos")   

    terminar=int(input('''Deseas seguir jugando pulsa: 1 
Deseas acabar el juego pulsa:2
ingresa la opcion:'''))
    if terminar== 2:
        a=0
    elif terminar==1:
        a=1
        print("El total de puntos fue: ",cont)

    
    
