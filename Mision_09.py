#Autor: Zabdiel Valentín Garduño Vivanco
#Interacción con diversas listas

def extraerPares(lista):
    listaN=[]
    for k in range(0,len(lista)):#Por cada elemento de la lista verifica si es par
        if lista[k]%2==0:
            listaN.append(lista[k])
    return listaN


def extraerMayoresPrevio(lista):#Compara los valores para analizar el mayor por pareja
    listaN=[]
    for k in range(1,len(lista)):
        if lista[k]>lista[k-1]:
            listaN.append(lista[k])
    return listaN

def intercambiarParejas(lista):
    listaN=[]

    for k in range(1,len(lista),2):#Si el numero de elementos es par entonces lo agrega a una lista nueva
        listaN.append(lista[k])
        listaN.append(lista[k-1])
    if not len(lista)%2==0:#Si el numero de elementos es impar entonces un elemento sobrante
        a=len(lista)-1
        listaN.append(lista[a])
    return listaN


def intercambiarMM(lista):
    a=0
    b=0
    c=0
    d=0
    #Se crean cuatro variables para almecenar la posición y valor del mayor y menor numero
    if len(lista)>=2:
        for k in range(0,len(lista)):
            if lista[k]==max(lista):
                a=k
                b=lista[k]
            if lista[k]==min(lista):
                c=k
                d=lista[k]
        lista[a]=d
        lista[c]=b
        return lista
    else:
        return lista



def promediarCentro(lista):
    a=0
    b=0
    for k in range(0,len(lista)):
        if lista[k]==max(lista):
            a=k
        if lista[k]==min(lista):
            b=k
    if len(lista)>=2:#El valor mayor y menor se iguala a cero y se elimina de la lista
        lista[a]=0
        lista[b]=0
        lista.remove(0)
        lista.remove(0)
        if len(lista)>=1:#Si no hay suficiente elementos solo saca el promedio
            promedio=sum(lista)//len(lista)
            return promedio
        else:
            return "0"#Si no hay elementos para promediar regresa 0
    if len(lista)<2:
        return "0"

def calcularEstadistica(lista):
    listaN=[]
    if len(lista)>=2:
        promedio=sum(lista)/len(lista)
        for x in range(0,len(lista)):#Se hace un For para almacenar las sumatorias en una lista
            listaN.append((lista[x]-promedio)**2)
        desviacion=(sum(listaN)/(len(listaN)-1))**(1/2)#Se hace la formula de desviación y se regresa.
        return (promedio,desviacion)
    if len(lista)==1:
        promedio=sum(lista)/len(lista)
        return (promedio,0)
    else:
        return (0,0)
def calcularSuma(lista):
    listaN=[]
    for k in range(0,len(lista)):#Se hace un For por cada elemento de la lista
        if lista[k]==13:#Si en dado caso existe el 13 lo almacena en una lista(las posiciones)
            listaN.append(k)
    if len(listaN)>=1:
        for x in range(0,len(listaN)):#Si la lista creada encontro el 13 elimina sus valores proximos.
            lista[listaN[x]]=0
            lista[listaN[x]-1]=0
            lista[listaN[x]+1]=0
        return sum(lista)#Regresa la lista
    if len(listaN)==0:#Si nunca hubo 13 entonces regresa la lista
        return sum(lista)

