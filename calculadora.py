#!C:\Users\zx19student140\AppData\Local\Microsoft\WindowsApps\python.exe

print("Content-Type: text/plain\n")

import cgi 

args = cgi.parse()

a = int(args['num1'][0])
b = int(args['num2'][0])
o = int(args['oper'][0])

eva = {
    1:'Suma',
    2:'Resta',
    3:'Multiplicacion',
    4:'Division'
}

def ope():
    if o == 1: return a + b
    elif o == 2: return a - b
    elif o == 3: return a * b
    elif o == 4: return a / b
    else: print('Error de operación')

print('La ', eva[o] ,' entre ' , a , ' y ' , b , ' es igual a ' , ope())