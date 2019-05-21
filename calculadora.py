

def decimal_binario(num_decimal):
    modulos=[]
    
    while True:
        var_guar=num_decimal//2
        var_guar2=num_decimal%2
        num_decimal=var_guar
        modulos.append(var_guar2)
        
        if var_guar<=0:
            break
    modulos_reverse=[]
    for a in reversed(modulos):
        modulos_reverse.append(a)
    
    return modulos_reverse

num_decimal=int(input("Digite su número: ")) 
var=decimal_binario(num_decimal)
print(*var)

def decimal_octal(num_decimal):
    modulos=[]
    
    while True:
        var_guar=num_decimal//8
        var_guar2=num_decimal%8
        num_decimal=var_guar
        modulos.append(var_guar2)
        
        if var_guar<=0:
            break
    modulos_reverse=[]
    for a in reversed(modulos):
        modulos_reverse.append(a)
    
    return modulos_reverse

num_decimal=int(input("Digite su número: ")) 
var=decimal_octal(num_decimal)
print(*var)

'''def decimal_hexadecimal(num_decimal):
    modulos=[]
    
    while True:
        var_guar=num_decimal//16
        var_guar2=num_decimal%16
        num_decimal=var_guar
        modulos.append(var_guar2)
        
        if var_guar<=0:
            break
    modulos_reverse=[]
    for a in reversed(modulos):
        modulos_reverse.append(a)
    
    

    num_convert=[]

    for i in modulos_reverse:
        if i==10:
            i="A"
        elif i==11:
            i="B"
        elif i==12:
            i="C"
        elif i==13:
            i="D"
        elif i==14:
            i="E"
        elif i==15:
            i="F"

        num_convert.append(i)

    return num_convert'''


num_decimal=input("Digite su número: ") 
'''var=decimal_hexadecimal(num_decimal)
print(*var)'''





def binario_decimal(num_binario):

    string=str(num_binario)
    
    potencias=[]
    for i in range(0,len(string)):
        potencias.append(2**i)
        potencias_reverse=[]
        for a in reversed(potencias):
            potencias_reverse.append(a)
    return potencias_reverse

print(binario_decimal(num_decimal))
    

'''x=int(input(print("Bienvenido, digite la opción que desee: \n 1)Traducir de decimal a binario \n 2)Traducir de decimal a octal \n 3)Traducir de decimal a hexadecimal \n 4)Traducir de binario a decimal \n 5)Traducir de binario a octal \n 6)Traducir de binario a hexadecimal \n 7)Traducir de octal a decimal \n 8)Traducir de octal a binario \n 9)Traducir de octal a hexadecimal \n 10)Traducir de hexadecimal a binario \n 11)Traducir de hexadecimal a decimal \n 12)Traducir de hexadecimal a octal")))
if x==1:
    print(prueba(num_prueba decimal))'''