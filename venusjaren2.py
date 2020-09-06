# Deze tool berekent je leeftijd in Venusjaren
# Door Nikita Verhoeven

import datetime as dt

nu = dt.datetime.now()  # datum van vandaag

venusjaar_verhouding = 0.62  # Venus draait 0.62 keer zo snel om de zon als de Aarde

# Wat de console toont:
print("Wat is je naam?")  # vraag om naam
naam = input()  # invoer toekennen variabele 'naam'

print("Wat is je geboortejaar?")  # vraag om geboortejaar
geboortejaar = int(input())  # invoer geboortejaar

leeftijd = nu.year - geboortejaar  # berekening leeftijd in jaren
leeftijd_in_venusjaren = leeftijd / venusjaar_verhouding #berekening leeftijd in venusjaren

# Toont huidige jaar en berekende leeftijd in een string
print("Beste " + naam + ", in "
      + str(nu.year) + " zal je leeftijd op aarde "
      + str(leeftijd) + " zijn.")

# Toont leeftijd in Venusjaren in een string
print("En je leeftijd is dan " + str(leeftijd_in_venusjaren) + " in Venusjaren.")