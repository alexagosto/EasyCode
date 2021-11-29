# # Imports for parser
# import sys
# sys.path.insert(0, "../..")
# import ply.yacc as yacc
# # v this import gives us tokens from each line of code 
# from Lexer import tokens 

# # Made to hold tuples
# names = {}
# # Int to know how many indents/spaces were used in file. 
# spaces = 0

# # Intermediate code location
# f = open('D:\\Programming stuff\\VSC\\PL4030 Project\\test.py','w')

# #
# # The following lines of code will declare operands
# # for token names that will be used in intermediate code,
# # This will include math, prints, attributes, among others.
# #
# # Simple ones will not be explained, complex operands will
# # have a comment explaining what they do. 
# #


# # Helping operands to clean up and error check intermediate code.
# def indent ():
#     global spaces 
#     for i in range(0, spaces):
#         f.write("\t")

# def variable_verify():
#     if names[id]:
#         return names[id]
#     print("Variable " + id + " is not in system.")

# def p_error(p):
#     print("Syntax error by user, check syntax and try again.")


# def p_expression_plus(p):
#     'expression : expression PLUS term' 
#     indent()
#     f.write(str(p[1]) + " + " + str(p[3]) + "\n")
#     print ("p_expression_add") 


# def p_expression_minus(p):
#     'expression : expression MINUS term' 
#     indent()
#     f.write(str(p[1]) + " - " + str(p[3]) + "\n")
#     print ("p_expression_minus") 


# def p_expression_times(p):
#     'expression : expression TIMES term' 
#     indent()
#     f.write(str(p[1]) + " * " + str(p[3]) + "\n")
#     print ("p_expression_times") 


# def p_expression_db(p):
#     'expression : expression DIVIDEDBY term' 
#     indent()
#     f.write(str(p[1]) + " / " + str(p[3]) + "\n")
#     print ("p_expression_db") 


# def p_expression_equals(p):
#     'expression : ID EQUALS expression' 
#     indent()
#     f.write(str(p[1]) + " = " + str(p[3]) + "\n")
#     print ("p_expression_equals") 


# def p_expression_att(p):
#     'expression : ID ATTRIBUTE ID EQUALS term'
#     f.write(str(p[1]) + " . " + str(p[3]) + " = " + str(p[5]) + "\n")

# def p_expression_display(p):
#     'expression : DISPLAY factor'
#     f.write(str(p[1]) + " " + str(p[2]) + "\n")

# def p_for(p):
#     'expression : FOR ID BETWEEN term AND term'
#     indent()
#     global spaces
#     spaces = spaces + 1
#     f.write("for " + str(p[2]) + " in range(" + str(p[4]) + "," + str(p[6]) + ") :" + "\n")

# def p_condition_while(p):
#     'condition : WHILE' 
#     p[0] = p[1]

# def p_condition_if(p):
#     'condition : IF'
#     p[0] = p[1]

# def p_condition_else(p):
#     'condition : ELSE'
#     p[0] = p[1]

# def p_condition_gt(p):
#     'expression : condition term GREATERTHAN term'
#     indent()
#     f.write(str(p[1]) + " " + str(p[2]) + " >= " + str(p[4]) + " :" + "\n")
#     global spaces
#     spaces = spaces + 1

# def p_condition_lt(p):
#     'expression : condition term LESSTHAN term'
#     indent()
#     f.write(str(p[1]) + " " + str(p[2]) + " <= " + str(p[4]) + " :" + "\n")
#     global spaces
#     spaces = spaces + 1

# def p_condition_exact(p):
#     'expression : condition term EXACT term'
#     indent()
#     f.write(str(p[1]) + " " + str(p[2]) + " == " + str(p[4]) + " :" + "\n")
#     global spaces 
#     spaces = spaces + 1

# # End of syntax analysis. 
# def p_expression_end(p):
#     'expression : END'
#     f.close()
#     sys.exit()


# # Following operands convert inputs of other operands.
# def p_term_ID(p):
#     'term : ID'
#     p[0] = p[1]
#     print("p_expression_ID")


# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
#     print('p_expression_term')


# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
#     print("p_term_factor")


# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]
#     print("p_term_num")


# def p_factor_expr(p):  
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]
#     print ("p_factor_expr")
    

# # End of converting operands.



# # Used to change indents/spaces of next line. 
# def p_endblock(p):
#     'expression : ENDBLOCK'
#     p[0] = p[1]
#     global spaces
#     spaces = spaces - 1 



# # Generate Parser. 
# parser = yacc.yacc() 
