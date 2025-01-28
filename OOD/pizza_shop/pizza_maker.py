from abc import ABC, abstractmethod
from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Pizza(ABC):

    def __init__(self):
        self.description = "Base pizza" 
        self.size = Size.MEDIUM

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

class ThinCrustPizza(Pizza):
    def __init__(self, size: Size):
        super().__init__()
        self.description = "thin crust"
        self.size = size

    def get_description(self) -> str:
        return f"A {self.size.name.lower()} size pizza with {self.description}. \nToppings: \n"
    
    def cost(self) -> float:
        base_cost = 8.0
        if self.size == Size.SMALL:
            return base_cost
        elif self.size == Size.MEDIUM:
            return base_cost + 2.0
        elif self.size == Size.LARGE:
            return base_cost + 4.0

class ThickCrustPizza(Pizza):
    def __init__(self, size: Size):
        super().__init__()
        self.description = "thick crust"
        self.size = size

    def get_description(self) -> str:
        return f"A {self.size.name.lower()} size pizza with {self.description}. \nToppings: \n"
    
    def cost(self) -> float:
        base_cost = 10.0
        if self.size == Size.SMALL:
            return base_cost
        elif self.size == Size.MEDIUM:
            return base_cost + 3.0
        elif self.size == Size.LARGE:
            return base_cost + 5.0
        
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        super().__init__()
        self.pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass

class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self.pizza.get_description() + "- Cheese \n"

    def cost(self) -> float:
        return self.pizza.cost() + 1.5
    
class Pepperoni(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self.pizza.get_description() + "- Pepperoni \n"
    
    def cost(self) -> float:
        return self.pizza.cost() + 3.0
    
class Onion(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self) -> str:
        return self.pizza.get_description() + "- Onion \n"
    
    def cost(self) -> float:
        return self.pizza.cost() + 0.75