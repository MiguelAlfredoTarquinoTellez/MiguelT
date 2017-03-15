print('~Problema en donde se tienen 3 numeros flotantes y los suma')
a = 1.2
b = 3.2
c = 4.5
print(a + b + c)
print('----------------------------------------------------------')
print('')
print('~Imprime si un numero es mayor a 1000, menor a 500 o un numero entre 500 a 1000')
a = 654
if(a > 1000):
    print('Numero mayor a 1000')
elif(a > 500):
    print('Numero mayor a 500 y menor a 1000')
elif(a < 500):
    print('Numero menor a 500')   
print('----------------------------------------------------------')
print('')
print('~Saber el area de un triangulo')
a=5
b=6
r=(a*b)/2
print ("El area del Triangulo es" +str (r))
print('----------------------------------------------------------')
print('')
print('~La hipotenusa de un triangulo con b = 2 y h = 2')
a = 2
b = (a**2) + (a**2)
raiz = b ** 0.5
print(raiz)
print('----------------------------------------------------------')
print('')
print('~saber si una cadena de texto tiene la palabra arbol consecutivamente')
a = 'ndlanldkarbolooinos'
b = len(a)
rsp = 0
for i in range(0,b,1):
    if(a[i]=='a'):
        c = i       
if(a[c]=='a'):
    x = c+1
    if(a[x]=='r'):
        x = x+1
        if(a[x]=='b'):
            x = x+1
            if(a[x]=='o'):
                x = x+1
                if(a[x]=='l'):
                    rsp = 1
if(rsp == 1):
    print('La cadena "'+a+'" tiene la palabra arbol consecutivamente')
else:
    print('La cadena "'+a+'" no tiene la palabra arbol consecutivamente')                                          
print('----------------------------------------------------------')
print('')
print('~Saber cuantos numeros pares hay en una cadena de texto')
a = "a,2,c,s"
contar = 0
for  i in a:
    try:
        k = int(i)
        g = k % 2 
        if(g == 0):  
            contar = contar + 1
    except:
        c = 1
print(contar)                    