def KM_to_MI(KM):
    """Konvertēt kilometrus jūdzēs."""
    return KM * 0.621371

def MI_to_KM(MI):
    """Konvertēt jūdzes kilometros."""
    return MILES / 0.621371 # type: ignore

def KG_to_LBS(KG):
    """Konvertēt kilogramus mārciņās."""
    return KG * 2.20462

def LBS_to_KG(POUNDS):
    """Konvertēt mārciņas kilogramos."""
    return POUNDS / 2.20462

def L_to_GAL(LITERS):
    """Konvertēt litrus galonos (ASV)."""
    return LITERS * 0.264172

def GAL_to_L(GALLONS):
    """Konvertēt galonus (ASV) litros."""
    return GALLONS / 0.264172

def USD_to_EUR(USD):
    """Konvertēt ASV dolārus uz Euro."""
    return USD * 0.84235020

def EUR_to_USD(EUR):
    """Konvertēt Euro uz ASV dolāriem."""
    return EUR / 0.84235020

def get_positive_float(prompt):
    """Iegūt pozitīvu skaitli no lietotāja."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("❌ Lūdzu ievadi pozitīvu skaitli!")
        except ValueError:
            print("❌ Lūdzu ievadi korektu skaitli. Mēģini vēlreiz.")

def get_valid_choice(prompt, valid_options):
    """Iegūt korektu izvēli no lietotāja."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        else:
            print(f"❌ Nepareiza izvēle! Lūdzu ievēlies no: {', '.join(valid_options)}")


def convert_distance():
    """Distance conversion menu."""
    print("\n=== Distances Konvertēšana ===")
    print("1. Kilometrus uz jūdzēm")
    print("2. Jūdzes uz kilometriem")
    choice = get_valid_choice("Izvēlies (1 vai 2): ", ["1", "2"])
    
    if choice == "1":
        KM = get_positive_float("Ievadi distanci kilometros: ")
        MI = KM_to_MI(KM)
        print(f"✅ {KM} km = {MI:.2f} jūdzes")
    elif choice == "2":
        MI = get_positive_float("Ievadi distanci jūdzēs: ")
        KM = MI_to_KM(MI)
        print(f"✅ {MI} jūdzes = {KM:.2f} KM")

def convert_weight():
    """Weight conversion menu."""
    print("\n=== Svara Konvertēšana ===")
    print("1. Kilogramus uz mārciņām")
    print("2. Mārciņas uz kilogramiem")
    choice = get_valid_choice("Izvēlies (1 vai 2): ", ["1", "2"])
    
    if choice == "1":
        KG = get_positive_float("Ievadi svaru kilogramos: ")
        LBS = KG_to_LBS(KG)
        print(f"✅ {KG} kg = {LBS:.2f} mārciņas")
    elif choice == "2":
        LBS = get_positive_float("Ievadi svaru mārciņās: ")
        KG = LBS_to_KG(LBS)
        print(f"✅ {LBS} mārciņas = {KG:.2f} kg")

def convert_volume():
    """Volume conversion menu."""
    print("\n=== Tilpuma Konvertēšana ===")
    print("1. Litrus uz galoniem")
    print("2. Galonus uz litriem")
    choice = get_valid_choice("Izvēlies (1 vai 2): ", ["1", "2"])
    
    if choice == "1":
        LITERS = get_positive_float("Ievadi tilpumu litros: ")
        GALLONS = L_to_GAL(LITERS)
        print(f"✅ {LITERS} L = {GALLONS:.2f} galoni")
    elif choice == "2":
        GALLONS = get_positive_float("Ievadi tilpumu galonos: ")
        LITERS = GAL_to_L(GALLONS)
        print(f"✅ {GALLONS} galoni = {LITERS:.2f} L")

def convert_currency():
    """Currency conversion menu."""
    print("\n=== Valūtas Konvertēšana ===")
    print("1. ASV dolārus uz Euro")
    print("2. Euro uz ASV dolāriem")
    choice = get_valid_choice("Izvēlies (1 vai 2): ", ["1", "2"])
    
    if choice == "1":
        USD = get_positive_float("Ievadi summu ASV dolāros: ")
        EUR = USD_to_EUR(USD)
        print(f"✅ ${USD} = €{EUR:.2f}")
    elif choice == "2":
        EUR = get_positive_float("Ievadi summu Euro: ")
        USD = EUR_to_USD(EUR)
        print(f"✅ €{EUR} = ${USD:.2f}")

def main_menu():
    """Main menu - choose conversion type."""
    while True:
        print("\n" + "="*40)
        print("🔄 UNIVERSĀLS KONVERTERS 🔄")
        print("="*40)
        print("1. Distances konvertēšana (KM ↔ Jūdzes)")
        print("2. Svara konvertēšana (KG ↔ Mārciņas)")
        print("3. Tilpuma konvertēšana (L ↔ Galoni)")
        print("4. Valūtas konvertēšana (USD ↔ EUR)")
        print("5. Iziet")
        print("="*40)
        
        choice = get_valid_choice("Izvēlies konversijas tipu (1-5): ", ["1", "2", "3", "4", "5"])
        
        if choice == "1":
            convert_distance()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_volume()
        elif choice == "4":
            convert_currency()
        elif choice == "5":
            print("\n👋 Paldies par izmantošanu! Uz redzēšanos!")
            break

if __name__ == "__main__":
    main_menu()
