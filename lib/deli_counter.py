def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        callout = "The line is currently:"
        for index, name in enumerate(katz_deli):
            pass
            callout += f" {index +1}. {name}"
        
        print(callout)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")
    

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        pass
        print(f"There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    