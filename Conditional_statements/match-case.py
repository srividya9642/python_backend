''' Match-case is python's version of switch-case found in other languages. It allows us to match a variable's value against a set of patterns.'''



number = 2

match number :
    case 1 :
        print("One")
        
    case 2 |3 :
        print("Two or Three")
    case _ :
        print("Other number")