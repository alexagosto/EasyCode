#  EasyCode

### _PL Project based around creating a programming language that implements logic functionalities._

Run/Debug the Main.py and enjoy EasyCode. The following are possible operations and syntax that EasyCode allows you to do ordered from simplest to most complex:

### 1- **Arithmetic Commands**

    EasyCode makes full use and execution of the PEMDAS rule to keep all arithmetic equations correct. Each operation may use its preceding one in equations, so they may all be mixed and matched.
    Possible operands include:
    - Example Operand: symbol | usage examples -> console response

    - Addition: + | 5 + 5 -> 10 | 3 + 2 + 20 -> 25

    - Subtraction: - | 5 - 3 -> 2 | 20 - 10 -> 19
    (includes negatives)| 10 - 25 -> -15

    -Multiplication: * | 10 * 2 -> 20 | 10 * 3 + 2 -> 32

    -Division: / | 20 / 5 -> 4 | 2 - 10 / 2 -> 3
    (It is still not possible to divide by 0. Doing so will return an error. This includes Variables as the divisor.)

    -Exponents: ^ | 5^2 -> 25 | 10^2 -> 100

    -Parenthesis: () | (10 - 2) / 2 -> 4 | (10 - 2) ^ 2 -> 64

### 2- **Variables**

    EasyCode allows for the storing and repurposing of variables by using the VAR operand. Variables may be declared and later used for an equation, or they may be declared with an equation. Both examples are showcased below:
    >>USER INPUT
    >Terminal Response

    - Declared and used in equation
      - >> VAR a = 5
      - > 5
      - >> a
      - > 5
      - >> a * 10
      - > 50

    - Declared as part of an expression
      ->> VAR a = (10 - 2) / 2 + 26
      -> 30
      ->> (a - 2) + 32
      -> 60

    - Variables may also be used to declare other variables
      ->> VAR a = 5
      -> 5
      ->> VAR a = VAR b = VAR c
      -> 5
      ->> VAR c
      -> 5

### 3- **Logic Operands and Comparisons**

    EasyCode implements Logic operands and comparisons. Similar to other low level languages true is defined as 1 and false is defined as 0. These include:

    -LogicOp/ComparisonExpression | symbol | usage

    -Exact              | == | 5 == 5 -> 1 (true) | 2+8 == 5+5 -> 1
    -NotEquals           | != | 5 != 5 -> 0 (false)
    -LessThan           | <  | 5 < 6 -> 1 | 30<20 -> 0
    -LessThanEquals     | <= | 10 <= 10 -> 1 | 10<=20 -> 1 | 30<=20 -> 0
    -GreaterThan        | >  | 7 > 6 -> 1 | 10>20 -> 0
    -GreaterThanEquals  | >= |10 >= 10 -> 1 | 30>=20 -> 1 | 10>=20 -> 0
    -Not                | NOT| NOT 5==5 -> 0 | NOT 5==6 -> 1
    -And                | AND| 3==3 AND 2==2 -> 1 | 3==3 AND 2==1 -> 0
    -Or                 | OR | 3==3 OR 2==1 -> 1 | 3==2 OR 2==1 -> 0

### 4- **IF/THEN ELSE ELIF statements**

    Easycode has also implemented a simple if then mechanims where users can make statements with commands following the IF/THEN rule. You may use these in variable assignment too, such as:

    ->> IF 5 == 5 THEN 305
    -> 305
    ->> IF 5==6 THEN 305 ELSE 777
    -> 777
    ->> VAR age = 25
    -> 25
    ->> VAR price = IF age >= 18 THEN 40 ELSE 20
    -> 40

### 5- **FOR/WHILE LOOPS**

    Easycode implements basic for/while loops that include a step function, they must be used with the THEN operand implemented in addition 4. Later on in development lists will be added and their result will be displayed in lists. The following are some examples of the loops being used wwith some of the previous additions to the language:
    -Loop type | operand | usage
    ->> USER INPUT
    -> Terminal output

    -FOR LOOP | FOR | usage:
    ->> VAR factorial = 1
    -> 1
    ->> FOR i = 1 TO 6 THEN VAR factorial = factorial * i
    ->> factorial
    -> 120

    -FOR LOOP | FOR | negative step for loop:
    ->> VAR factorial = 1
    -> 1
    ->> FOR i = 5 TO 0 STEP -1 THEN VAR result = result * i
    ->> result
    -> 120

    -WHILE LOOP | WHILE | usage:
    ->> VAR i = 0
    -> 0
    ->> WHILE i < 100000 THEN VAR i = i + 1
    (This will simply take a bit to complete as the language has no print function yet, the print, in addition to the list function will be added later on.)

