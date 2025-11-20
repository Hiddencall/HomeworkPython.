from smartphone import Smartphone

catalog = [Smartphone("Samsung", "Galaxy", "+7 953 233 23 14"),
           Smartphone("Ifone", "I16", "+7 962 424 12 13"),
           Smartphone("Xaomi", "M16PRO", "+7 915 657 21 12"),
           Smartphone("ReadmeNote", "12S", "+7 931 647 67 43"),
           Smartphone("Techno", "PRO14S", "+7 991 265 72 13")]

for smartphone in catalog:
    print(f"{smartphone.marka}-{smartphone.model}. {smartphone.number}")
