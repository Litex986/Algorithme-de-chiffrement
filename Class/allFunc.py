import random

class allFunc:
    def __init__(self):
        '''
        Contains dictionaries with functions for encryption without a key in self.func along with their inverses in self.funcDecode.
        Contains dictionaries with functions for encryption with a key in self.funcKey along with their inverses in self.funcKeyDecode.
        '''
        self.func = {0: self.binary_inversion, 1: self.binary_switch, 2: self.substitute_hex, 3: self.reverseOneTwo, 4: self.reverseString}
        self.funcKey = {0: self.matriceMelange}
        self.funcDecode = {0: self.binary_inversion, 1: self.binary_switch_decode, 2: self.substitute_hex_decode, 3: self.reverseOneTwo, 4: self.reverseString}
        self.funcKeyDecode = {0: self.matriceMelange_decode}

    def xor(self, key, msg):
        '''
        XOR operation between two strings.
        Adapting the key to have strings of the same length.
        Conversion to binary for XOR operation.
        '''
        if len(key) > len(msg):
            key = key[:(len(msg))]
        elif len(key) < len(msg):
            while len(key) < len(msg):
                key += key
            key = key[:(len(msg))]
        assert len(key) == len(msg), "xor: msg and key have not the same len"
        a = self.hexToBin(key)
        b = self.hexToBin(msg)
        res = ''
        for i in range(len(a)):
            res += str(int(a[i]) ^ int(b[i]))
        return self.binToHex(res)

    def stringToInt(self, text):
        '''
        Converts a string into str(int) to simplify special characters.
        Uses their Unicode code.
        '''
        res = [str(ord(i)).zfill(len(str(max([ord(c) for c in text])))) for i in text]
        return str(len(res[0])) + ''.join(res)

    def intToString(self, text):
        '''
        Inverse of stringToInt.
        '''
        length = int(text[0])
        numbers = [text[i:i+length] for i in range(1, len(text), length)]
        return ''.join(chr(int(num)) for num in numbers)

    def intToHex(self, number):
        '''
        Converts an int to hexadecimal.
        '''
        number = int(number)
        res = ""
        while number > 0:
            number, remainder = divmod(number, 16)
            res = "0123456789abcdef"[remainder] + res
        return res if res else "0"

    def hexToInt(self, hexa):
        '''
        Inverse of intToHex.
        '''
        return str(sum(int(char, 16) * (16 ** i) for i, char in enumerate(hexa[::-1])))

    def hexToBin(self, hexa):
        '''
        Converts a hexadecimal to binary.
        '''
        res = ''
        for i in hexa:
            res += bin(int(i, 16))[2:].zfill(4)
        return res

    def binToHex(self, hexa):
        '''
        Inverse of hexToBin.
        '''
        return ''.join([hex(int(hexa[i:i+4], 2))[2:] for i in range(0, len(hexa), 4)])


    def binary_inversion(self, hexa):
        '''
        Fonction d'inversion des 0 et 1 en binaire
        '''
        binary = self.hexToBin(hexa)
        res = ''
        for i in binary:
            res += '0' if i == '1' else '1'
        hexa = self.binToHex(res)
        return hexa
    
    def binary_switch(self, hexa):
        '''
        Fonction de manipulation de binaire par transposition
        '''
        binary = self.hexToBin(hexa)
        res =""
        for i in range(len(binary)-1):
            if binary[i+1] == "1":
                res += '0' if binary[i] == '1' else '1'
            else:
                res += binary[i]
        res = res + binary[-1]
        return self.binToHex(res)

    def binary_switch_decode(self, hexa):
        '''
        Inverse de binary_switch
        '''
        binary = self.hexToBin(hexa)
        for i in range(2, len(binary)+1):
            if binary[-i+1] == "1":
                binary = binary[0:-i] + ('0' if binary[-i] == '1' else '1') + binary[len(binary)-i+1:len(binary)] 
        return self.binToHex(binary)
    
    def substitute_hex(self, hex_input):
        '''
        Hexadecimal substitution function.
        '''
        hex_input = hex_input
        substituted_hex = ''.join('{:X}'.format(15 - int(c, 16)) for c in hex_input)
        return substituted_hex.lower()

    def substitute_hex_decode(self, substituted_hex):
        '''
        Inverse of substitute_hex.
        '''
        substituted_hex = substituted_hex
        original_hex = ''.join('{:X}'.format(15 - int(c, 16)) for c in substituted_hex)
        return original_hex.lower()

    def reverseOneTwo(self, hexa):
        '''
        Binary manipulation function by transposition.
        '''
        hexa = list(hexa)
        for i in range(len(hexa) - 1):
            if i % 2 == 0:
                charIndiceSave = hexa[i]
                hexa[i] = hexa[i + 1]
                hexa[i + 1] = charIndiceSave
        return ''.join(hexa)

    def reverseString(self, hexa):
        '''
        Function to reverse the string of characters.
        '''
        return hexa[::-1]

    def matriceMelange(self, hexa, KEY):
        '''
        Function similar to S-Box but uses an additional encryption key to generate the matrix randomly.
        '''
        if len(hexa) % 2 != 0: 
            hexa = '0' + hexa
            zero = True
        else: 
            zero = False
        hexaForm = [format(i, '02x') for i in range(256)]
        random.seed(KEY)
        random.shuffle(hexaForm)
        matrice = [hexaForm[i:i+16] for i in range(0, 256, 16)]
        res = "".join(matrice[int(hexa[i], 16)][int(hexa[i + 1], 16)] for i in range(0, len(hexa), 2))
        if zero == True: 
            res = "ff" + res
        else: 
            res = "ee" + res
        return res

    def matriceMelange_decode(self, hexa, KEY):
        '''
        Inverse of matriceMelange.
        '''
        if hexa[:2] == "ff": 
            zero = True
        elif hexa[:2] == "ee": 
            zero = False
        assert hexa[:2] == "ff" or hexa[:2] == "ee"
        hexaForm = [format(i, '02x') for i in range(256)]
        random.seed(KEY)
        random.shuffle(hexaForm)
        matrice = [hexaForm[i:i+16] for i in range(0, 256, 16)] 
        res = ''
        for k in range(0, len(hexa), 2):
            idx = [(i, j) for i, row in enumerate(matrice) for j, val in enumerate(row) if val == hexa[k]+hexa[k+1]][0]
            res += hex(idx[0])[-1:] + hex(idx[1])[-1:]
        if zero == True: 
            res = res[3:]
        else: 
            res = res[2:]
        return res

    def messageToListToMelange(self, hexa, KEY):
        '''
        Function not used but intended for random transposition.
        '''
        hexa = [i for i in hexa]
        random.seed(KEY)
        [random.shuffle(hexa) for _ in range(random.randint(5, 20))]
        return ''.join(hexa)

    def messageToListToMelange_decode(self, hexa, KEY):
        '''
        Inverse of messageToListToMelange.
        '''
        hexa = [i for i in hexa]
        index = [str(i) for i in range(len(hexa))]
        random.seed(KEY)
        for i in range(random.randint(5, 20)):
            random.shuffle(index)
        res = [None for _ in range(len(hexa))]
        for idx, v in enumerate(index):
            res[int(v)] = hexa[idx]
        return ''.join(res)


