from Class import key, allFunc
import secrets

class Encrypt:
    def __init__(self, KEY, message, comp=[2, 2, 2]):
        self.key = key.Key(KEY)
        self.complex = comp # Number of iterations for the loops
        self.func = allFunc.allFunc()
        self.message = message
        '''
        Follows the encryption plan from our technical documentation
        --------------------------------
        1) Division of the message into chunks of 32 characters
        2) First layer
        3) Intermediate
        4) Main loop
        5) Intermediate with the vector
        6) Last layer
        7) Reconstruction
        '''
        self.splitMessage(True) # 1
        self.initialisationKeys() 
        self.layer(0) # 2
        self.concatenationMessage() # 3
        self.splitMessage() # 3
        self.initialisationVector() # Initializes the initialization vector that will determine the order of functions randomly
        self.mainLoop() # 4
        self.concatenationMessage(self.vecInit) # 5
        self.splitMessage() # 5
        self.layer(2) # 6
        self.concatenationMessage() # 7
        
    def splitMessage(self, first=False):
        '''
        Division of the message into chunks of 32 characters
        '''
        if first:
            hexa = self.func.intToHex(self.func.stringToInt(self.message))
            if len(hexa)%2!=0:hexa = '0' + hexa
        else:
            hexa = self.message
        self.message = [hexa[i:i+32] for i in range(0, len(hexa), 32)]

    def initialisationKeys(self):
        '''
        Prepare the keys to be derived later
        '''
        self.key.keyBase = self.key.deriveKeys(self.key.KEY, 4)
        self.key.keys[3] = self.key.deriveKeys(self.key.keyBase[3], 2)

    def initialisationVector(self):
        '''
        Initializes the initialization vector that will determine the order of functions randomly
        '''
        self.vecInit = []
        self.vecInit.append([secrets.randbelow(len(self.func.func)) for i in range((self.complex[2]*self.complex[1]) * len(self.message))]) # For functions without a key
        self.vecInit.append([secrets.randbelow(len(self.func.funcKey)) for i in range(self.complex[1] * len(self.message))]) # For functions with a key

    def layer(self, layer):
        '''
        Encryption layer used during the first and last layers
        '''
        self.key.keys[layer] = self.key.deriveKeys(self.key.keyBase[layer], self.complex[0] * len(self.message)) # Generating subkeys for each part of the message
        for i in range(len(self.message)): # For each part of the message
            for j in range(self.complex[0]): # x repetition for each part of the message (default x=2)
                key = self.key.deriveKeys(self.key.keys[layer][j + i * self.complex[0]], 3) # Generating 3 subkeys for each operation
                self.message[i] = self.func.xor(key[0], self.message[i]) # XOR
                self.message[i] = self.func.funcKey[j%len(self.func.funcKey)](self.message[i], key[1]) # Encryption function with a key
                self.message[i] = self.func.xor(key[2], self.message[i]) # XOR

    def mainLoop(self):
        self.key.keys[1] = self.key.deriveKeys(self.key.keyBase[1], self.complex[1] * len(self.message)) # Generating subkeys for each part of the message
        for i in range(len(self.message)): # For each part of the message
            for j in range(self.complex[1]): # x repetition for each part of the message (default x=2)
                key = self.key.deriveKeys(self.key.keys[1][j + i * self.complex[1]], 3) # Generating 3 subkeys for each operation
                self.message[i] = self.func.xor(key[0], self.message[i]) # XOR
                for k in range(self.complex[2]): # x repeat keyless encryption (default x=2)
                    self.message[i] = self.func.func[self.vecInit[0][j*self.complex[2] + k + i * self.complex[1] * self.complex[2]]](self.message[i]) # function chosen by the initialization vector
                self.message[i] = self.func.funcKey[self.vecInit[1][j + i * self.complex[1]]](self.message[i], key[1]) # Encryption function with a key
                self.message[i] = self.func.xor(key[2], self.message[i]) # XOR
    
    def concatenationMessage(self, vector=None):
        '''
        Group message pieces into one 
        Possibility of adding the initialization vector
        '''
        concat = self.message
        maxLen = len(self.message[0])
        concat = "".join(concat[i] for i in range(len(concat)))
        lenMess = hex(maxLen)[2:].zfill(4)
        concat = lenMess + "".join(concat)
        if vector:
            vec = ''
            for i in vector[0]:vec += str(i).zfill(2)
            vec += str(len(self.func.func))
            for i in vector[1]:vec += str(i).zfill(2)
        self.message =  concat if not vector else vec + str(len(self.func.func)) + concat