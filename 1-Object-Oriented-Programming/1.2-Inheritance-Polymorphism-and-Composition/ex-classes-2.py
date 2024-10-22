'''Realizar un programa que:
1. De un mensaje de bienvenida al usuario que diga "Automotores La Rueda".
2. Le de un menu de opciones en donde el usuario pueda agregar autos al sistema, ver los autos, cotizarlos o salir del sistema.
3. En caso que seleccione agregar autos, pedirle la marca, el modelo y el costo. Al ingresar el costo del mismo su valor estará en dólares. Almacenar el auto en una lista.
4. Si elije ver autos, deberá imprimir una línea con marca, modelo y costo por cada auto almacenado en la lista del punto anterior.
5. Si desea cotizar un auto, el sistema deberá pedirle el modelo del auto y calcular su precio haciendo el producto de su costo por la cotización del dólar ($185).
6. Si desea salir del sistema, se le dará un mensaje de despedida y se cerrará la ejecución del programa.
7. En caso que ingrese una opción incorrecta, informárselo y volver al menu.
'''
import os 


class Car():
    def __init__(self, brand, model, cost):
        self.brand = brand
        self.model = model
        self.cost = cost
       
    def showCar(self):
        print("Car brand: ", self.brand, "| Model: ", self.model, " | Cost: $", self.cost)
        print("")

    def quoteCar(self):
        print("The car quote ", self.brand, " ", self.model, " is: $", self.cost*185)


class CarList:
    def __init__(self):
        self.cars = []  

    def addCar(self, newCar):
        existingCar = False
        for car in self.cars:
            if car.brand == newCar.brand and car.model == newCar.model:
                print("The car entered is already on the list.")
                existingCar = True 
        if not existingCar:
            self.cars.append(newCar)
            print("The car was added successfully.")

    def showCars(self):
        if len(self.cars) == 0:
            print("The car list is empty.")
        else:
            for car in self.cars:
                car.showCar()  
    
    def findCar(self, brand, model):
         for car in self.cars:
            if car.brand == brand and car.model == model:
                return car
         print("The car entered is not in the list")

    

def showMenu():
    print("")
    print("-------------   Motor vehicles - La Rueda -  -------------")
    print("")
    print("1 - Add")
    print("2 - Show")
    print("3 - Quote")
    print("0 - Exit")

def cleanConsole():
    os.system('cls')

def addCarToList(carList):
    brand = input("Brand: ")
    model = input("Model: ")
    cost = float(input("Cost (Dolar): "))
    car = Car(brand, model, cost)
    carList.addCar(car)
    return carList

def quoteCarOfList(carList):
    brand = input("Brand: ")
    model = input("Model: ")
    car = carList.findCar(brand, model)
    if car:
       car.quoteCar()


def main():
    salir = False   
    carList = CarList()   
    print(" ")
    input("Press enter to open the menu...")
    while not salir:
        cleanConsole()  
        showMenu()
        opcion = input("  Enter an option (1-2-3-0): ")
        print("")
        match opcion:
            case '1':
                print("Add car")
                carList = addCarToList(carList)
            case '2':
                print("Show car")
                carList.showCars()
            case '3':
                print("Quote car")
                quoteCarOfList(carList)
            case '0':                
                salir = True
                print("Option chosen: Exit")
            case _:        
                print("The chosen option is not available.") 
        input("Press enter to continue...")

main() 
