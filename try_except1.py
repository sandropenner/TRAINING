#try:
#    pass
   # 4/0
    #print(name)
#except NameError as e:
#    print(e)
#except ZeroDivisionError:
#    print('Math Issue')
#except Exception:
#    print('ERROR')
#class CheeseError(Exception):
#    pass

#def upper_fun(word):
#    if len(word) <= 0:
#        raise CheeseError("The word needs atleast 1 letter!")
#    return word.upper

#print(upper_fun(""))

#print('after')
print("What's 9 + 10?")
num = 0
while num != 21:
    try:
        num = int(input())
        if num == 21:
            print("You did it!")
        else:
            print("WRONG")    
    except Exception:
        print("THAT'S NOT A NUMBER!!")  
