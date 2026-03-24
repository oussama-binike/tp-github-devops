def connecter(email, mot_de_passe):
    if not email or not mot_de_passe:
        raise ValueError("Email et mot de passe requis")
    return {"statut": "connecté", "email": email}
