class Animal:
    name = ''
    
    def eat(self):
        print('Я могу поесть')
        
    class Dog(Animal):
        def display(self):
            print('Меня зовут' self.name)
            
    def eat(self):
        super().eat()
        print('Я могу поесть')
        
    Collei=Dog()
    Collei.name = 'Max'
    print(Collei.__dict__)
    Collei.display()
    Collei.eat()