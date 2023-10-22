import pwntools

# Spécifie le système d'exploitation cible
target = pwntools.linux.openssh.OpenSSH()

# Génère des données aléatoires
data = pwntools.util.random_bytes(1024)

# Envoie les données à la cible
target.send(data)

# Attend une réponse de la cible
response = target.recv()

# Vérifie si la réponse est inhabituelle
if response.startswith("Invalid packet"):
    print("Vulnérabilité trouvée !")
else:
    print("Pas de vulnérabilité trouvée.")
