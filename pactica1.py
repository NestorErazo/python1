""""
num = 15
print(num, type(num))

num = 15.5
print(num, type(num))

nom="nestor"
print(nom, type(nom))

boo=3==4
print(boo, type(boo))

print("esto es una suma")

num_1=2
num_2=4
result =num_1+num_2
print("La suma ",result)

print("incremento o decremento ")
x=5
print("el valor inicial de x es :",x)
x+=3
x+=4
x+=6
x+=7
print("el valo de x es  suma :",x)
""
x*=5
x*=4
x*=6
x*=8
print("el valo de x es multi:",x)


x/=5
x/=4
x/=6
x/=8
print("el valo de x es div:",x)

x=12
x//=5

print("el valor de x es div entera:",x)

x=3
x**=2
print("el valor de x es al cuadrado:",x)


x=14
x%=5

print("el valor de x es %:",x)

mensaje="hola"

mensaje+=" jose"
num=3
num+=4

print(mensaje ,"tu numero es:",num)


nombre="Hola "
nombre += input("digita tu nombre: ")
print(nombre,"este es el incremento de una variable")


print("concatenacion")
mesnsaje=" *Hola"
espacio=" "
nombre="Jose"
print(mesnsaje+espacio+nombre)

num1= 4
num2=6
result1=num1+num2
result2=str(result1)
print(result2)
print("el result 1 es :"+ result2)

print("la suma de ",num1,"+",num2,"=",result2)

print ("busqueda")

mensaje = "Hola nestor"
buscar_subCadena = mensaje.find("nestor")
print(buscar_subCadena)

print ("extraccion")
mensaje = "Hola nestor"
extraer_cadena= mensaje[1:7]

print(extraer_cadena)

if condicion_logic:
    instracion1
    
#act_1
if(True):
    print("a ingresado a la estructura de control condicional")

 #act2
 num1 == 5
 if num1==5:
     print("el numero es cinco")
     print("fin")       
     
print("Sistema para clacula el promedio de notas de una estudiante")
name = input("ingrese nombre ")
nota_1 = int(input("digitar nota 1 "))
nota_2 = int(input("digitar nota 2 "))
nota_3 = int(input("digitar nota 3 "))
prom = (nota_1+nota_2+nota_3)/3
prom = int(prom)
if prom >= 3:
    print("felicitaciones ",name,"Aprobaste Y promerdio de ",prom)
    print("fin") 

x = 6
if x==5:
   print("es 5")
else 
   print ("no es 5")
  
#sentencia condicionales compuestas 




# sentencia condicionales multiples
if condicion_logica:
    instruccion
else if condicion_logica
    instruccion
else:
    instruccion
 
x = 7
  
if x == 5:
     print("es 5")
elif x == 6 :
     print("es 6")
elif x == 7:
     print("es 7")
  

#Act 
print("******************")
print("*** conversor ***") 
print("===============")

num_1 = int(input("cual es el numero que desea convertir"))

if num_1 == 1:
    print("el numero es uno")
elif num_1 == 2:
    print("el numero es dos")
elif num_1 == 3:
    print("el numero es tres")
elif num_1 == 4:
    print("el numero es cuatro")
elif num_1 == 5:
    print("el numero es cinco")
else :
    print("el numero no esta en la lista")
print("final")      
#convertir una cadena a minusculas 
cadena ="hola MUNdo" 
#print(cadena.lower())
#convertir una cadena a mayusculas 
#print(cadena.upper())       

#convertir una cadena a minusculas y  viceversa
print(cadena.swapcase())

#convertir una cadena a formato titulo
print(cadena.title())


#act 3 menu    
print("******************")
print("*** conversor ***") 
print("===============")

print("Menus de opciones: \n")
menu = '''
print ("presiona 1 para convertir de numero a palabra")
print ("presiona 2 para convertir de palabra a numero")
    '''
print (menu)
opcion =int(input("cual es la opcion deseada  : "))
    
if opcion == 1:
        print("\n conversor de numero a palabra")
        opcion_uno= int(input("cual es el numero que desea convertir "))
        if opcion_uno == 1:
            print("el numero es 'UNO' ")
        elif opcion_uno == 2:
            print("el numero es 'DOS' ")
        elif opcion_uno == 3:
            print("el numero es 'TRES' ")
        elif opcion_uno == 4:
            print("el numero es 'CUATRO' ")
        else:
            print("el numero no esta en la lista")
if opcion == 2:
     print("\n conversor de palabra a numero")
     opcion_dos= input("cual es la palabra que desea convertir ")
     opcion_dos=opcion_dos.lower()
     if opcion_dos == 'uno':
         print("el numero es 1 ")
     elif opcion_dos == 'dos':
         print("el numero es 2 ")
     elif opcion_dos == 'tres':
         print("el numero es 3 ")
     elif opcion_dos == 'cuatro':
         print("el numero es 4 ")
     else:
         print("la palabra no esta en la lista")                         

año = 2022
evento ="semana santa"
print(f'lo mejor de las fiestas de {evento} del {año}')


flor = "rosas"
print(f'lo mejor del jarin de mi casas esta lleno {flor}')
 
                   

modelo=" Otimus Tucan"
precio = 19000000
impuesto = precio*19/100
print(f'Bicible {modelo} tiene un valor {precio+impuesto} pesos')

  
  

#act 4 validar password

print("******************")
print("*** validador de password ***") 
menu = '''
bienvenido al registro de usuario , por favor digitar la opcion que desee
acpntinuacion seleccion del 1 al 3  
[1]digitar su nombre
[2]digitar su edad
[3]digitar el correo electronico
'''

print(menu)
opcion= input("digite una opcion de 1 a 3")
if opcion == '1':
   # pass#comando de espera
    nombre=input("por favor ingresar nombre")
    if nombre.isalpha():
        print(f'nombre ingresado es {nombre}')
        # print('nombre ingresado es'+nombre)
        # print('nombre ingresado es',nombre)
        # print('nombre ingresado es{}'.format(nombre))
    else:
        print('nombre ingresado no es alfabetico')    
elif opcion == '2':
    edad=input("digite su edad ")
    if edad.isnumeric():
        print(f'edad ingresada es {edad}')
        # print('edad ingresada es'+edad)
        # print('edad ingresada es',edad)
        # print('edad ingresada es{}'.format(edad))
    else:
       print('edad ingresada no es numerica')   
    
elif opcion == '3':
    correo=input("digite su correo electronico ")
    if correo.find('@')>=0 and correo.find('.')>=0:
       print(f'su correo electronico  ingresado es {correo}')
    else:
        print('correo electronico ingresado no es valido')
else: 
    print("debes digitar un numero entre 1 y 3")
    print("**"*10)
 

  #lista de ejl 1
  
Lista = ["lunes","martes","miercoles","jueves","viernes"]
print(Lista[3])

#lista y tuplas

nums =[1,2,3,4,6]
tupla =(10,20,30,40,50)
# print(nums[2])
# print(tupla[3])
# nums[0] =100
# tupla[0] = 100
# print(nums[0])
#print(tupla[0])
nums.append(6)
print(nums)
     
mi_lista =[1,2,"hola",3.14]
print(mi_lista)  
a =[1,2,3,5,8,9]
print(a)

objeto = (7,"hola",True,3.14)
print(objeto) 
mi_tupla=(10,20,30)
print(mi_tupla)

# mi_conjunto = {1,2,3}
# print(mi_conjunto)

# mi_conjunto_1 = set()
# print(mi_conjunto_1)
   
mi_conjunto = {1,2,"jose",3.1416}


mi_conjunto.add(3)
mi_conjunto.add("hola")
mi_conjunto.add("A")
mi_conjunto.discard("A")
# mi_conjunto.clear()
print("jose" in mi_conjunto)
print(3.1416 not in mi_conjunto)

print(mi_conjunto)


#diccionarios para la app

#act 5
diccionnario = {"azul":"blue","a":"A"}
diccionnario["uno"]=1
print(diccionnario["azul"])
diccionnario["azul"]="BLUE"
del (diccionnario["a"])
print(diccionnario)


diccionnario= {"pedro":{"edad":22,"estatura":1.65},"ana":[24,1.70],"maria":[30,1.75]}

print(diccionnario["pedro"])


#ciclos for

# nums=[4,78,9,81]
# for n in nums:
#     print(n)
    
for i in range (0,5):
    print(i)
    if i ==2:
        print("ok")
        
for i in range (10,-1,-1):
    print(i)
    if i == 2 :
         print("ok")
  
#bucle infinito
x=1
while x<10:
    print(x)
    

#incrementar bucle white
x=0
while x<10:
    print(x)
    x+=1
    
     #decrementar  bucle white    
x=9
while x>0:
    print(x)
    x-=2

x=0
while x<7:
    print("nestor")
    x+=1
realizar un ciclo que permita evaluar los valores menores a 100
y que los incrementos sean de 2 en 2 y que cumplala condicion
de hacer un breack  imprime un mensaje de bucle finalizado


x =0
while x<100:
    print(x)
    x+=2
    if x>10:
      break
    print("bucle finalizado")

x  = 10
while x>0:
    print("valor de variable actual",x)
    x=x-1
    if x ==7:
        break
    print("bucle finalizado")
    

# funciones  
def nombreDeLaFuncion(valores);
    # codigo acciones o valores
    return resultado

#funcion sin parrametro 

def diHola():
    print("hola")
    

diHola()

def HolaConNombre(nombre):
    print("Hola",nombre)    
    

HolaConNombre("nestor")
    
    
def suma(a,b):
        print(a+b)
suma(3,4)


def Multi(num):
    print(f"{num}*5 = {num*5}")
    print("inicio")
    
Multi(1)
print("fin")
    
    
def Saludo(nombre):
    print(f"Hola {nombre}".format(nombre))
    
def gracias(gracias):
    print("gracias {}".format(gracias))    
Saludo("nestor")
gracias("nestor")


def suma(a,b=4):
    return a + b

def resta(a,b):
    return a - b

Ressults=suma(3)
Ressults2=resta(a=5,b=3)



def multiplica(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


#realizar un programa que capture 2 valores ,los compare y determine cual es el mayor

def mayor(a,b):
        if a>b:
            max=a    
        else:
            max=b
        return max
print("digitar primer numero")
a =int(input('por favor digitar numero 1 '))
print("digitar primer numero")
b = int(input('por favor digitar numero 2 '))

mayor= numeromayor(a,b)

print("el numero mayor es", mayor)
mayor()



#clases atributos 
metodo -- init#iniciar atributos de un objet
def __init__(self,parrametros):#constructor de la clase
    
class Nomb_clase(objeto):
    
#clase auto
class Auto:
    marca= "mazda"
    modelo="2014"
taxi = Auto()

print(taxi.marca,taxi.modelo)

class Human:
    def __init__(self, edad,nombre, ocupacion):
        self.edad = 41
        self.nombre = nombre
        self.ocupacion = ocupacion

persona_1 = Human(34,"maria","ingeniera")
print(persona_1.edad)
print(persona_1.nombre)
print(persona_1.ocupacion)
print('soy',persona_1.nombre,"mi edad es : ", persona_1.edad)


#calculadora
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def mostrar_menu():
    print("calculadora basica")
    print("1 suma")
    print("2 resta")
    print("3 multiplicacion")
    print("4 division")
    print("5 salir")

while True:
    mostrar_menu()
    opcion =input("Elija una opcion: ")
    if opcion == "5":
        print("salir del programa")
        break
    if opcion in("1","2","3","4"):

        num1 = float(input("primer numero: "))
        num2 = float(input("segundo numero: "))
        
        
    if opcion == "1":
            print("Resultado suma:", suma(num1, num2))
    elif opcion == "2":
            print("Resultado resta:", resta(num1, num2))
    elif opcion == "3":
            print("Resultado multiplicacion:", multiplicacion(num1, num2))
    elif opcion == "4":
            print("Resultado division:", division(num1, num2))
    else:
            print("Opcion no valida")
    print("Fin")


class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        
def menu():
    print("\nMenu registro de contactos:")
    print("\nMenu :")
    print("1. Agregar contacto")
    print("2. Mostrar contacto")
    print("3. Buscar contacto")
    print("4. eleminar contacto")
    print("5. Salir")

contactos = []

while True:
    menu()
    opcion = input("\n elege una opcion : ")
    
    if opcion == "5":
        print("saliste del programa :")
        break
    if opcion =="1":
        nombre = input("ingresa nombre : ")
        telefono = input("ingresa telefono :")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto)
        print("Contacto agregado correctamente : ")
        
    elif opcion == "2":
        for c in contactos:
            print(f"Nombre: {c.nombre}, Telefono: {c.telefono}")
            
    elif opcion == "3":
        nombre =input("ingresa nombre a buscar :")
        encontrado=False
        for c in contactos:
            if c.nombre == nombre:
                print(f"Nombre : {c.nombre}, Telefono : {c.telefono}")
                encontrado=True
                break
        if not encontrado:
            print("Contacto no encontrado ")
    
    elif opcion == "4":
        nombre = input("ingresa nombre a eliminar ")
        encontrado=False
        for i in range(len(contactos)):
            if contactos[i].nombre == nombre:
                del contactos[i]
                print("Contacto eliminado correctamente ")
                encontrado=True
                break
        if not encontrado:
            print("Contacto no encontrado")


num1 = 20
num2 = 0

try:
   print("la divcion entre {0} y {2} ".format(num1,num2,(num1/num2)))
   resultado = num1/num2

except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
    print("hasta aqui va el programa")
    


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
def menu():
    print("\nMenu registro de productos:")
    print("\nMenu :")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto")
    print("4. Actualiza cantidad")
    print("5. eliminar producto")
    print("6. Salir")
inventario=[]

while True:
    menu()
    opcion = input("\n elege una opcion : ")
    
    if opcion == "6":
        print("saliste del programa :")
        break
    
    if opcion =="1":
        try:
            nombre = input("ingresa nombre : ")
            cantidad = int(input("ingresa cantidad :"))
            precio = float(input("ingresa precio :"))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("Producto agregado correctamente : ")
        except ValueError:
            print("Error: Ingreso incorrecto de datos")
        
    elif opcion == "2":
         for p in inventario:
          print(f"Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
    elif opcion == "3":
        nombre = input("ingresa nombre a buscar :")
        encontrado=False
        for p in inventario:
            if p.nombre == nombre:
                print(f"Nombre : {p.nombre}, Cantidad : {p.cantidad}, Precio : {p.precio}")
                encontrado=True
                break
        if not encontrado:
            print("Producto no encontrado ")
    
    elif opcion == "4":
        nombre = input("ingresa nombre a actualizar :")
        encontrado=False
        for i in range(len(inventario)):
            if inventario[i].nombre == nombre:
                try:
                    cantidad = int(input("ingresa nueva cantidad :"))
                    inventario[i].cantidad = cantidad
                    print("Cantidad actualizada correctamente ")
                    encontrado=True
                    break
                except ValueError:
                    print("Error: Ingreso incorrecto de datos")
        if not encontrado:
            print("Producto no encontrado")
            
    elif opcion == "5":
        nombre = input("ingresa nombre a eliminar ")
        encontrado=False
        for i in range(len(inventario)):
            if inventario[i].nombre == nombre:
                del inventario[i]
                print("Contacto eliminado correctamente ")
                encontrado=True
                break
        if not encontrado:
            print("Contacto no encontrado")
             
        
        
  """      
