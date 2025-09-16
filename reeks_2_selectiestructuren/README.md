Hier ga je aan de slag met selectiestructuren in Python.  

Naast de klassieke `if .... elif .... elif .... else` structuur kan je af en toe ook eens gebruikmaken van de ternaire operator:
```python
antwoord = "OK" if controle_getal == 0 else "Fout"
```

Complexe condities kunnen samengesteld worden m.b.v. de `and`, `or` en `not` sleutelwoorden.

Tot slot kan de `in` operator handig zijn. In plaats van
```python
if x == "steen" or x == "hagedis":
```
kan je ook schrijven 
```python
if x in ["steen", "hagedis"]:
```

**Te lezen:** [`if` Statements](https://docs.python.org/3.7/tutorial/controlflow.html#if-statements)
