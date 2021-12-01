# This is a comment, these are ignored.
PRINT("Welcome to EasyCode")

VAR a = 4
FOR i = 0 TO 5 THEN 
    VAR b = a - i
    PRINT("This is how to use a loop")
    PRINT("Times i will print again:")
    PRINT( a - i )
END

FUN mult(a, b) -> a * b
VAR list = [0]
PRINT(list)
FOR i = 1 TO 10 THEN 
    VAR j = i + 1
    VAR num = mult(i, j)
    list + num
    PRINT(list)
END


PRINT("The length of the list you just made is: ")
PRINT(LEN(list))

    
