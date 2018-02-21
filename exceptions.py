try:
    for i in ['a','b','c']:
        print i**2
except:
    print "Unsupported type!"


try:
    x = 5
    y = 0
    z = x/y

except:
    print "Division by zero!"

finally:
    "Finally block"

# error handle in a loop

def ask():
    while True:
        try:
            i = int(raw_input("Input an integer: "))
        except:
            print "An error occurred! Please try again!"
            continue
        else:
            print "Thank you, your number squared is: ", i*i
            break

ask()