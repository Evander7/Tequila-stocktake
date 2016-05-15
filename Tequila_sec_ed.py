#A list of all available Tequilas, to show the user when they type "help"
#all lowercase values of these exact phrases are stored in the weights dictionary
#The script should take upper and lower case values of these exact strings
tequila_list = ["Jose Cuervo", "JLP", "Herradura", "El Jimador", "Arette", "Casa Noble","Don Julio Blanco", "Don Julio", "Don Julio 1942", "KAH", "Patron",\
                "Porfidio", "1800", "1800 Anejo", "Fortaleza", "T1", "Gran Centenario", "Jose Cuervo Reserva"]

#sets the Tequilas, and the weights of their different bottles.                
weights = {
    "jose cuervo":0.9, #guess
    "jlp":0.9, #guess
    "herradura": 0.9, #guess
    "el jimador":0.53,
    "arette":0.638,
    "casa noble":0.905,
    "don julio blanco":0.702,
    "don julio":0.789,
    "don julio 1942":.7, #guess
    "kah":.6, #guess
    "patron":0.77,
    "porfidio":0.7,
    "1800":0.817,
    "1800 anejo":0.747,
    "fortaleza":0.791,
    "t1":0.951,
    "gran centenario":0.583,
    "jose cuervo reserva":0.765
}


#universally sets the density of tequila
rho = 0.9501


def test():
    print("Type the name of the Tequila you want to test. Type 'Help' to see a list of all tequilas.")
    name = input("name : ")
    #type "help" to see all accepted inputs
    if name.lower() == "help":
        print("These are all the types of Tequila supported. If you're having difficulty, make sure you're spelling them right:")
        print(tequila_list)
        print("")
        test()

    #if the lowercase version of the name is in the dictionary "weights"
    elif name.lower() in weights:
        name = name.lower()
        #grabs the weight of that name's bottle by putting it into the dicitonary
        weight_b = weights[name]
        #Gets the current weight of bottle + tequila
        weight_t =(input("How much does this weigh? "))
        
        try:
            weight_t = float(weight_t)
            #makes sure that only a number has been entered, nothing else
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        #total weight minus weight of bottle
        volume = weight_liquid / rho
        #density = mass/volume^
        #also, assumes we're looking for shots measuring 30ml each
        shots = volume / .03
        if shots < 100:
            #gives it to 2 dp, provided the number is less than 100 (ie, a reasonable number)
            print("There are {} shots (of 30ml each) left in this bottle".format(str(shots)[:4]))
            print ("")
        else:
            #in case some silly and crazily big number is entered
            print("There are {} shots (of 30ml each) left in this bottle".format(shots))
            print("")
        test()

    #lets me fill any bottle I want with water as a test to see if the calculations work
    #asks what bottle I'm using, gets that bottle, and sets density = 1
    elif name.lower() == "water":
        try:
            bottle = input("What bottle are you using?  ").lower()
        except:
            print("Whoops! Are you sure you're spelling that correctly?")
            test()    
   
        weight_b = weights[bottle]
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / 1
        shots = volume / .03
        if shots < 100:
            print("There are {} shots (of 30ml each) left in this bottle".format(str(shots)[:4]))
            print ("")
        else:
            print("There are {} shots (of 30ml each) left in this bottle".format(shots))
            print("")
            
        test()

        
    else:
        print("Whoops! I don't recognise that name. Type 'Help' to see a list of accepted names, \
        and make sure they're spelt correctly!")
        test()


test()
