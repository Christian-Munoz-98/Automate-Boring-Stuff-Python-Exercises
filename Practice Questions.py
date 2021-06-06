#1. What are the two values of the Boolean data type? How do you write them?
'''True o False, se deben escribir en mayúsculas'''

#2. What are the three Boolean operators?
'''and, or, not'''

#3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
'''
True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False

not True = False
not False = True
'''
#4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5) #Si 5 es mayor que 4 a la vez que 3 es equivalente a 5, el resultado es falso
not (5 > 4) #Niega que 5 sea mayor a 4, el resultado es falso
(5 > 4) or (3 == 5) #Evalua si 5 es mayor que 4 o 3 equivale a 5, el resultado es Verdadero
not ((5 > 4) or (3 == 5)) #Niega que 5 es mayor que 4 o 3 es equivalente a 5, el resultado es falso
(True and True) and (True == False) #El resultado es falso 
(not False) or (not True) #El resultado es verdadero

#5. What are the six comparison operators?
'''
>
<
>=
<=
==
!=
'''

#6. What is the difference between the equal to operator and the assignment operator?
'''
El operador de asignación le otorga un valor en memoria a una variable, mientras que el de operador de equivalencia evalua si dos valors son equivalentes
'''

#7. Explain what a condition is and where you would use one.
'''
Un bloque de código que se ejecutará si se cumple una condicion que regresa un valor booleano
'''

#8. Identify the three blocks in this code:
'''
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
'''
#9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = int(input())

if spam == 1:
    print("hello")
elif spam == 2:
    print("Howdy")
else:
    print("Gretings")
#10. What keys can you press if your program is stuck in an infinite loop?
"Ctrl +C"
#11. What is the difference between break and continue?
'''
El break rompe el ciclo si una condición se cumple
El continue se salta a la siguiente iteración del ciclo desde el inicio si se cumple una condición
'''
#12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
'''
Ninguna
'''

#13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1,11):
    print(i)

i = 1

while i <= 10:
    print(i)
    i += 1


#14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

spam.bacon()