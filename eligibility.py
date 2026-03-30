def var_balsot(vecums):
    """
    Pārbauda, vai persona var balsot.

    Args:
        vecums (int): Personas vecums.

    Returns:
        bool: True, ja var balsot, pretējā gadījumā False.
    """
    return vecums >= 18

def var_iret_auto(vecums, ir_aplieciba):
    """
    Pārbauda, vai persona var īrēt automašīnu.

    Args:
        vecums (int): Personas vecums.
        ir_aplieciba (bool): Vai personai ir autovadītāja apliecība.

    Returns:
        bool: True, ja var īrēt automašīnu, pretējā gadījumā False.
    """
    return vecums >= 21 and ir_aplieciba

def var_pensionara_atlaide(vecums, ir_veterans):
    """
    Pārbauda, vai persona saņem pensionāra atlaides.

    Args:
        vecums (int): Personas vecums.
        ir_veterans (bool): Vai persona ir veterāns.

    Returns:
        bool: True, ja saņem pensionāra atlaides, pretējā gadījumā False.
    """
    return vecums >= 65 or ir_veterans

def var_studenta_atlaide(vecums, ir_students):
    """
    Pārbauda, vai persona saņem studenta atlaides.

    Args:
        vecums (int): Personas vecums.
        ir_students (bool): Vai persona ir students.

    Returns:
        bool: True, ja saņem studenta atlaides, pretējā gadījumā False.
    """
    return 16 <= vecums <= 26 and ir_students


def parse_ja_ne(atbilde):
    """
    Pārvērš lietotāja atbildi "jā/nē" par bool vērtību.

    Args:
        atbilde (str): Lietotāja atbilde.

    Returns:
        bool: True, ja atbilde ir jā (vai ja), citādi False.
    """
    if not isinstance(atbilde, str):
        return False
    atbilde = atbilde.strip().lower()
    return atbilde in ('jā', 'ja', 'y', 'yes', 'j')


def ir_deriga_atbilde(atbilde):
    """
    Pārbauda, vai atbilde ir derīga (jā vai nē variants).

    Args:
        atbilde (str): Lietotāja atbilde.

    Returns:
        bool: True, ja derīga, citādi False.
    """
    if not isinstance(atbilde, str):
        return False
    atbilde = atbilde.strip().lower()
    return atbilde in ('jā', 'ja', 'y', 'yes', 'j', 'nē', 'ne', 'no', 'n')


if __name__ == "__main__":
    try:
        vecums = int(input("Ievadiet savu vecumu: "))

        if vecums <= 17:
            print("Jūs vēl esat bērns!")
            raise SystemExit(0)

        while True:
            atbilde = input("Vai jums ir autovadītāja apliecība? (jā/nē): ")
            if ir_deriga_atbilde(atbilde):
                ir_aplieciba = parse_ja_ne(atbilde)
                break
            else:
                print("Ievadi lūdzu korektu atbildi!")

        while True:
            atbilde = input("Vai esat veterāns? (jā/nē): ")
            if ir_deriga_atbilde(atbilde):
                ir_veterans = parse_ja_ne(atbilde)
                break
            else:
                print("Ievadi lūdzu korektu atbildi!")

        while True:
            atbilde = input("Vai esat students? (jā/nē): ")
            if ir_deriga_atbilde(atbilde):
                ir_students = parse_ja_ne(atbilde)
                break
            else:
                print("Ievadi lūdzu korektu atbildi!")

        print("\nAtbilstības rezultāti:")

        print(f"• Drīkstat Balsot: {'✅ Jā' if var_balsot(vecums) else '❌ Nē'}")

        if var_iret_auto(vecums, ir_aplieciba):
            print("• Drīkstat Īrēt auto: ✅ Jā")
        else:
            if not ir_aplieciba:
                print("• Drīkstat Īrēt auto: ❌ Nē (nav autovadītāja apliecības)")
            else:
                print("• Drīkstat Īrēt auto: ❌ Nē (vecums mazāks par 21)")

        if var_pensionara_atlaide(vecums, ir_veterans):
            print("• Drīkstat saņemt senioru atlaides: ✅ Jā")
        else:
            print("• Drīkstat saņemt senioru atlaides: ❌ Nē")

        if var_studenta_atlaide(vecums, ir_students):
            print("• Drīkstat saņemt studenta atlaides: ✅ Jā")
        else:
            print("• Drīkstat saņemt studenta atlaides: ❌ Nē")

    except ValueError:
        print("Lūdzu, ievadiet derīgu skaitli vecumam.")
