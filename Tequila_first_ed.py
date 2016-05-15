'''
Especial Jose Cuervo 0.9502
Clasico Jose Cuervo 0.9496
Black Jose Cuervo 0.9505
Tradicional Jose Cuervo 0.9499
Reserva de la Familia Jose Cuervo 0.9502


avg = 0.9532, or 0.9501


'''
tequila_list = ["Jose Cuervo", "JLP", "Herradura", "El Jimador", "Arette", "Casa Noble","Don Julio Blanco", "Don Julio", "Don Julio 1942", "KAH", "Patron",\
                "Porfidio", "1800", "1800 Anejo", "Fortaleza", "T1", "Gran Centenario", "Jose Cuervo Reserva de la Familia"]
rho = 0.9501
def test():
    #resets rho, in case some exact densities are used\
    #ie with Reserva de la familia, it will override the global definition
    rho = 0.9501
    print("Type the name of the Tequila you want to test. Type 'Help' to see a list of all tequilas.")
    name = input("name : ")
    if name.lower() == "help":
        print("These are all the types of Tequila supported. If you're having difficulty, make sure you're spelling them right:")
        print(tequila_list)
        print("")
        test()
        
#Jose Cuervo
    elif name.lower() == "jose cuervo":
        weight_b = .5 #guessed bottle weight
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#JLP        
    elif name.lower() == "jlp":
        weight_b = .5 #guessed bottle weight
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Herradura        
    elif name.lower() == "herradura":
        weight_b = .5 #guessed bottle weight
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#El Jimador        
    elif name.lower() == "el jimador":
        weight_b = .530
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Arette        
    elif name.lower() == "arette":
        weight_b = .638 #averaged the blanco and reposado on hand (.633 and .642)
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Casa Noble        
    elif name.lower() == "casa noble":
        weight_b = .905
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Don Julio Blanco
    elif name.lower() == "don julio blanco":
        weight_b = .702
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Don Julio
    elif name.lower() == "don julio":
        weight_b = .789
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()

#Don Julio 1942
    elif name.lower() == "don julio 1942":
        weight_b = .5 #guessed bottle weight
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
        
#KAH
    elif name.lower() == "kah":
        weight_b = .5 #guessed bottle weight
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Patron
    elif name.lower() == "patron":
        weight_b = .77 
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#Porfidio
    elif name.lower() == "porfidio":
        weight_b = .5 #guessed bottle weight
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#1800
    elif name.lower() == "1800":
        weight_b = .817 
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
        
#1800 Anejo
    elif name.lower() == "1800 anejo":
        weight_b = .747 
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()

#Fortaleza
    elif name.lower() == "fortaleza":
        weight_b = .791
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
#T1
    elif name.lower() == "t1":
        weight_b = .951
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
            
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
        
#Jose Cuervo Reserva de la familia
    elif name.lower() == "jose cuervo reserva":
        rho = 0.9502 
        weight_b = .765
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        weight_liquid = weight_t - weight_b
        volume = weight_liquid / rho
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()

#Gran Centenario
    elif name.lower() == "gran centenario":

        weight_b = 0.583 
        #setting the weight of the bottle
        #finding out how much the bottle + liquid weighs
        #makes sure input is just a float
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        #calculating the weight of the liquid
        weight_liquid = weight_t - weight_b
        #using rho = m/v to calculate volume of just the liquid
        volume = weight_liquid / rho
        #calculating how many 30ml shots are in there
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
        

        
#Water test        
    elif name.lower() == "water": 
        rho = 1
        weight_b = .77
        #setting the weight of the bottle
        #finding out how much the bottle + liquid weighs
        #makes sure input is just a float
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        #calculating the weight of the liquid
        weight_liquid = weight_t - weight_b
        #using rho = m/v to calculate volume of just the liquid
        volume = weight_liquid / rho
        #calculating how many 30ml shots are in there
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()

    else:
        print("Whoops! I don't recognise that name. Type 'Help' to see a list of accepted name, \
and make sure they're spelt correctly!")
        test()
    
#format below:
'''

When creating a new Tequila, copy and paste above the "else" statement, making sure it's indented one\
space, and replace $NAME and $BOTTLE_WEIGHT. 

#don't know if I need to know if it's Blanco etc . If I do, then I find name[:len(name)-2],
#provided the name is written $NAME B/R/A (with the space), and $name is lowercase


    elif name.lower() == "$NAME":

        weight_b = $BOTTLE_WEIGHT 
        #setting the weight of the bottle
        #finding out how much the bottle + liquid weighs
        #makes sure input is just a float
        weight_t =(input("How much does this weigh? "))
        try:
            weight_t = float(weight_t)
        except:
            print("Whoops! Try *just* inputting numbers, nothing else")
            test()
        #calculating the weight of the liquid
        weight_liquid = weight_t - weight_b
        #using rho = m/v to calculate volume of just the liquid
        volume = weight_liquid / rho
        #calculating how many 30ml shots are in there
        shots = volume / .03
        print("There are {} 30 ml shots left in this bottle".format(shots))
        print ("")
        test()
    
'''    

test()
