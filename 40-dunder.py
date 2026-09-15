'''
Dunder variables-> predefined special variables with double underscores at the start and end
                -> created by python automatically
applications/use of dunder variables
1)identifying modules
2)track where files are stored
3)provide documentation
4)controls how modules will behave when they are imported

Dunder variables:
1. __name__ -> it provides name of the module
            -> if file is executed directly then it will be assigned __main__
            -> if file is imported then it will be assigned the name of the module

2. __doc__ -> returns the docstring of the module
3. __file__ -> returns the path of the file
4. __package__ -> returns the package name
5. __cached__ -> returns the path of the cache file
'''