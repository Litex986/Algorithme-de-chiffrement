from Class import key, allFunc

class Decrypt:
    '''
    Contains the inverse methods of Encrypt
    Executes them in the reverse direction of the encryption
    '''
    def __init__(self, KEY, message, comp=[2, 2, 2]):
        self.key = key.Key(KEY)
        self.func = allFunc.allFunc()
        self.complex = comp
        self.message = message
        self.initialisationKeys()
        self.concatenationMessageReverse()
        self.layer(2)
        self.splitMessageReverse()
        self.concatenationMessageReverse(True)
        self.mainLoop()
        self.splitMessageReverse()
        self.concatenationMessageReverse()
        self.layer(0)
        self.splitMessageReverse(True)
        
    def splitMessageReverse(self, first=False):
        if first:
            self.message = self.func.intToString(self.func.hexToInt(''.join(self.message)))
        else:
            self.message = ''.join(self.message)
    
    def initialisationKeys(self):
        self.key.keyBase = self.key.deriveKeys(self.key.KEY, 4)
        self.key.keys[3] = self.key.deriveKeys(self.key.keyBase[3], 2)
    
    def layer(self, layer):
        self.key.keys[layer] = self.key.deriveKeys(self.key.keyBase[layer], self.complex[0] * len(self.message))
        for i in range(1, len(self.message) + 1):
            for j in range(1, self.complex[0]+1):
                key = self.key.deriveKeys(self.key.keys[layer][-(j + (i - 1) * self.complex[0])], 3)
                self.message[-i] = self.func.xor(key[2], self.message[-i])
                self.message[-i] = self.func.funcKeyDecode[(j-1)%len(self.func.funcKeyDecode)](self.message[-i] , key[1])
                self.message[-i] = self.func.xor(key[0], self.message[-i])
    
    def mainLoop(self):
        self.key.keys[1] = self.key.deriveKeys(self.key.keyBase[1], self.complex[1] * len(self.message))
        for i in range(1, len(self.message)+1):
            for j in range(1, self.complex[1]+1):
                key = self.key.deriveKeys(self.key.keys[1][-(j + (i - 1) * self.complex[1])], 3)
                self.message[-i] = self.func.xor(key[2], self.message[-i])
                self.message[-i] = self.func.funcKeyDecode[self.vecInit[1][-(j + (i-1) * self.complex[1])]](self.message[-i], key[1])
                for k in range(1, self.complex[2]+1):
                     self.message[-i] = self.func.funcDecode[self.vecInit[0][-((j-1)*self.complex[2] + k + (i-1) * self.complex[1] * self.complex[2])]](self.message[-i])
                self.message[-i] = self.func.xor(key[0], self.message[-i])
    
    def concatenationMessageReverse(self, vector=False):
        vectorlst = []
        if vector:
            spliter = self.message.find(str(len(self.func.func)))
            vectorlst.append(self.message[0:spliter])
            spliter2 = self.message.find(str(len(self.func.func)), spliter + 1)
            vectorlst.append(self.message[spliter+1:spliter2])
            self.message = self.message[spliter2+1:]
            self.vecInit = [[int(vectorlst[0][i:i+2]) for i in range(0, len(vectorlst[0]), 2)], [int(vectorlst[1][i:i+2]) for i in range(0, len(vectorlst[1]), 2)]]
        else:message = [0, 0]
        idxlen = int(self.message[0:4], 16)
        message = self.message[4:]
        messageLst = [message[i:i+int(idxlen)] for i in range(0, len(message), int(idxlen))]
        self.message = messageLst