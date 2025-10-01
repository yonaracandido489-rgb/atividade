num1= float(input("digite o primeiro numero:"))
num2= float(input("digite o segundo numero:"))
if num2 !=0 :
    if num1 % num2 ==0:
        print(f "{num1} e divisivel por {num2}")
    else:
        print(f "{num1} nao e divisivel por {num2}")
    else:print(" nao e possivel dividir por zero")