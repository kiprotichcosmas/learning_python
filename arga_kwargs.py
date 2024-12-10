#using both non-key and key arguments in one function

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    print( )
    print("Your shipping label is: ", end=" ")
    for key, value in kwargs.items():
        print(f"{key} : {value}")


shipping_label("Dr", "Cosmas", "Karonei", "3RD",
                street="Ariel",
                city="Junius",
                apt = "100",
                state="Linius",
                zip="12345")