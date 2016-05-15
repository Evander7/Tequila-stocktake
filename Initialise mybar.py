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

with open("mybar.txt", "r+") as bar:
    for key in weights:
        bar.write(key + "\n")