Keep in mind that the for loop is NOT inclusive, so in the first example above, it will iterate over 5 numbers, not 6.

### 6- **Functions**

    EasyCode implements Functions using the FUN keyword, this allows a user to create their own functions with the previous and following operands on this list. You can also create anonymous functions and assign them to variables
    The following are usage examples:
    - Function declaration: FUN id(value1, value2 ..., valueX) -> functionPurpose
    ->> USER INPUT
    -> Terminal output

    - Simple usage case:
    ->> FUN add(a, b) -> a + b
    -> <function add>
    ->> add(3, 10)
    -> 13

    - Applying to variable:
    ->> VAR add_func = add
    -> <function add>
    ->> add_func(1, 2)
    -> 3

    - Anonymous Function
    ->> FUN (a) -> a + 5
    -> <function <anonymous>>

    ->> VAR add_five_func = FUN (a) -> a + 5
    -> <function <anonymous>>
    ->> add_five_func(3)
    -> 8

### 7- **Strings**

    EasyCode implements very simple string functions, one may create, concatenate, multiply, and use strings in functions. The operand for string is: " "
    The following are some examples of using strings in EasyCode:

    ->> USER INPUT
    -> Terminal output

    - String usage
    ->> "This is how you create strings."
    -> "This is how you create strings."

    - String concatenation
    ->> "This is " + "string concatenation in action."
    -> "This is string concatenation in action."

    - String multiplication
    ->> "I " + "really " * 3 + "love EasyCode"
    -> "I really really really love EasyCode"

    - String + Functions
    ->> FUN greeting(person) -> "Hello, " + person + ", nice to meet you!"
    -> <function greeting>
    ->> greeting("Alex")
    -> "Hello, Alex, nice to meet you!"

### 8- **Lists**

    EasyCode implements lists using the bracket operator "[]", these lists allow the user to concatenate, append and remove items from the list by using mathematical operands. The following are the uses of mathematical operands on lists and examples of list usage.

    -  "->" terminal response
    - Example Operand: symbol | usage examples

    - List creation:   [] | [1, 2, 3] -> [1, 2 ,3]
    - Append:           + | [1, 3 , 4] + 5 - > [1, 3, 4, 5]
    - concatenate:      * | [1, 3, 2] * [4, 6, 7] -> [1, 3, 2, 4, 6, 7]
    - Remove (position) / | [1, 4, 6, 7] / 2 -> [1, 4, 7]


    Both WHILE and FOR loops have lists implemented in them to so they will display all values as a list.
    ->> FOR i = 1 TO 9 THEN 2 ^ i
    -> [2, 4, 8, 16, 32, 64, 128, 256]

