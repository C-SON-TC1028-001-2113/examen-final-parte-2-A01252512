def main():
    matriz = []
    lista_suma=[]
    renglones = int(input())
    columnas = int(input())
    for i in range(renglones):
        lista = []
        matriz.append(lista)
        for j in range(columnas):
            matriz[i].append(int(input()))
    
    for i in range(columnas):
        suma = 0
        for j in range(renglones):
            suma = matriz[j][i]+suma
        lista_suma.append(suma)
    print(lista_suma)
  




if __name__=='__main__':
    main()
