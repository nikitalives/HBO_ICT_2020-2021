#  Deze tool berekent de wisselkoers
#  Door Nikita Verhoeven

#  Waarde van de valuta in EUR
US_DOLLAR = 1.1811
GB_POUNDS = 0.9079
JP_YEN = 125.317

#  Vraag om input zodat de juiste valuta wordt genomen

valuta = int(input("Kies een valuta. Valuta: 1 = US Dollar, "
                   "2 = GB Pounds, 3 = Yen: "))
wisselbedrag = int(input("In te wisselen bedrag: "))

#  If else statement die checkt welke soort valuta wordt gegeven

if valuta == 1:
    valuta_invoer = "Dollar"
    te_ontvangen_bedrag = wisselbedrag / US_DOLLAR
elif valuta == 2:
    valuta_invoer = "Pounds"
    te_ontvangen_bedrag = wisselbedrag / GB_POUNDS
elif valuta == 3:
    valuta_invoer = "Yen"
    te_ontvangen_bedrag = wisselbedrag / JP_YEN
else:
    print("Kies voor 1, 2 of 3.")  ## wanneer er niet voor 1 2 of 3 wordt gekozen

#  format functie zorgt voor afgeronde op 2 decimalen
#  Print vervolgens het bedrag + omgerekende bedrag en de juiste valuta

print("Voor " + str(wisselbedrag) + " " + valuta_invoer + " krijgt u "
      + str(format(te_ontvangen_bedrag, '.2f')) + " Euro.")

#  Berekent transactiekosten van 1.5 procent over het te ontvangen bedrag
PERCENTAGE_TRANSACTIEKOSTEN = 0.015
transactie_kosten = te_ontvangen_bedrag * PERCENTAGE_TRANSACTIEKOSTEN

#  Checkt of de transactiekosten 2 euro of lager is, bij lager dan 2 euro
#  zijn de transactiekosten altijd 2 euro

if transactie_kosten <= 2:
    transactie_kosten = 2
else:
    transactie_kosten = transactie_kosten

#  het te ontvangen bedrag min de transactiekosten

eindbedrag = te_ontvangen_bedrag - transactie_kosten
print("De transactiekosten bedragen " + str(format(transactie_kosten,'.2f'))
      + " Euro. U ontvangt " + str(format(eindbedrag, '.2f')) + " Euro.")

