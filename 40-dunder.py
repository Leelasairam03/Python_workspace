'''
Dunder variables-> predefined special variables with double underscores at the start and end
                -> created by python automatically
applications/use of dunder variables
1)identifying modules
2)track where files are stored
3)provide documentation
4)controls how modules will behave when they are imported

Dunder variables: (practical in package_architecture folder)
1. __name__ -> it provides name of the module
            -> if file is executed directly then it will be assigned __main__ (string)
            -> if file is imported then it will be assigned the name of the module (string)
    
    note: to prevent certain code from executing whenever a module is imported that code should be placed inside a conditonal block
        if __name__ == "__main__":
            #test code

2. __file__ -> it shows the full path of that module/file which is currently being exdcuted at the moment
              
3. __package__ -> it is used by import system which tells to which package the module belongs to
               ->gives the name of the package under execution
                

4. __cached__ -> it stores the full file path of the bytecode generated for that module

5. __doc__ -> it stores the doc string of a module,class,function
           -> doc string=>string written at very beginning of a module.or class,or function,or method
           -> used for documentation purpose and to tell users what our code does
'''