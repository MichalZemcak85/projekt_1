
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# print(texts)

hlavicka = """projekt_1.py: první projekt do Engeto Online Python Akademie\n
author: Michal Zemčák
email: michal.zemcak@gmail.com
discord: michal_79719"""

print(hlavicka)
print("")
oddelovac = "-" * 50

# Registrováni jsou následující uživatelé:
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Vyžádá si od uživatele přihlašovací jméno a heslo
username = input("Zadej svoje jmeno:")
password = input("Zadej svoje heslo:")

# Ověření uživatelských přihlašovacích údajů:
# pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
# pokud není registrovaný, upozorni jej a ukonči program.**
if username in users and users[username] == password:
    print("username:" + username,
          "password:" + password,
          oddelovac,
          "Welcome to the app, " + username,
          "We have 3 texts to be analyzed.",
          oddelovac,
          sep="\n")
# Pokud uživatel není registrovaný:
else:
    print(
        "username:" + username,
        "password:" + password,
        "unregistered user, terminating the program..",
        sep="\n")
    exit()

# analýza textu
cislo_textu = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)
if cislo_textu.isdigit():
    cislo_textu = int(cislo_textu)
    if 1 <= cislo_textu <= 3:
        analyse_text = TEXTS[cislo_textu - 1]
        # počet slov
        pocet_slov = len(analyse_text.split())
        # počet slov začínajících velkým písmenem
        pocet_zac_velke = sum(1 for word in analyse_text.split() if word.istitle())
        # počet slov psaných velkými písmeny
        pocet_velke = sum(1 for word in analyse_text.split() if word.isupper())
        # počet slov psaných malými písmeny
        pocet_male = sum(1 for word in analyse_text.split() if word.islower())
        # počet čísel (ne cifer)
        pocet_cisel = sum(1 for word in analyse_text.split() if word.isdigit())
        # sumu všech čísel (ne cifer) v textu
        suma_vsech_cisel = sum(int(word) for word in analyse_text.split() if word.isdigit())

        delka_slova = [len(word.strip(".,?!")) for word in analyse_text.split()]
        delka_slova_vyskyt = {length: delka_slova.count(length) for length in set(delka_slova)}

        print(f"There are {pocet_slov} words in the selected text.")
        print(f"There are {pocet_zac_velke} titlecase words.")
        print(f"There are {pocet_velke} uppercase words.")
        print(f"There are {pocet_male} lowercase words.")
        print(f"There are {pocet_cisel} numeric strings.")
        print(f"The sum of all the numbers {suma_vsech_cisel}.")

        # program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
        print(oddelovac)
        print("LEN|  OCCURENCES  |NR.")
        print(oddelovac)
        for pocet, vyskyt in sorted(delka_slova_vyskyt.items()):
            print(f"{pocet:2}|{'*' * vyskyt:14}|{vyskyt}")
    else:
        # pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
        print(username + " text number is out of range, terminating the program..")
else:
    # pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
    print(username + " invalid input, terminating the program..")
