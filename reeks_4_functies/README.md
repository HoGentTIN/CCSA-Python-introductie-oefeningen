In deze reeks definieer je zelf functies in Python.

Functies zijn zeer belangrijk voor zowel modulariteit als hergebruik van code. Functies definiëren in Python is zeer eenvoudig. Hieronder definiëren we een functie `hallo` met een 
default-waarde voor het argument `roepen`. Daarna wordt de functie tweemaal opgeroepen.
```python
def hallo(naam, roepen=False):
    if roepen:
        return f"HALLO, {naam.upper()}!"
    else:
        return f"Hallo, {naam}."

print(hallo("wereld"))
print(hallo("wereld", True))
```
geeft de volgende uitvoer:
```
Hallo, wereld.
HALLO, WERELD!
```

**Te lezen**:
- [Defining Functions](https://docs.python.org/3.7/tutorial/controlflow.html#defining-functions)
- [Default Argument Values](https://docs.python.org/3.7/tutorial/controlflow.html#default-argument-values)
- [Keyword Arguments](https://docs.python.org/3.7/tutorial/controlflow.html#keyword-arguments)