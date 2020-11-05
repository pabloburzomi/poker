import random

def sorteo_carta(): #Mezcla de mazo
  carta = []
  numero_baraja = ('AS','2','3','4','5','6','7','8','9','10','J', 'Q', 'K')
  palo_baraja = ('corazones','pica','trebol','diamante')
  x = len(numero_baraja) - 1
  y = len(palo_baraja) - 1
  numero_random = random.randint(0,x)
  palo_random = random.randint (0,y)
  carta = numero_baraja[numero_random], palo_baraja[palo_random]
  
  return carta
  

def validacion(carta): #Guarda las cartas que van saliendo
  if carta not in cartas_en_uso:
    cartas_en_uso.append(carta)
    return carta
  else:
    return False


def reparto_cartas(num): #Reparte las cartas
  #Sorteo de cartas y validacion
  if num == 1: # O se le PIDE DE A 1 CARTA...
    carta1 = sorteo_carta()
    while validacion(carta1) == False:
      carta1 = sorteo_carta()
    return carta1
  
  if num == 5: # O se le PIDE LA MANO COMPLETA
    carta1 = sorteo_carta()
    while validacion(carta1) == False:
      carta1 = sorteo_carta()
    carta2 = sorteo_carta()
    while validacion(carta2) == False:
      carta2 = sorteo_carta()
    carta3 = sorteo_carta()
    while validacion(carta3) == False:
      carta3 = sorteo_carta() 
    carta4 = sorteo_carta()
    while validacion(carta4) == False:
      carta4 = sorteo_carta() 
    carta5 = sorteo_carta()
    while validacion(carta5) == False:
      carta5 = sorteo_carta()
    su_mano = [carta1,carta2,carta3,carta4,carta5]
    return su_mano


def jugador1(su_mano): #El Rival (la computadora)
  aux = 0
  #cartas_en_uso = []
  contador_jugador1 = poker(su_mano)[0] #Los puntos del juego del contrincante
  
  cartas_iguales_jugador1 = poker(su_mano)[1] #las cartas iguales del contrincante
  
  if contador_jugador1 == 0: #Si no saco puntos en el 1er juego, se le da 5 cartas nueva para el segundo juego
    su_mano.clear()
    su_mano = reparto_cartas(5)
    print("\nLa computadora cambia las 5 cartas...")
    
  elif contador_jugador1 != 0 and contador_jugador1 < 5:
    if len(cartas_iguales_jugador1) == 6: #6 es el numero de 3 cartas iguales (3 * 2 de numero y palo)
      print("\nLa computadora cambia 2 cartas...")
    else:
      print(f"\nLa computadora cambia {5 - len(cartas_iguales_jugador1)} cartas")
    for i in range(0,len(su_mano)):
      if su_mano[i] not in cartas_iguales_jugador1:
        aux = su_mano.index(su_mano[i])
        su_mano.pop(aux)
        carta_remplazo = reparto_cartas(1)
          
        su_mano.insert(aux,carta_remplazo)#coloca carta nueva en el lugar de la carta removida
          
          
  elif contador_jugador1 >= 5: #si es igual o mayor a 5 el contrincante tiene escalera o poker
    print(f"\nLa computadora No cambia ninguna carta...")
  
  return su_mano


def cambio_carta(su_mano):#Para hacer cambio de cartas después del 1er Juego
  
  cambiar_carta = 0
  num_aRemover = int(input("\nATENCIÓN... ¿CUANTAS CARTAS DESEA CAMBIAR?, 0 para ninguna: "))
  
  print(f"\nEligio Cambiar {num_aRemover} cartas")
  
  while num_aRemover > 5:
    num_aRemover = int(input("Elija un Número de cartas válido. Usted tiene 5 cartas en su mano: "))
  if num_aRemover == 5:
    su_mano.clear()
    #cartas_en_uso = reparto_cartas()[0]
    su_mano = reparto_cartas(5) #ultimo cambio    
    num_aRemover = 0
    return su_mano
    
  while num_aRemover > 0:
    cambiar_carta = int(input("Presione 1 para cambiar la primer carta, 2 para la segunda y asi..."))
    while cambiar_carta > 5:
      cambiar_carta = int(input("Presione un número valido. Usted tiene sólo 5 cartas en la mano"))
    cambiar_carta -= 1 #para sincronizar la ubicacion que elije con el indice de la lista
    su_mano.pop(cambiar_carta)#elimina carta de la mano
    carta_remplazo = reparto_cartas(1)#saca nueva carta del mazo
    su_mano.insert(cambiar_carta,carta_remplazo)#coloca carta nueva en el lugar de la carta removida
    num_aRemover -=1#contador
  return su_mano


