from pizza_maker import *

if __name__ == "__main__":
    # my_pizza = ThickCrustPizza(Size.LARGE)
    # my_pizza = Cheese(my_pizza)
    # my_pizza = Pepperoni(my_pizza)
    # my_pizza = Onion(my_pizza)

    pizza_done = False 
    
    while not pizza_done:
        size = int(input("Wich size do you want? \n  1. Small \n  2. Medium \n  3. Large \n"))
        crust_type = int(input("Which pizza crust do you want? \n  1. Thin Crust \n  2. Thick Crust \n"))

        if size == 1:
            size = Size.SMALL
        elif size == 2:
            size = Size.MEDIUM
        elif size == 3:
            size = Size.LARGE
        #else to deal with wrong inputs

        if crust_type == 1:
            my_pizza = ThinCrustPizza(size)
        elif crust_type == 2:
            my_pizza = ThickCrustPizza(size)
        #else to deal with wrong inputs
        
        n = 0
        while n < 2:
            toppings = int(input("Choose your toppings (Max = 2): \n  1. Cheese \n  2. Pepperoni \n  3. Onion \n  0. Exit \n"))
            
            if toppings == 1:
                my_pizza = Cheese(my_pizza)
                n += 1
            elif toppings == 2:
                my_pizza = Pepperoni(my_pizza)
                n += 1
            elif toppings == 3:
                my_pizza = Onion(my_pizza)
                n += 1
            elif toppings == 0:
                pizza_done = True
                break
   
        print(f"\nPizza description: \n- {my_pizza.get_description()}")
        print(f"Cost: ${my_pizza.cost()}.")
        pizza_done = True