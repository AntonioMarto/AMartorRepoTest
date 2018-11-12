
def Case_1 ():
    print "\n############################# Case 1: No Exception! #############################"
    print "Taceback error will be displayed and our code will blow up here because we did not anticipate our error code to hadle (except) the Exception: \n"
    f=open('ze_.txt') # "ze_.txt" does not exist and Python will throw an exception and blow up the code here


print "\n############################# Case 2: General Exception! #############################"
try:
    f=open('ze_.txt') # "ze_.txt" does not exist, Python will throw an exception but because it's inside the "try:"" block the expection will be hadle in the "except:" block
except Exception:
    print "Some exception was thrown!!! We do not know which one."


print "\n############################# Case 3: Nature of General Exception! #############################"
try:
    f=open('ze_.txt') # "ze_.txt" does not exist, Python will throw an exception but because it's inside the "try:" block the expection will be hadle in the "except:" block
except Exception as e: #it will tell the user the nature of the expection
    print e

print "\n############################# Case 4: Catch a particular Exception! #############################"
try:
    f=open('ze_.txt') # "ze_.txt" does not exist, Python will throw an exception but because it's inside the "try:" block the expection will be hadle in the "except:" block
except IOError as e: #it will catch a particular type of exception the user the nature of the expection
    print (e)


print "\n############################# Case 5: Else and Finally clauses! #############################"
try:
    f=open('ze.txt') # "ze.txt" exists
except Exception as e:
    print e
else:  # only runs if we do not throw an exception 
    print "content of %s:" %f.name
    print f.read()
finally: # runs no matter the code is succefully or if we throw an exception
    print "\nExecuting Finally..."
    f.close()


print "\n############################# Case 6: Raise Manual Exception! #############################"
try:
    f=open('ze.txt') # "ze.txt" exists
    if f.name == 'ze.txt':
        raise Exception
except Exception:
    print "Manual exception was Raised!!!"
finally: # runs no matter the code is succefully or if we throw an exception
    print "\nExecuting Finally..."
    f.close()