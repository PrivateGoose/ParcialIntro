'''import math
def decimal_binario():
    decimal=int(input("Digite su número decimal: "))
    binario=""
    if decimal==0:
        print("Su número es 0.")
    else:
        while True:
            if (decimal//2==0):
                binario="0"+binario
            else:
                binario="1"+binario
                decimal=int(math.floor(decimal/2))
        
    print(binario)'''            


num_decimal=int(input("Digite su número: "))

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
        

var=decimal_binario(num_decimal)

print(*var)




'''x=int(input(print("Bienvenido, digite la opción que desee: \n 1)Traducir de decimal a binario \n 2)Traducir de decimal a octal \n 3)Traducir de decimal a hexadecimal \n 4)Traducir de binario a decimal \n 5)Traducir de binario a octal \n 6)Traducir de binario a hexadecimal \n 7)Traducir de octal a decimal \n 8)Traducir de octal a binario \n 9)Traducir de octal a hexadecimal \n 10)Traducir de hexadecimal a binario \n 11)Traducir de hexadecimal a decimal \n 12)Traducir de hexadecimal a octal")))
if x==1:
    print(prueba(num_prueba decimal))'''