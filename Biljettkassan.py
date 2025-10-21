# ------------------------------------------------------------
# 1) Biljettkassan – summera inkomster (split, strip, int, loop)
# ------------------------------------------------------------
# Startvärden (hårdkodat):
belopp = "120, 75, 120, 90, 75"
#total_sum = 0
#ticket_count = 0
# Instruktion:
# - Dela strängen med split(",")
#parts = belopp.split(",")
#print(belopp)
# - Ta bort mellanslag runt varje del med strip()
#for part in parts:
  #  clean_part = part.strip()
    # - Konvertera varje del till int i en loop
  #  belopp = int(clean_part)
    # - Räkna antal biljetter och total summa
 #   total_sum += belopp
 #   ticket_count += 1
# - Skriv en kort sammanfattning
#print(f"Number of tickets sold: {ticket_count}")
#print(f"Total income: {total_sum}")
#

# Uppgradera med input:

belopp = input("Enter amounts separated by commas: ")
for belopp in belopp.split(","):
    belopp = belopp.strip()
    if belopp.isdigit():
        belopp = int(belopp)
        print(belopp)
    else:
        print(f"Invalid input: {belopp}")