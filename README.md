# Algorithme-de-chiffrement
 Algorithme de chiffrement symétrique


## 1 - Initialisation

### **clef de chiffrement**

&emsp;512 bits

&emsp;composition de lettre minuscule et chiffre

### **message**

&emsp;division du message en morceau de 128 bits `x_message`

### **clef de chiffrement** 

&emsp;hash de la clef 

&emsp;dérivation en ( 2 * `x_message` + 2 * `x_message`+ 2 * `x_message` + 2) sous clef `y_sous_clef`

&emsp;&emsp;2 * `x_message` pour la première couche de chiffrement  `y_sous_clef0`

&emsp;&emsp;2 * `x_message` pour les 2 itérations de la boucle principale `y_sous_clef1`

&emsp;&emsp;2 * `x_message` pour la dernière couche de chiffrement `y_sous_clef2`

&emsp;&emsp;+2 pour les 2 couches intermédiaires `y_sous_clef3`

### **vecteur initialisation** 

&emsp;((2*2+2) * `x_message`) nombres aléatoires correspondant à des fonctions `vecteur`

&emsp;&emsp;2 pour 2 fonctions de chiffrement par itération de la boucle principale

&emsp;&emsp;*2 pour 2 itérations

&emsp;&emsp;+2 pour une fonction utilisant la clef de chiffrement pour les 2 itérations

&emsp;&emsp;*`x_message` pour `x_message` bout de message

## 2 - Première couche

2 itérations `i` pour chacune des `x_message`

&emsp;dérivation de la `i` ème `y_sous_clef0` = `y_sous_clef0_1`

&emsp;xor avec la première dérivée de la `i` ème `y_sous_clef0_1`

&emsp;1 fonction de chiffrement utilisant la deuxième dérivée de la`i` ème `y_sous_clef0_1`

&emsp;xor avec la troisième dérivée de la `i` ème `y_sous_clef0_1`

## 3 - Intermédiaire

dérivation en 2 de la première `y_sous_clef3`

reconstitution de message avec les `x_message` chiffré en utilisant la première dérivée de `y_sous_clef3`

redécoupage du message en morceau de 256 bits `x_message2` en utilisant la deuxième dérivée de `y_sous_clef3`

## 4 - Boucle principale

2 itération `j` pour chacune des `x_message2`

&emsp;dérivation de 3 sous clefs  de la `j` ème `y_sous_clef1` = `y_sous_clef1_1`

&emsp;xor avec le première `y_sous_clef1_1`

&emsp;2 fonctions de chiffrement choisies par le `vecteur` parmi les fonction de chiffrement

&emsp;1 fonction de chiffrement choisie par le `vecteur`  utilisant la deuxième `y_sous_clef1_1` 

&emsp;xor avec la troisième `y_sous_clef1_1`

## 5 - Intermédiaire

dérivation en 3 de la deuxième `y_sous_clef3`

reconstitution de message avec les `x_message2` chiffré en utilisant la première dérivée de `y_sous_clef3`

ajout du `vecteur` dans le message en utilisant la deuxième dérivée de `y_sous_clef3`

redécoupage du message en morceau de 256 bits `x_message3` en utilisant la troisième dérivée de `y_sous_clef3`

## 6 - Dernière couche

2 itérations `k` pour chacune des `x_message3`

&emsp;dérivation de la `k` ème `y_sous_clef2` = `y_sous_clef0_1`

&emsp;xor avec la première dérivée de la `k` ème `y_sous_clef0_1`

&emsp;1 fonction de chiffrement utilisant la deuxième dérivée de la`k` ème `y_sous_clef0_1`

&emsp;xor avec la troisième dérivée de la `k` ème `y_sous_clef0_1`

## 7 - Reconstitution

reconstitution de message avec les `x_message3` chiffré en utilisant la deuxième `y_sous_clef3`



----



### **Classe `Key` :**

- **`deriveKeys`**: Cette méthode prend une clé et dérive plusieurs sous-clés à l'aide de la fonction de hachage SHA256 et HKDF (HMAC Key Derivation Function).

Dans le contexte de la classe `Key`, la méthode `deriveKeys` utilise HKDF pour dériver plusieurs sous-clés à partir d'une clé principale. Ces sous-clés dérivées peuvent ensuite être utilisées pour différentes opérations de chiffrement et de déchiffrement.

### **Classe `allFunc` :**

- **Fonctions de Conversion**: Convertissent entre différentes représentations de données telles que chaînes de caractères, entiers, hexadécimal et binaire.
- **Fonctions de Manipulation Binaire**:
    - **`binary_inversion`**: Inverse les bits 0 et 1 dans une représentation binaire.
    - **`binary_switch`**: Manipule une chaîne binaire par transposition.
    - **`binary_switch_decode`**: Inverse la fonction **`binary_switch`**.
    - **`reverseOneTwo`**: Effectue une manipulation binaire par transposition.
    - **`reverseString`**: Inverse l'ordre des caractères dans une chaîne.
- **Fonctions de Substitution Hexadécimale**:
    - **`substitute_hex`**: Effectue une substitution hexadécimale sur une entrée.
    - **`substitute_hex_decode`**: Inverse la fonction **`substitute_hex`**.
- **`matriceMelange` et `matriceMelange_decode`**: Ces fonctions utilisent une clé de chiffrement supplémentaire pour générer une matrice de manière aléatoire pour le chiffrement et le déchiffrement.

### **Classe `Encrypt` :**

- Prend une clé et un message à chiffrer.
- Effectue les étapes de chiffrement selon un plan défini :
    - Division du message en morceaux de 32 caractères.
    - Couches de chiffrement (première, principale, dernière) utilisant des sous-clés dérivées.

### **Classe `Decrypt` :**

- Contient les méthodes inverses pour décrypter un message chiffré.
- Effectue les étapes de décryptage en sens inverse par rapport au chiffrement.

### **Fonction `argument` :**

- Gère les arguments de ligne de commande pour l'exécution du script.
- Lit le message à chiffrer/déchiffrer à partir d'un fichier.
- Détermine le mode (chiffrer ou déchiffrer) et exécute l'action appropriée.

# Utilisation

Chiffrement :

```powershell
python3 "C:/chemin/vers/votre_script.py" -k 'votre_clé_secrete' -f 'C:/chemin/vers/votre_fichier.txt’
```

- `chemin_vers_script`: Chemin complet vers votre script de chiffrement Python.
- `-k 'votre_clé'`: Option pour spécifier la clé de chiffrement (optionnel).
- `-f 'chemin_vers_votre_fichier'`: Option pour spécifier le chemin complet vers le fichier à chiffrer.

Déchiffrement :

```powershell
python3 "C:/chemin/vers/votre_script.py" -k 'votre_clé_secrete' -f 'C:/chemin/vers/votre_fichier_chiffré.txt’ -m d
```

- `chemin_vers_script`: Chemin complet vers votre script de chiffrement Python.
- `-k 'votre_clé'`: Option pour spécifier la clé de déchiffrement.
- `-f 'chemin_vers_votre_fichier'`: Option pour spécifier le chemin complet vers le fichier chiffré.
- `-m d`: Option pour spécifier le mode déchiffrement