def poker(la_mano):#Chequea si hay juego
  cartas_iguales = []
  contador = 0
  aux = []
  aux2 = 0
  #Chequea juegos (salvo escalera) 
  for i in range (0,len(la_mano)):
    for j in range(i+1,len(la_mano)):#va descartando la que ya considero
      if la_mano[i][0] == la_mano[j][0]: #El [0] es para que tome en cuenta solo los números de las cartas y no el palo
          if la_mano[i] not in cartas_iguales:
            cartas_iguales.append(la_mano[i])
          if la_mano[j] not in cartas_iguales:  
            cartas_iguales.append(la_mano[j])
          contador += 1
  
  if contador == 0:
    #Chequea Escalera
    numero_baraja = ('AS','2','3','4','5','6','7','8','9','10','J', 'Q', 'K')
    lista_aux = []
    for i in range(0,len(la_mano)):
        lista_aux.append(la_mano[i][0])  
        aux.append(numero_baraja.index(lista_aux[i])) #El aux guarda el indice en el que se encuentra cada una de las cartas de la mano, en numero_baraja
    aux.sort()
    
    aux2 = aux[0]  #Guarda el primer indice de la mano en el que hubo coincidencia con numero_baraja
    for i in range (0,len(lista_aux)):
      if (aux2 + i) == aux[i]:
        contador += 1

    if contador != 5:#Para cuando el AS vale 13
      if aux2 == 0:
        aux2 = aux[1]
        for i in range (0,len(lista_aux) - 1):
          if (aux2 + i) == aux[i + 1]:
              contador += 1
    if contador != 5:
      contador= 0
  return contador, cartas_iguales, aux


def puntos(contador,cartas_iguales):# Chequea los puntos de poker()
  if contador == 0:
    print(f"\nNo ha sacado juego...")
  elif contador == 1:
    print(f"\nHa sacado PAR de {cartas_iguales[0][0]}: {cartas_iguales}")
  elif contador == 2:
    print(f"\nHa sacado PAR de {cartas_iguales[0][0]}, y PAR de {cartas_iguales[2][0]}")
  elif contador == 3:
    print(f"\nHa sacado tres {cartas_iguales[0][0]}: {cartas_iguales[0]}, {cartas_iguales[1]}, {cartas_iguales[2]}")
  elif contador == 4:
    print(f"\nHa sacado full!!!")
  elif contador == 5:
    print("\n¡¡Ha obtenido ESCALERA!!")
  elif contador >= 6: # 6 es el número de 4 cartas iguales, Y 10 de 5 
    print("Ha obtenido POKER!!!!")
  return None


def Ganador(resultado_jugador, resultado_rival): #Quien ganó la partida
  contador,cartas_iguales,carta_mas_alta = resultado_jugador
  contador_rival,cartas_iguales_rival,carta_mas_alta_rival = resultado_rival
  numero_baraja = ('AS','2','3','4','5','6','7','8','9','10','J', 'Q', 'K')
  if cartas_iguales != [] and cartas_iguales_rival != []:
    if contador == contador_rival:
      aux_jugador = []
      aux_rival = []
      for i in range(0,len(cartas_iguales)):
        aux_jugador.append(numero_baraja.index(cartas_iguales[i][0]))
        aux_rival.append(numero_baraja.index(cartas_iguales_rival[i][0]))
      aux_jugador.sort()
      aux_rival.sort()

  if contador_rival > contador:
    print ("\n\n\nTu oponente gana la partida...\n\n")
  elif contador_rival < contador:
    print ("\n\n\nHas ganado la partida...!!!\n\n")
  else:
    if contador_rival == contador and contador_rival != 0:
      ganador_conJuego(aux_jugador,aux_rival)
    else:
      if carta_mas_alta[0] == 0 and carta_mas_alta_rival[0] != 0: #0 es el AS
        print("\nTu ganas por tener la carta mas alta (un AS)...")
      elif carta_mas_alta[0] != 0 and carta_mas_alta_rival[0] == 0:
        print("\nTu oponente gana por tener la carta mas alta (un AS)...")
      else:
        ganador_sinJuego(cartas_iguales,cartas_iguales_rival)
  return None

