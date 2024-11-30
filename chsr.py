def chiffrer(texte, decalage):
    result = ""
    for char in texte:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + decalage) % 26 + start)
        else:
            result += char
    return result

def dechiffrer(texte, decalage):
    return chiffrer(texte, -decalage)

def main():
    print("Bienvenu dans le programme de chiffrement et déchiffrement de César !")

    while True:
        choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer un texte ? (C/D) : ").strip().lower()

        if choix not in ['c', 'd']:
            print("Choix invalide. Veuillez entrer 'C' pour chiffrer ou 'D' pour déchiffrer.")
            continue
        
        texte = input("Entrez le texte : ")

        while True:
            try:
                decalage = int(input("Entrez le décalage (clé) : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide pour le décalage.")

        if choix == 'c':
            texte_resultat = chiffrer(texte, decalage)
            print(f"Texte chiffré : {texte_resultat}")
        elif choix == 'd':
            texte_resultat = dechiffrer(texte, decalage)
            print(f"Texte déchiffré : {texte_resultat}")
        
        recommencer = input("Voulez-vous effectuer une autre opération ? (O/N) : ").strip().lower()
        if recommencer != 'o':
            print("Au revoir !")
            break
        
if __name__ == "__main__":
    main()
