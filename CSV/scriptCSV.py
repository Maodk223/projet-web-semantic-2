import csv

# Ouvrir le fichier CSV en mode lecture et un nouveau fichier CSV en mode écriture
with open('Top_10_Albums_By_Year_Album_Length.csv.csv', 'r', newline='', encoding='utf-8') as input_file, \
     open('cleaned.csv', 'w', newline='', encoding='utf-8') as output_file:

    reader = csv.DictReader(input_file, delimiter=';')
    writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames, delimiter=';')
    writer.writeheader()

    # Parcourir chaque ligne du fichier d'entrée
    for row in reader:
        # Vérifier si la clé 'Year' existe et si sa valeur est supérieure ou égale à 2015
        if 'Year' in row and int(row['Year']) >= 2014:
            # Écrire la ligne dans le fichier de sortie
            writer.writerow(row)
