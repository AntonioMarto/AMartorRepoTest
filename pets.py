class Pet(object): # Pet is a class of the type `object` 
    def __init__(self, name, species): # Class initialization: `__init__` is method (special Python function) is called when a instance of a class is first created.
        self.name = name
        self.species = species
        # `self` is the instance of the class.
        # when we run the code: `boby = Pet("Boby", "Epanhol-Breton")`, 
        # the __init__ method is called with values (boby, "Boby", and "Epanhol-Breton") 
        # for the variables (self, name, and species), respectively.

    
    # methods to get the contents of the class:
    def getName(self):
        return self.name
    
    def getSpecies(self):
        return self.species

    def __str__(self):      
        return "%s is a %s" %(self.name, self.species)
        
# boby = Pet("Boby", "dog")
# print "Name: %s" %boby.getName()
# print "Specie: %s" %boby.getSpecies()
# print boby