# functions add and display_name are used to show how many non-key arguments can be passed to a function

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return  total
print(add(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Ariel", "Junius", "Linius")
print()
print()


#function print_address is used to show how multiple keyword-arguments can be passed to a function

def print_address(**kwargs):
    for key, value in kwargs.items():
         print(f"{key}: {value}")
print_address(street="Ariel",
              city="Junius",
              apt = "100",
              state="Linius",
              zip="12345")