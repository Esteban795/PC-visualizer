import matplotlib.pyplot as plt
import pandas as pd

# parse csv file
try:
    data = pd.read_csv('PC-visualizer/data.csv', sep=';')
except FileNotFoundError:
    print('File not found. Make sure it is named data.csv and in the PC-visualizer subfolder.')
    exit()

columns = data.columns

try:
    offer_title_column = columns.get_loc('Intitulé du tarif')
except KeyError:
    print('Column "Intitulé du tarif" not found. Make sure the file is in the right format, or modify the name of the column in the code.')
    exit()

try:
    offer_name_column = columns.get_loc("Nom de l’offre")
except KeyError:
    print("Column \"Nom de l'offre\" not found. Make sure the file is in the right format, or modify the name of the column in the code.")
    exit()

try:
    price_column = columns.get_loc("Prix de la réservation")
except KeyError:
    print("Column \"Prix de la réservation\" not found. Make sure the file is in the right format, or modify the name of the column in the code.")
    exit()

offer_name = data.columns[offer_name_column]
total_price = 0
histogram = {}

for index, row in data.iterrows():
    cancelled = row["Statut de la contremarque"]
    if cancelled == "annulé": #skip cancelled reservations
        continue
    total_price += row[price_column]
    offer_title = row[offer_title_column]
    histogram[offer_title] = histogram.get(offer_title, 0) + 1
    offer_name = row[offer_name_column]

labels = [f"{key} ({value})" for key, value in histogram.items()]
values = list(histogram.values())

#plotting values
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')
plt.title(f"Répartition des ventes pour l'offre {offer_name} (total : {total_price}€)")
plt.savefig('PC-visualizer/plot.png',bbox_inches='tight')