# Ciic4030-Project
### *PL Project based around creating a python like programming language that implements logic functionalities.*

Debug/Run the Main.py and enjoy EasyCode. The following are possible operations and syntax that EasyCode allows you to do ordered from simplest to most complex:

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
    ->> FOR i = 1 TO 6 THEN VAR result = result * i
    ->> result
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
    d




___

The following is a log of progress on the language, starting at earliest development and
TODO 
11/28/2021:
Currently the code will take an input and using a lexer and a parser creates intermediary code based around mathematical equations and with PEMDAS in mind.
The code in its current state will not run any code as it has no iterpreter. That is the following process. 

11/29/2021:
    Code now has working interpreter and can process variables, code works as follows:
    > VAR a = 5
    > 5
    > a
    > 5
    > a ^ 2
    > 25 
    > VAR a = a * 2
    > 10
    > a 
    > 10

Next Readme update will catalogue adding logical operators to the language.
