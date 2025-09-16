# Fibonaccigetallen

De manier waarop de rij van Fibonacci gedefinieerd is, is een voorbeeld van wat in de wiskunde een **recursieve definitie** genoemd wordt. De rij begint met 0 en 1 en vervolgens is elk volgend element van de rij steeds de som van de twee voorgaande elementen. Het $n$-de getal van Fibonacci $F_n$ wordt zo gegeven door:

$$F_0 = 0,\ \ \ F_1 = 1$$

en

$$F_n = F_{n-1} + F_{n-2}$$

voor $n > 1$.


Het begin van de reeks is dus

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …

### Opgave

Schrijf een recursieve functie `fib` waaraan een getal $n \in \N$ moet doorgegeven worden. De functie moet het $n$-de Fibonaccigetal $F_n$ teruggeven.  

### Voorbeeld

```
>>> fib(0)
0
>>> fib(1)
1
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3

```