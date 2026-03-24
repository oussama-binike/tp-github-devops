def saluer(nom):
    return f"Bonjour depuis GitHub, {nom} !"

def calculer_imc(poids, taille):
    return round(poids / (taille ** 2), 2)

if __name__ == "__main__":
    print(saluer("DevOps"))
    print("IMC:", calculer_imc(70, 1.75))

def formater_message(msg, majuscules=False):
    return msg.upper() if majuscules else msg.lower()
