#  Deze tool berekent de leeftijd en leeftijd in Venusjaren
#  Door Nikita Verhoeven

import datetime as dt

#  Toekennen van variabele om huidige datum te kunnen tonen en om het huidige jaar
#  in de berekening te kunnen meenemen
nu = dt.datetime.now()
huidige_jaar = nu.year

#  Toekennen van variabele venusjaar_verhouding
#  Venus draait 0.62 keer zo snel om de zon als de Aarde
venusjaar_verhouding = 0.62

#  Vraagt om naam in de console en vraagt om het geboortejaar, zodat de leeftijd
#  in jaren kan worden berekend en de leeftijd in Venusjaren kan worden berekend

naam = input("Wat is je naam? ")
geboortejaar = int(input("Wat is je geboortejaar? "))

#  Berekening van leeftijd in 'aardjaren' en vervolgens de leeftijd berekend
#  in Venusjaren door de leeftijd in aardjaren te delen door 0.62 (aantal keer
#  sneller dan de draaiing van de aarde om de zon)

leeftijd = huidige_jaar - geboortejaar
leeftijd_in_venusjaren = leeftijd / venusjaar_verhouding

#  Print de naam uit de input, weergeeft het  huidige jaar en weergeeft de
#  berekende leeftijd in een string in de console
#  Print een regel daaronder eens string met daarin de

print("Beste " + naam + ", in "
      + str(nu.year) + " zal je leeftijd op aarde "
      + str(leeftijd) + " zijn.")
print("En je leeftijd is dan " + str(leeftijd_in_venusjaren) + " in Venusjaren.")
