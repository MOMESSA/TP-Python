# Demander … l'utilisateur de saisir le nombre de notes
nombre_notes = int(input("Combien de notes souhaitez-vous saisir ? "))

# Initialiser une liste pour stocker les notes
notes = []

# Saisir les notes et les stocker dans la liste
for i in range(nombre_notes):
    note = float(input(f"Saisissez la note {i + 1} : "))
    notes.append(note)


