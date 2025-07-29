
def greet(name, region):
    message = get_message(region)
    return message + " " + name

def get_message(region):
    if (region == 'USA'):
        return 'Hello'
    elif (region == 'India'):
        return 'Namaste'
print(greet('Jessa', 'USA'))