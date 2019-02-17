def plus(x): # returns a tuple of 2 elements [proshmo, arithmos]
    a = ['+',x]
    return a

def minus(x):
    a = ['-',x]
    return a

def times(x):
    a = ['*',x]
    return a

def div(x):
    a = ['/',x]
    if x==0:
        raise ValueError('Division by zero.')
    return a

def zero(a = None):
    this_num=0
    if a: # default value of a is None (isodunamo me orismo 2 synarthsewn -mia me orisma kai mia xwris)
        praksi = a[0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else: # klhsh synarthshs ws deuterou telesteou (xwris parametro)
        return this_num


def one(a = None):
    this_num=1
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num

def two(a = None):
    this_num=2
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num

def three(a = None):
    this_num=3
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num


def four(a = None):
    this_num=4
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num


def five(a = None):
    this_num=5
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num

def six(a = None):
    this_num=6
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num


def seven(a = None):
    this_num=7
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num


def eight(a = None):
    this_num=8
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num


def nine(a = None):
    this_num=9
    if a:
        praksi = a [0]
        other_num = a[1]
        if praksi=='+':
            return this_num + other_num
        elif praksi=='-':
            return this_num - other_num
        elif praksi=='*':
            return this_num * other_num
        elif praksi=='/':
            return this_num / other_num
    else:
        return this_num


#test
print("Examples:")
print("five(times(five())) =", five(times(five())))
print("five(plus(seven())) =", five(plus(seven())))
print("seven(minus(five())) =", seven(minus(five())))
print("five(minus(nine())) =", five(minus(nine())))
print("seven(div(five())) =", seven(div(five())))
#print(five(div(zero()))) 
# raises exception (division by zero)
