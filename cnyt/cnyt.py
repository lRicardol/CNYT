

def division(a=[],b=[]):
    parte_real=((a[0]*b[0])+(a[1]*b[1]))/(b[0]**2+b[1]**2)
    parte_imag=((b[0]*a[1])-(a[0]*b[1]))/(b[0]**2+b[1]**2)
    return (parte_real, parte_imag)
 
def multiplicacion(a=[],b=[]):
    multiplica_real=(a[0]*b[0])-(a[1]*b[1])
    multiplica_imag=(a[0]*b[1])+(b[0]*a[1])
    return (multiplica_real, multiplica_imag)
 
def suma(a=[],b=[]):
    sum_real=(a[0]+b[0])
    sum_imag=(a[1]+b[1])
    return (sum_real, sum_imag)
 
def resta(a=[],b=[]):
    res_real=(a[0]-b[0])
    res_imag=(a[1]-b[1])
    return (res_real, res_imag)
 
print(suma([3,2.8],[1.5,-2]))
print(multiplicacion([3,2.8],[1.5,-2]))
print(division([3,2.8],[1.5,-2]))
print(resta([3,2.8],[1.5,-2]))