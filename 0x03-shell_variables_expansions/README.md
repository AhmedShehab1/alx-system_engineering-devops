#alias : used to simply rename commands to be used more efficiently 
Syntax
alias [-p] [name=‘value’]

#Echo : 
used for various purposes however in this context used to print to standard output and the $ is used for expansion

#Export :
A variable that is exported is said to be environment variable this means that it will also be accessed by sub-shells
In the context of our script we use this to define a new directory in the PATH variable where the system searches for command to execute 

#tr 
Used in the script to replace the : colon with a new line in order to be able to effectively use the wc command to directly count the no. Of directories in the $PATH variable 

A script to create a local variable is straight and forward but don’t forget that it’s not allowed to start the variable name with a digit

By using the the expansion ‘$’ and providing the environment variable BINARY using the following syntax
echo $((2#BINARY))
This 2 before the # indicates that the following # no. Is binary [base#]n 

%s is a format specifier that represents string thus formatting the output .\n is an escape sequence that represent a new line character to be able to represent each combination of two digits in an independent line the -v option in Grep command (global regular expression print ) is used to exclude a given argument in this case the combination ‘oo’
#!/bin/bash

Here the %f is a format specifier used to display floating values in normal conditions it displays 6 floating values for that we restricted the floating points to two by writing .2 before ‘f’ 
clear