def ganador_conJuego(aux_jugador,aux_rival):
  
  if contador_rival == 1 and cartas_iguales[0][0] != cartas_iguales_rival[0][0]:
    if aux_jugador[0] == 0 or aux_rival[0] == 0: #Si alguno tiene un AS
      if aux_jugador[0] == 0:
        print("Tu ganas")
      else:
        print("La computadora gana")
    elif aux_jugador[0] > aux_rival[0]:
      print("\nHas ganado la partida!")
    elif aux_jugador[0] < aux_rival[0]:
      print("\nLa computadora gana...")
  elif contador_rival == 2: #Si los dos jugadores tienen dos pares de juegos
    if aux_jugador[3] > aux_rival[3]:
      print("\nTu ganas")
    elif aux_jugador[3] < aux_rival[3]:
      print("\nLa computadora gana...")
    else:
      if aux_jugador[0] > aux_rival[0]:
        print("\nTu ganas")
      elif aux_jugador[0] < aux_rival[0]:
        print("\nLa computadora gana...")
  elif contador_rival == 3:
    if aux_jugador[0] > aux_rival[0]:
      print("\nTu ganas")
    elif aux_jugador[0] < aux_rival[0]:
      print("\nLa computadora gana...")

def ganador_sinJuego(cartas_iguales,cartas_iguales_rival):
    #Si ninguno tiene juego, ni ases
    if carta_mas_alta_rival[4] > carta_mas_alta[4]:
      print(f"\n\n\nTu oponente gana por tener la carta mas alta...")
    elif carta_mas_alta_rival[4] < carta_mas_alta[4]:
      print(f"\n\n\nTu ganas por tener la carta mas alta...")
    else:
      if carta_mas_alta_rival[3] > carta_mas_alta[3]:
        print(f"\n\n\nTu oponente gana por tener la segunda carta mas alta...")
      elif carta_mas_alta_rival[3] < carta_mas_alta[3]:
        print(f"\n\n\nTu ganas por tener la segunda carta mas alta...")
      else:
        if carta_mas_alta_rival[2] > carta_mas_alta[2]:
          print(f"\n\n\nTu oponente gana por tener la tercer carta mas alta...")
        elif carta_mas_alta_rival[2] < carta_mas_alta[2]:
          print(f"\n\n\nTu ganas por tener la tercer carta mas alta...")




#Programa Principal
cartas_en_uso = []


#Repartir de cartas
print("La computadora ya recibió sus cinco cartas...")
mano_jugador1 = reparto_cartas(5) #Mano del programa
su_mano = reparto_cartas(5)  #Mano del jugador
print (f"\nTu juego por ahora es:\n\n {su_mano}")

#Primer Juego
poker(su_mano)[0] 
juego_contrincante = jugador1(mano_jugador1)

#Cambio de Cartas
su_mano = cambio_carta(su_mano) 
print ("\n\nTU JUEGO: ",su_mano)

#Segundo Juego
resultado_jugador = poker(su_mano)
contador,cartas_iguales,carta_mas_alta = resultado_jugador
puntos(contador,cartas_iguales)


#Mostrar cartas y ver los juegos
print(f"\nEl juego de la computadora es {juego_contrincante}")
resultado_rival = poker(juego_contrincante)
contador_rival,cartas_iguales_rival,carta_mas_alta_rival = resultado_rival
puntos(contador_rival,cartas_iguales_rival)

#Ganador

Ganador(resultado_jugador,resultado_rival)



""""
print(f"\n\n\nLas cartas que se usaron en esta partida son {len(cartas_en_uso)} -- {cartas_en_uso}")
"""

