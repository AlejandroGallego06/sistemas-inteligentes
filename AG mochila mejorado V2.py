## CREADO Versión inicial NDD Sept 2020
## Modificaciones posteriores

import random
import numpy as np


"""   Comentarios son Una Linea: #
O triple comilla doble: Un bloque"""

"""Si se desea una población inicial no aleatoria

cromosoma1 = [1, 0, 0, 0, 1]
cromosoma2 = [0, 1, 0, 0, 0]
cromosoma3 = [1, 1, 0, 0, 1]
cromosoma4 = [1, 1, 1, 0, 1]
poblInicial = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4]

"""

# MEJORA: Tamaño de la Población como parametro 
#random.seed(1)
#print("\n","aletorio:", random.randrange(2)) #Entero 0 o 1

##### FUNCIONES PARA OPERADORES


def evalua(n,x,poblIt,utilidad,pesos):
    suma=0
    total=0
    fitness = [0] * n  # Inicializamos la lista de fitness con ceros
    peso = [0] * n      # Inicializamos la lista de pesos con ceros
    pesoTotal=0
    for i in range(0, n):
      for j in range(0,x):
        suma+=poblIt[i,j]*utilidad[j]
      fitness[i]=suma
      total+=suma
      suma=0
    
    for i in range(0, n):
        for j in range(0,x):
            pesoTotal+=poblIt[i,j]*pesos[j]
        peso[i]=pesoTotal
        pesoTotal=0
    
    # if peso[i]>15:
    #     fitness[i]=0
    
    return fitness,total,peso

def imprime(n,total,fitness,poblIt,peso):
    #Tabla de evaluación de la Población
    acumulado= np.empty((n))
    acumula=0
    print ("\n",'Tabla Iteración:',"\n")
    for i in range(0, n):
      probab=fitness[i]/total
      acumula+=probab
      print([i+1]," ",poblIt[i],"  ",fitness[i]," ",peso[i]," ","{0:.3f}".format(probab)," ","{0:.3f}".format(acumula))
      acumulado[i]=acumula
    print("Total Fitness:      ", total)
    return acumulado

def seleccion(acumulado):
    escoje=np.random.rand()
    print("escoje:      ", escoje)
    
    for i in range(0,n):
      if acumulado[i]>escoje:
         padre=poblIt[i]
         break

    
    return (padre)
    
    

def cruce(a1,p1,p2):
    if a1<Pcruce:
        print("Mas grande", Pcruce, "que ", a1, "-> Si Cruzan")
        Pcorte = random.random() #Punto de corte
        print("Punto de corte: ", Pcorte)
        if Pcorte <= 0.33:
            temp1=p1[0:1]
            temp2=p1[1:4]
            print(temp1,temp2)
            temp3=p2[0:1]
            temp4=p2[1:4]
            print(temp3,temp4)
            hijo1 = list(temp1)
            hijo1.extend(list(temp4))
            hijo2 = list(temp3)
            hijo2.extend(list(temp2))

        elif Pcorte <= 0.66:
            temp1=p1[0:2]
            temp2=p1[2:4]
            print(temp1,temp2)
            temp3=p2[0:2]
            temp4=p2[2:4]
            print(temp3,temp4)
            hijo1 = list(temp1)
            hijo1.extend(list(temp4))
            hijo2 = list(temp3)
            hijo2.extend(list(temp2))
        elif Pcorte <= 1:
            temp1=p1[0:3]
            temp2=p1[3:4]
            print(temp1,temp2)
            temp3=p2[0:3]
            temp4=p2[3:4]
            print(temp3,temp4)
            hijo1 = list(temp1)
            hijo1.extend(list(temp4))
            hijo2 = list(temp3)
            hijo2.extend(list(temp2))
           
        #   temp1=p1[0:3] #[i:j] corta desde [i a j)
        #   temp2=p1[3:6]
        #   print(temp1,temp2)
        #   temp3=p2[0:3]
        #   temp4=p2[3:6]
        #   print(temp3,temp4)
        #   hijo1 = list(temp1)
        #   hijo1.extend(list(temp4))
        #   hijo2 = list(temp3)
        #   hijo2.extend(list(temp2))

    else:
      print("Menor", Pcruce, "que ", a1, "-> NO Cruzan")
      hijo1=p1
      hijo2=p2
    
    return hijo1,hijo2

