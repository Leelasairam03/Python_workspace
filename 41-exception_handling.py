'''
types of error:
1.Syntax error
-errors that occur by violating the grammar of the language
-programmer has to correct them only then the program will start executing

Example:print"hello world"-error


2.Runtime error
-errors that occur during the execution of the program
-programmer can't correct them unless he provide some logic to handle them

Example:
-end user input
-unavailable resource
-invalid operations etc
such type of errors are called as exceptions

normal flow of python execution:
-python will execute instructions one after another
-executes successfully and output is as per our expectation


abnormal flow:
-an exception will occur
-execution will stops abruptly
-the below code or instructions will not get executed

example:
a=10
b=0
c=a/b  #zero division error
print(c)

output:
    ZeroDivisionError: division by zero

to overcome such type of errors we have to use exception handling

Exception- 
    an unwanted/unexpected event that disrupts the normal flow of the program
    whenever exception occurs program execution stops abnormally,hence we need to handle these exceptions on high priority

Exception handling
    it does not mean repairing or correcting the exception,instead,it is a process in which we define a way,so that the program does not terminate abnormally due to exceptions
    highly recommended to use try,except block for handling exceptions
    main objective is graceful termination of program or resume normal flow of program

syntax:
try:
    #risky code/statements
except ExceptionType:
    #handling code/statements

try block:
-try is a keyword in python
-the code which may rise an exception should be written inside the try block

except block:
-except is keyword
-the corresponding handling code for the exception,if occured needs to be written inside the except block

Exception hierarchy:
-built in exceptions are arranged in a hierarchy
-all exceptions are derived from the base class 
-base class for all exceptions is 

BaseException
    |__>SystemExit
    |__>KeyboardInterrupt
    |__>GeneratorExit
    |__>Exception
        |__>ArithmeticError
            |__>ZeroDivisionError
            |__>OverflowError
            |__>FloatingPointError
            |__>ComplexWarning
        |__>AssertionError
        |__>AttributeError
        |__>EOFError
        |__>ImportError
            |__>ModuleNotFoundError
        |__>LookupError
            |__>IndexError
            |__>KeyError
        |__>NameError
            |__>UnboundLocalError
        |__>TypeError
        |__>OSError
            |__>FileNotFoundError
            |__>PermissionError
            |__>UnsupportedOperationError
            |__>FileExistsError
        |__>StopIteration
        |__>ValueError   

default Exception Handling:
in python for every exception there is a default exception handler which will execute if the exception is not handled by the programmer

Default exception handler:
    when an exception occurs and if it is not handled by the programmer,the default exception handler will execute
    it will print the exception type and the exception message
    then the program will terminate

case 1: 1) exception not occurred
        try:
            #risky code
        except ExceptionType:
            #handling code

        except block not executed

        2) exception occurred and handled
        try:
            #risky code
        except ExceptionType:
            #handling code

        except block will execute
        then normal flow continues
        expected name of the error should be provided in the except block

        3) exception occurred and not handled

        except block not present
        default exception handler will execute(pvm will create an exception/error object)
        program will terminate abnormally

        4)try block statement will be skipped from the point of exception

        5)what if exception occurs in the except block,program will terminate abnormally

        6)if exception occurs below the except block(outside),program will terminate abnormally

-exception should only occur in try block,then only we can handle them,otherwise pvm will provide default exception handler for unhandled exceptions

#try-except-else-finally

try:
    #risky code
except:
    #handling code
else:
    #executes if no exception occurs
finally:
    #always execute
#######################################
raise keyword
-> keyword which is used to invoke or raise an exception

syntax:
raise exceptionname('exception message')

-> raise keyword is followed by an instance of exception class which we want to invoke
-> we can choose either predefined exception or custom exception

steps to define a custom/userdefined exception
1) create a class with 'custom exception name' and it should inherit the base class Exception

class CustomException(Exception):
    pass

2)whenever there is a negative outcome(unwanted/unexpected result),raise and exception with custom error message using raise
keyword and appropriately handle using try-except block in the caller program


'''     


