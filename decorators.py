def start_end_decorater(function):
    
    def wrapper():
        print("start")
        function()
        print("stop")
    return wrapper 
def print_name():
    print("Alice")

print_name= start_end_decorater(print_name)
print_name()


