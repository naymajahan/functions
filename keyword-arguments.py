
# KEYWORD ARGUMENTS
####Additional arguments to a function and their action depends on the keyword that we place.
# keywords like- "end", "sep"

## keyword arguments- END

print("Nayma ", end= "")
print("Jahan")


## Keyword Argument- SEP(seperation)

print("Mitu","Oishe","Shoshe",sep=",")


##Examples of SCOPE
## SCOPE is region of code
 ## region inside a function- local scope & variables local variables
  ## region outside a function- global function & variables global variables

def f():
    c = 10
    print(c)

f()

### example of global variable

def f():
    global a
    print(23+a)

a= 22
f()

### Exception Handeling 
# Error Handeling


def func():
    try:
        return 100/x
    except :
        return "There is a zero division error"
answer = func()
print(answer)
