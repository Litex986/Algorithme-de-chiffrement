# Algorithme-de-chiffrement
 Algorithme de chiffrement symétrique

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