class Work:
    def __init__(self, nombre, detalles, estado):
        self.nombre = nombre
        self.detalles = detalles
        self.estado = estado
        
        
def menu():
    print("\nMenu registro de Tareas:")
    print("\nMenu :")
    print("1. Agregar Tareas")
    print("2. Mostrar Tareas")
    print("3. Buscar Tarea")
    print("4. Actualiza Tarea")
    print("5. eliminar Tarea")
    print("6. Salir")
alamcen=[]

while True:
    menu()
    opcion = input("\n elege una opcion : ")
    
    if opcion == "6":
        print("saliste del programa :")
        break
    
    if opcion =="1":
        try:
            nombre = input("ingresa Tarea : ")
            detalles = input("ingresa detalles :")
            estado = input("ingresa estado :")
            tareas = Work(nombre,detalles,estado)
            alamcen.append(tareas)
            print("tarea agregado correctamente : ")
        except ValueError:
            print("Error: Ingreso incorrecto de datos")
        
    elif opcion == "2":
         for p in alamcen:
          print(f"Nombre: {p.nombre}, Cantidad: {p.detalles}, Precio: {p.estado}")
    elif opcion == "3":
        nombre = input("ingresa nombre a buscar :")
        encontrado=False
        for p in alamcen:
            if p.nombre == nombre:
                print(f"Nombre : {p.nombre}, Cantidad : {p.detalles}, Precio : {p.estado}")
                encontrado=True
                break
        if not encontrado:
            print("tarea no encontrado ")
            
    elif opcion == "3":
         nombre = input("ingresa nombre a buscar:")
         encontrado=False
         for p in alamcen:
             if p.nombre == nombre:
                 print(f"Nombre : {p.nombre}, Detalles : {p.detalles}, Estado : {p.estado}")
                 encontrado=True
                 break
             if not encontrado:
                 print("tarea no encontrado ")
    
    elif opcion == "4":
        nombre = input("ingresa nombre a actualizar :")
        encontrado=False
        for i in range(len(alamcen)):
            if alamcen[i].nombre == nombre:
                try:
                    detalles = input("ingresa nuevos detalles :")
                    alamcen[i].detalles = detalles
                    print("Detalles actualizados correctamente ")
                    encontrado=True
                    break
                except ValueError:
                    print("Error: Ingreso incorrecto de datos")
        if not encontrado:
            print("tarea no encontrado")
        
    elif opcion == "5":
        nombre = input("ingresa nombre a eliminar ")
        encontrado=False
        for i in range(len(alamcen)):
            if alamcen[i].nombre == nombre:
                del alamcen[i]
                print("tarea eliminado correctamente ")
                encontrado=True
                break
        if not encontrado:
            print("tarea no encontrado")