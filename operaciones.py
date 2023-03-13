def sumar(a, b): 
    # if((a==int or a==float) and(b==int or b==float)):
        return (a + b)

def restar(a ,b):
    # if((a==int or a==float) and(b==int or b==float)):
        return (a-b)



def multiplicar(a ,b):
    # if((a==int or a==float) and(b==int or b==float)):
        return (a*b)
    

a=float(input("Introduce el numero 1: "))
b=float(input("Introduce el numero 2: "))

print(sumar(a,b))
print(restar(a,b))
print(multiplicar(a,b))