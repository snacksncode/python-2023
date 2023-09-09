## Zadania na 24 czerwca


### Zadanie A


liczby całkowite: 
- dodatnie
- ujemne 
- zera

np

a = [1,0,-1,-1,0,2,5,0,-2]

można wykonywać "operacje" (0 lub więcej razy)
- wybieramy pewien przedział tej tablicy/listy, i zamieniamy wszystkie
  liczby w tym przedziale na ich ujemne wartości...

czyli np. wybierając przedział zawierający [-1,-1,0,2,5] (z listy "a"), 
zamieniamy go na [1,1,0,-2,-5]


-------------------
napisać funkcję
```
def get_min_number_of_operations(a: list[int]) -> int
```

która wyliczy ile minimalnie tych operacji trzeba wykonać, by dostać tablicę
z liczami wyłącznie >=0

- przykłady:
a = [1,0,-1,-1,0,2,5,0,-2],    	--> 2
a = [-1, 1, -1],    			--> 2
a = [-1, 1, 2, 3],    			--> 1
a = [-1, 0, -1],    			--> 1
a = [-1, 1, -1, 1, -1, 1, -1],  --> 4
a = [1, -1,-2,-3,-4],  			--> 1
