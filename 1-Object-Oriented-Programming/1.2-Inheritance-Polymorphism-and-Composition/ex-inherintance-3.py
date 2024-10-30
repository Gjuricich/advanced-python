'''Crear un programa en python que:
1. De un mensaje de bienvenida que indique "Ferretería La Tuerca"
2. Le permita al usuario ingresar productos en cuatro categorías: Artículos de ferretería, artículos de electricidad, Herramientas y  Máquinas.
3. Todos los productos deberán tener un código, un nombre y un precio y se podrá acceder a esta información mediante un método.
4. Los artículos tendrán un número de stock y un método que nos indique "Debe Comprar" si el mismo menor  a 100.
Si el artículo es de electricidad deberá poseer además el dato de tensión y se deberá poder acceder a un método que defina si es de baja tensión (menos a 48V) o no.
5. Las herramientas deberán tener un rubro (electricidad, construcción, plomería, etc).  Se deberá poder acceder a un método que informe el rubro al que pertenece.
6. Las máquinas deberán tener un valor de potencia y deberemos poder acceder a un método que nos indique "Es de consumo alto" si la potencia es superior a los 2500W.
8. Cada vez que se ingrese un producto en el sistema, se deberán ejecutar todos los métodos correspondientes a su categoría.
'''
import os 

class Product():
    def __init__(self, cod, name, price):
        self.cod = cod
        self.name = name
        self.price = price
   
    def showInfo(self):
        print("The product ", self.name," cod ", self.cod, "has a price of $", self.price)

    def callMethods(self):
        self.showInfo()

class Tool(Product):
    def __init__(self, cod, name, price, category):
        Product.__init__(self, cod, name, price)
        self.category = category
   
    def getCategory(self):
        print("The tool", self.name, "has the category ", self.category)
    
    def callMethods(self):
        self.showInfo()
        self.getCategory()

class Machine(Product):
    def __init__(self, cod, name, price, power):
        Product.__init__(self, cod, name, price)
        self.power = power

    def showInfo(self):
        print("The product ", self.name," cod ", self.cod, "has a price of $", self.price, " and power of ", self.power, "w.")
    
    def checkPower(self):
        if(self.power>2500):
            print("the machine -", self.name, "- has a power(",self.power,"w) consumption - high -")

    def callMethods(self):
        self.showInfo()
        self.checkPower()
    
class Item(Product):
    def __init__(self, cod, name, price, stock):
        Product.__init__(self, cod, name, price)
        self.stock = stock
    
    def showInfo(self):
        print("The product ", self.name," cod ", self.cod, "has a price of $", self.price, " and stock of ", self.stock, "u.")
    
    def checkStock(self):
        if(self.stock<100):
            print("The item", self.name, "has less than 100 in stock. You must reestablish the available stock.")
        else:
            print("The item", self.name,"is available in stock.")

    def callMethods(self):
        self.showInfo()
        self.checkStock()

class IronmongeryItem(Item):
    def __init__(self, cod, name, price,stock):
        Item.__init__(self, cod, name, price,stock)    
    
    def callMethods(self):
        self.showInfo()

class ElectricityItem(Item):
    def __init__(self, cod, name, price, stock, voltage):
        Item.__init__(self, cod, name, price,stock)
        self.voltage = voltage

    def showInfo(self):
        print("The product ", self.name," cod ", self.cod, "has a price of $", self.price, ", stock of ", self.stock, "u and voltage ", self.voltage, "V.")
    
    def checkVoltage(self):
        if(self.voltage<48):
            print("The voltage in ", self.name,"is lower to 48V")

    def callMethods(self):
        self.showInfo()
        self.checkVoltage()

###############            Class ProductList          ####################### 
class ProductList():
    
    def __init__(self):
        self.productList = []  
 
    def productExists(self, code):
        existingProduct = False
        for product in self.productList:
            if product.cod == code:                
               existingProduct = True 
        return existingProduct  
      
    def addStockToProduct(self,code,stock):
        item = Item("","",0,0)
        for product in self.productList:
            if product.cod == code:   
                product.stock += stock
                print("The stock product was added successfully.")
                product.callMethods()             

    def addProduct(self, option):  
        product = Product(0,"","")  
        code = input("Code: ")

        if self.productExists(code):
            if option == "3" or option == "4":
                print("The product entered is already on the list.")
                return
            else: 
               stock = int(input("Add stock: "))
               self.addStockToProduct(code,stock)
        else:
            name = input("Name: ") 
            price = float(input("Price: "))
            if option == "1":
                stock = int(input("Stock: "))
                product = IronmongeryItem(code,name, price, stock) 
            elif option == "2":
                stock = int(input("Stock: "))
                voltage = int(input("Voltage: "))
                product = ElectricityItem(code, name, price, stock, voltage)
            elif option == "3":
                category = input("Category: ") 
                product = Tool(code, name, price, category)
            else:
                power = int(input("Power: "))
                product = Machine(code, name, price, power)

            self.productList.append(product)
            print("The product was added successfully.") 
            product.callMethods()
            
###############            Globals functions          ####################### 
def showMenu():
    print("")
    print("-------------   IronMongery -  La Tuerca -  -------------")
    print("")
    print("1 - Add Ironmongery Item")
    print("2 - Add Electricity Item")
    print("3 - Add Tool")
    print("4 - Add Machine")
    print("0 - Exit")

def cleanConsole():
    os.system('cls')

def main():
    salir = False   
    products = ProductList() 
    print(" ")
    input("Press enter to open the menu...")
    while not salir:
        cleanConsole()  
        showMenu()
        option = input("  Enter an option (1-2-3-4-0): ")
        print("")
        match option:
            case '1':
                print("Add Ironmongery Item")
                products.addProduct(option)      
            case '2':
                print("Add Electricity Item")
                products.addProduct(option) 
            case '3':
                print("Add Tool")
                products.addProduct(option) 
            case '4':
                print("Add Machine")         
                products.addProduct(option)   
            case '0':                
                salir = True
                print("Option chosen: Exit")
            case _:        
                print("The chosen option is not available.") 
        input("Press enter to continue...")

main() 

