Een aantal oefeningen waarin je zelf een klasse moet definiëren. Hieronder een eenvoudig voorbeeld van een klasse:
```python
class Dog:
    dogCount = 0;
    def __init__(self, name):  ## Constructor heeft de naam  __init__
        self.name = name
        self.tricks = [] # Alle truukjes die *deze* hond kent
        Dog.dogCount += 1 # Verhoog het *totaal* aantal honden   
    
    def add_trick(self, trick):
        self.tricks.append(trick)
        
    def bark(self):
        return "woof woof"
```
Deze klasse kan je bv. als volgt gebruiken:
```python
d = Dog('Fido')
e = Dog('Nero')
d.add_trick('roll over')
d.add_trick('play dead')
print(d.name) # Drukt af: "Fido"
print(d.tricks) # Drukt af:  ['roll over', 'play dead']
print(d.bark()) # Drukt af: "woof woof"
print(Dog.dogCount) # Drukt af: "2"
```

**Te lezen:**

- [A first look at classes](https://docs.python.org/3.7/tutorial/classes.html#a-first-look-at-classes)