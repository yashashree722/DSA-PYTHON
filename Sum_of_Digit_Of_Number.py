def fun(number) :
    if number ==0 :
        return 0 
    if number % 9 ==0:
        return 9
    return number %9


ans =fun(71)
print(ans)


# tc = o(1)