### 9- **Built in Functions**

    EasyCode comes with some functions already built in that the user may call at any point, including variable assignment.

    The following is a list of included functions plus their usage example:
    ->> USER INPUT
    -> Terminal output

    # PI function:
    ->> VAR a = MATH_PI
    -> 3.141592653589793


    # Input function | INT input function
    ->> VAR name = INPUT()
    ->> Alex
    -> "Alex"
    ->> name
    -> "Alex"

    ->> VAR age = INPUT_INT()
    ->> 21
    -> 21
    ->> age
    -> 21

    ->> VAR age = INPUT_INT()
    ->> Twenty one
    -> 'Twenty one' must be an integer. Try again!


    # Clear | Clears the screen. CLS() does the same thing.
    ->> VAR age = INPUT_INT()
    ->> 21
    -> 21
    ->> age
    -> 21
    ->> CLEAR()  |Proceeds to clear the screen|


    # Check for number | Returns 1 for true 0 for false.
    ->> IS_NUM(123)
    -> 1

    ->> IS_NUM([1, 2])
    -> 0


    # Check for string | Returns 1 for true 0 for false.
    ->> IS_STR("DAD")
    -> 1

    ->> IS_STR(42)
    -> 0


    # Check for list | Returns 1 for true 0 for false.
    ->> IS_LIST(123)
    -> 0

    ->> IS_LIST([1, 2])
    -> 1


    # Check for function | Returns 1 for true 0 for false.
    ->> FUN add(a, b) -> a + b
    -> <function add>
    ->> IS_FUN(add)
    -> 1

    ->> IS_FUN(PRINT)
    -> 1

    ->> IS_FUN(57)
    -> 0


    # Append | Appends an object to a list.
    ->> VAR list = [1, 3, 5]
    -> [1, 3, 5]
    ->> APPEND(list, 7)
    -> 0
    ->> list
    -> [1, 3, 5, 7]


    # POP | Removes an element of a list by position, starts at 0.
    ->> VAR list = [1, 3, 5, 7]
    -> [1, 3, 5]
    ->> POP(list, 2)
    -> 5
    ->> list
    -> [1, 3, 7]

    # Extend | Concatenates lists.
    ->> VAR list = [1, 3, 5, 7]
    -> [1, 3, 5]
    ->> EXTEND(list, [9, 11, 13])
    -> 0
    ->> list
    -> [1, 3, 5, 7, 9, 11, 13]

    # Length | Returns a number pertaining to how long a list is.
    ->> VAR list = [1, 3, 5]
    -> [1, 3, 5]
    ->> LEN(list)
    -> 3

### 10- **Multiple statements in one line**

    EasyCode allows for multiple statements in a single line of code by using the semicolon (;) operand. This applies to all past features.
    Here is an example of this feature in action:

    # Single statement (same as before)
    ->> 1 + 2
    -> 3

    # Multiple statements
    ->> 1 + 2; 3 + 4
    -> [3, 7]

    # Multiple statements using IF statement
    ->> IF 5==5 THEN; PRINT("Statement is:"); PRINT("True") ELSE PRINT("False")
    -> Statement is:
    -> True
    -> 0

---

### 11- **Return break and continue**

    EasyCode has the functionality to use Return break and continue whithin loops and functions. This is mostly useful for expanding upon the multiple statements in a line feature.
    The following is a usage example:

    ->> USER INPUT
    -> Terminal output

    # Return whithin multi-line function
    ->> VAR a = [1, 2, 3]
    -> [1, 2, 3]
    ->> FOR i = 4 TO 10 THEN; IF i == 6 THEN CONTINUE ELIF i == 8 THEN BREAK; VAR a = a + i; END
    -> 0
    ->> a
    -> [1, 2, 3, 4, 5, 7]

---

### 12- **Functions with natural language alternative**

    EasyCode impelments a variety of commands which can be used with natural language to substitute functions and translate them to EasyCode code statements. This is mostly useful for implementing functions which should be easily human readable.

    _plus, _incrementBy, _append -> +
    _minus, _min, _substractBy -> -
    _divide, _divideBy, _removePos -> /
    _multiply, _multiplyBy, _concat -> *
    _power, _pow, _exponent, _powerOff -> ^
    _module -> %
    _exact -> ==
    _lessThan -> <
    _greaterThan -> >
    _lessThanEquals -> <=
    _greaterThanEquals -> >=
    _equal -> =
    _notEqual -> !
    _lparen -> (
    _rparen -> )
    _semicolon -> ;
    _lbracket -> [
    _rbracket -> ]
    _lcurl -> {
    _rcurl -> }
    _emptyList -> []
    _iterateFor -> FOR
    _iterateWhileUntil -> WHILE <
    _thenContinue -> THEN CONTINUE
    _afterContElif -> THEN CONTINUE ELIF
    _afterContElse -> THEN CONTINUE ELSE

---

### 13- **Run Function**

    The last function EasyCode boasts is the ability to read out files under the .ec ending with EasyCode syntax code. A file named ExampleCode.ec has been added to the project to give users an idea of how to use said feature, and how to get started on writing their own code.

    Simply run the main.py file, and type in the RUN function as follows:
    ->> RUN("ExampleCode.ec")

    With that simple command the language will read out the code you have made and give you the result.
    You're now ready to make your own EasyCode files. : )

    Thanks for using EasyCode!

---