def mutacion(hijo):
    for i in range(0, x):
        a2 = np.random.rand()
        # print("Mutacion en gen ", i, "con probabilidad" , a2)
        if a2<Pmuta:
            print("Mutacion en gen ", i)
            if hijo[i]==0:
                hijo[i]=1
            else:
                hijo[i]=0
    return hijo  
      
    
#### Parametros #####
x=4  #numero de variables de decision - Elementos diferentes: x
n=4  #numero de individuos en la poblacion - cromosomas: n
Pcruce=0.98  #Probabilidad de Cruce
Pmuta=0.1   #Probabilidad de Mutación


fitness= np.empty((n))
# acumulado= np.empty((n))
suma=0
total=0

#Individuos, soluciones o cromosomas 
#poblInicial = np.random.randint(0, 2, (n, x)) # aleatorios (n por x) enteros entre [0 y2)
#random.random((4,5)) # 4 individuos 5 genes
cromosoma1 = [0, 1, 0, 0]
cromosoma2 = [0, 0, 0, 0]
cromosoma3 = [0, 0, 0, 1]
cromosoma4 = [0, 1, 1, 0]
poblInicial = np.array([cromosoma1, cromosoma2, cromosoma3, cromosoma4])

# Ingresar los datos del Problema de la Mochila - Peso y Utilidad de los Elementos
pesos = [7, 6, 8, 2]
utilidad = [4, 5, 6, 3]
#pesos = [5, 7, 10, 30, 25]
#utilidad = [10, 20, 15, 30,15]

print("Poblacion inicial Aleatoria:","\n", poblInicial)
print("\n","Utilidad:", utilidad) 
print("\n","Pesos", pesos )   
poblIt=poblInicial

######  FIN DE LOS DATOS INICIALES



##Llama función evalua, para calcular el fitness de cada individuo
fitness,total,peso=evalua(n,x,poblIt,utilidad,pesos)
#####print("\n","Funcion Fitness por individuos",  fitness)
#####print("\n","Suma fitness: ",  total)

##### imprime la tabla de la iteracion
imprime(n,total,fitness,poblIt,peso)
acumulado= imprime(n,total,fitness,poblIt,peso)
print("Acumuladooooooo: ", acumulado)
##### ***************************************
# Inicia Iteraciones

# Crear vector de 5x2 vacio  a = numpy.zeros(shape=(5,2))
for iter in range(100):
  print("\n","Iteración ", iter+1)
  
  for i in [0,2]:  ## Para el bloque de 2 hijos cada vez
    papa1=seleccion(acumulado) # Padre 1
    print("padre 1:", papa1)
    papa2=seleccion(acumulado) # Padre 2
    print("padre 2:", papa2)
    
    hijoA,hijoB=cruce(np.random.rand(),papa1,papa2)
    print("hijo1: ", hijoA)
    poblIt[i]=hijoA
    print("hijo2: ", hijoB)
    poblIt[i+1]=hijoB

    hijoA=mutacion(hijoA)
    print("hijo1 mutado: ", hijoA)
    poblIt[i]=hijoA
    hijoB=mutacion(hijoB)
    print("hijo2 mutado: ", hijoB)
    poblIt[i+1]=hijoB
    
  print("\n","Poblacion Iteración ", iter+1,"\n", poblIt)
  fitness,total,peso=evalua(n,x,poblIt,utilidad,pesos)
  #### print("\n","Funcion Fitness por individuos",  fitness)
  #### print("\n","Suma fitness: ",  total)

  ##### imprime la tabla de la iteracion
  imprime(n,total,fitness,poblIt,peso)
    