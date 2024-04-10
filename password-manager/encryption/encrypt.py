'''
Primary Author: Jake Mitton
Contributor(s): N/A

An implementation of AES (Advanced Encryption System) for the
encryption of user passwords.

Sources:
https://csrc.nist.gov/files/pubs/fips/197/final/docs/fips-197.pdf
'''

# from encryption.tables import Tables
from encryption.tables import Tables


def print_that_input(grid: list) -> None:
    print(grid[0][0], grid[1][0], grid[2][0], grid[3][0])
    print(grid[0][1], grid[1][1], grid[2][1], grid[3][1])
    print(grid[0][2], grid[1][2], grid[2][2], grid[3][2])
    print(grid[0][3], grid[1][3], grid[2][3], grid[3][3])


class Encryption(Tables):
    '''
    Implements AES to encrypt passwords for storage in database
    METHODS:
        sub_bytes(self)
        shift_rows(self)
        mix_columns(self)
        add_round_key(self)
    '''

    def __init__(self, input: str, key: list) -> None:
        super().__init__()
        try:
            input = self.str_to_hex(input)
        except ValueError:
            print("ERROR: Password cannot exceed 16 characters.")
            exit()
        else:
            # Each sublist in input is a COLUMN of the input so the input actually looks like:
            #    [0]  [4]  [8]   [12]
            #    [1]  [5]  [9]   [13]
            #    [2]  [6]  [10]  [14]
            #    [3]  [7]  [11]  [15]
            self.input = [[input[0], input[1], input[2], input[3]],
                          [input[4], input[5], input[6], input[7]],
                          [input[8], input[9], input[10], input[11]],
                          [input[12], input[13], input[14], input[15]]]
            self.expanded_key = self.key_expansion(key)

    def _sub_word(self, word: str) -> str:
        '''
        Takes a four byte input word and substitutes each byte using the s-box
        :param word: A 4-byte input string (in hexadecimal)
        :return: word after substituting bytes using s-box
        '''
        for each in range(0, len(word)):
            x = int(word[each][0], 16)
            y = int(word[each][1], 16)
            word[each] = self.sbox[x][y]
        return word

    def _rot_word(self, word: list) -> list:
        '''
        Takes a four byte input word and performs a left rotation of one position.
        Word at intake:       [b0, b1, b2, b3]
        Word after Rotation:  [b1, b2, b3, b0]
        :param word: A 4-byte input string (in hexadecimal)
        :return: word after rotation
        '''
        temp = word.pop(0)
        word.append(temp)
        return word

    def _sub_bytes(self) -> None:
        '''
        Substitutes each byte using the SBOX substitution table
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        for column in range(0, len(self.input)):
            for index in range(len(self.input[column])):
                x = int(self.input[column][index][0], 16)
                y = int(self.input[column][index][1], 16)
                self.input[column][index] = self.sbox[x][y]

    def _shift_rows(self) -> None:
        '''
        Applies a wrapped around left shift to the bytes
        of each row of the input grid
            00 01 02 03         00 01 02 03     * 0 shift *
            10 11 12 13    ->   11 12 13 10     * 1 shift *
            20 21 22 23         22 23 20 21     * 2 shift *
            30 31 32 33         33 30 31 32     * 3 shift *

        Because the input grid is stored as a list the shift
        is equivalent to the following:
            [[00, 10, 20, 30], [01, 11, 21, 31], [02, 12, 22, 32], [03, 13, 23, 33]]
            [[00, 11, 22, 33], [01, 12, 23, 30], [02, 13, 20, 31], [03, 10, 21, 32]]

        :arg self: description
        :except No exceptions thrown by this method
        :return None
        '''
        temp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        temp[0][0] = self.input[0][0]
        temp[0][1] = self.input[1][1]
        temp[0][2] = self.input[2][2]
        temp[0][3] = self.input[3][3]

        temp[1][0] = self.input[1][0]
        temp[1][1] = self.input[2][1]
        temp[1][2] = self.input[3][2]
        temp[1][3] = self.input[0][3]

        temp[2][0] = self.input[2][0]
        temp[2][1] = self.input[3][1]
        temp[2][2] = self.input[0][2]
        temp[2][3] = self.input[1][3]

        temp[3][0] = self.input[3][0]
        temp[3][1] = self.input[0][1]
        temp[3][2] = self.input[1][2]
        temp[3][3] = self.input[2][3]
        for col in range(len(temp)):
            for item in range(0, 4):
                self.input[col][item] = temp[col][item]

    def _mix_columns(self) -> None:
        '''
        Treats each column as a four term polynomial and multiplied
        modulo x^4+1 with a(x) = {03}x^3+{01}x^2+{01}x+{02}
        This function is represented by mds_matrix:
            2  3  1  1
            1  2  3  1
            1  1  2  3
            3  1  1  2
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        temp_input = [['00', '00', '00', '00'],
                      ['00', '00', '00', '00'],
                      ['00', '00', '00', '00'],
                      ['00', '00', '00', '00']]
        mds_matrix = [[2, 3, 1, 1],
                      [1, 2, 3, 1],
                      [1, 1, 2, 3],
                      [3, 1, 1, 2]]

        for column in range(0, len(self.input)):
            for row in range(0, len(self.input[column])):
                temp_hex = int('00', 16)
                for index in range(0, len(self.input[column])):
                    c = int(self.input[column][index][0], 16)
                    r = int(self.input[column][index][1], 16)

                    temp_value = 0
                    if mds_matrix[row][index] == 1:
                        temp_value = int(self.input[column][index], 16)
                    elif mds_matrix[row][index] == 2:
                        temp_value = int(self.multi_2[c][r], 16)
                    elif mds_matrix[row][index] == 3:
                        temp_value = int(self.multi_3[c][r], 16)

                    temp_hex = temp_hex ^ temp_value
                temp_input[column][row] = hex(temp_hex)
        self.input = [['0' + index[2:] if len(index[2:]) < 2 else index[2:] for index in each] for each in temp_input]

    def key_expansion(self, key: list) -> list:
        '''
        This method is the same for Encrypt and Decrypt classes
        Expand the cipher key to be 44 bytes long
        :arg key: A list of words [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
                  Where 1-4 is word 1, 5-6 is word 2, 7-8 is word 3...
        :except No exceptions thrown by this method
        :return List of the expanded key as 4 byte words
        '''
        # This is the list of round constants DO NOT MODIFY
        RCON = [['01', '00', '00', '00'], ['02', '00', '00', '00'],
                ['04', '00', '00', '00'], ['08', '00', '00', '00'],
                ['10', '00', '00', '00'], ['20', '00', '00', '00'],
                ['40', '00', '00', '00'], ['80', '00', '00', '00'],
                ['1B', '00', '00', '00'], ['36', '00', '00', '00']]

        expanded_w = []
        temp = []
        four_ago = []

        # Copy the key into the first four words of the expanded key
        for i in range(0, 4):
            expanded_w.append(key[i])

        # Iterate over the key generating new words to append
        for j in range(4, 44):
            for each in range(0, 4):
                temp.append(expanded_w[j - 1][each])
                four_ago.append(expanded_w[j - 4][each])
            # Every fourth round the _sub_word and _rot_word methods are applied
            # and an extra XOR operation is carried out between the current word and RCON
            if j % 4 == 0:
                temp = self._sub_word(self._rot_word(temp))
                for byte in range(0, len(temp)):
                    temp[byte] = hex(int(temp[byte], 16) ^ int(RCON[int(j / 4) - 1][byte], 16))[2:]
            # Each round ends with current word XOR word from 4 rounds ago
            more_temp = []
            for each in range(0, len(four_ago)):
                most_temp = hex(int(four_ago[each], 16) ^ int(temp[each], 16))[2:]
                if len(most_temp) < 2:
                    most_temp = '0' + most_temp
                more_temp.append(most_temp)
            # Add current word to the expanded word list and reset the temporary lists
            expanded_w.append(more_temp)
            temp.clear()
            four_ago.clear()
        return expanded_w

    def _add_round_key(self, round_num: int) -> None:
        '''
        This method is the same for Encrypt and Decrypt classes
        :arg self: Required by python
        :arg round_num: What round of the encryption the cipher is on
        :except No exceptions thrown by this method
        :return None
        '''
        if round_num > 0:
            round_num = round_num * 4
        for column in range(0, len(self.input)):
            for row in range(0, len(self.input[column])):
                self.input[column][row] = hex(
                    int(self.input[column][row], 16) ^ int(self.expanded_key[round_num + column][row], 16))[2:]
                if len(self.input[column][row]) < 2:
                    self.input[column][row] = '0' + self.input[column][row]

    def apply_cipher(self) -> str:
        '''
        Calls the other methods to implement the AES 128 Cipher.
        This is not exact to the FIPS 197 specification of AES,
        specifically, the cipher typically runs for 10 rounds,
        whereas our implementation runs one round of encryption
        due to time constraints in implementation.
        :arg self: Required by Python
        :except No exceptions thrown by this method
        :return:None
        '''

        self._sub_bytes()
        self._shift_rows()
        self._mix_columns()
        self._add_round_key(0)

        cipher_string = ''
        for sub_list in self.input:
            for hex_value in sub_list:
                cipher_string += hex_value
        return cipher_string


class Decryption(Tables):
    '''
    Implements inverse AES to decrypt passwords for storage in database
    METHODS:
        sub_bytes(self)
        shift_rows(self)
        mix_columns(self)
        add_round_key(self)
    '''

    def __init__(self, input: str, key: list) -> None:
        super().__init__()

        # Input is received as a list of lists in the format:
        #    [0][0]  [1][0]  [2][0]  [3][0]
        #    [0][1]  [1][1]  [2][1]  [3][1]
        #    [0][2]  [1][2]  [2][2]  [3][2]
        #    [0][3]  [1][3]  [2][3]  [3][3]
        # Where each number is the index if the data was a single list
        indices = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        self.input = [[], [], [], []]
        for each, ind in zip(range(0, len(input), 2), indices):
            self.input[ind].append(input[each:each + 2])

        for sub_list in self.input:
            if len(sub_list) < 4:
                for each in range(len(sub_list), 4):
                    sub_list.append('00')

        self.expanded_key = self.key_expansion(key)

    def _sub_word(self, word: str) -> str:
        '''
        Takes a four byte input word and substitutes each byte using the s-box
        :arg word: A 4-byte input string (in hexadecimal)
        :except No exceptions thrown by this method
        :return: word after substituting bytes using s-box
        '''
        for each in range(0, len(word)):
            x = int(word[each][0], 16)
            y = int(word[each][1], 16)
            word[each] = self.sbox[x][y]
        return word

    def _rot_word(self, word: list) -> list:
        '''
        Takes a four byte input word and performs a left rotation of one position.
        Word at intake:       [b0, b1, b2, b3]
        Word after Rotation:  [b1, b2, b3, b0]
        :arg word: A 4-byte input string (in hexadecimal)
        :except No exceptions thrown by this method
        :return: word after rotation
        '''
        temp = word.pop(0)
        word.append(temp)
        return word

    def _inv_shift_rows(self) -> None:
        '''
        Applies a wrapped around right shift to the bytes
        of each row of the input grid
            00 01 02 03         00 01 02 03     * 0 shift *
            10 11 12 13    ->   13 10 11 12     * 1 shift *
            20 21 22 23         22 23 20 21     * 2 shift *
            30 31 32 33         31 32 33 30     * 3 shift *
        :arg self: description
        :except No exceptions thrown by this method
        :return None
        '''
        temp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        temp[0][0] = self.input[0][0]
        temp[1][1] = self.input[0][1]
        temp[2][2] = self.input[0][2]
        temp[3][3] = self.input[0][3]

        temp[1][0] = self.input[1][0]
        temp[2][1] = self.input[1][1]
        temp[3][2] = self.input[1][2]
        temp[0][3] = self.input[1][3]

        temp[2][0] = self.input[2][0]
        temp[3][1] = self.input[2][1]
        temp[0][2] = self.input[2][2]
        temp[1][3] = self.input[2][3]

        temp[3][0] = self.input[3][0]
        temp[0][1] = self.input[3][1]
        temp[1][2] = self.input[3][2]
        temp[2][3] = self.input[3][3]
        for col in range(len(temp)):
            for item in range(0, 4):
                self.input[col][item] = temp[col][item]

    def _inv_sub_bytes(self) -> None:
        '''
        Substitutes each byte using the Inverse SBOX substitution table
        :arg self: Required by python
        :except NA No exceptions thrown by this method
        :return None
        '''

        for column in range(0, len(self.input)):
            for index in range(len(self.input[column])):
                x = int(self.input[column][index][0], 16)
                y = int(self.input[column][index][1], 16)
                self.input[column][index] = self.inverse_sbox[x][y]

    def _inv_mix_columns(self) -> None:
        '''
        Treats each column as a four term polynomial and multiplied
        modulo x^4+1 with a(x) = {0b}x^3+{0d}x^2+{09}x+{03}
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''

        temp_input = [['00', '00', '00', '00'],
                      ['00', '00', '00', '00'],
                      ['00', '00', '00', '00'],
                      ['00', '00', '00', '00']]

        mds_matrix = [['0e', '0b', '0d', '09'],
                      ['09', '0e', '0b', '0d'],
                      ['0d', '09', '0e', '0b'],
                      ['0b', '0d', '09', '0e']]

        for column in range(0, len(self.input)):
            for row in range(0, len(self.input[column])):
                temp_hex = int('00', 16)
                for index in range(0, len(self.input[column])):
                    c = int(self.input[column][index][0], 16)
                    r = int(self.input[column][index][1], 16)

                    temp_value = 0
                    if mds_matrix[row][index] == '01':
                        temp_value = int(self.input[column][index], 16)
                    elif mds_matrix[row][index] == '02':
                        temp_value = int(self.multi_2[c][r], 16)
                    elif mds_matrix[row][index] == '03':
                        temp_value = int(self.multi_3[c][r], 16)
                    elif mds_matrix[row][index] == '09':
                        temp_value = int(self.multi_9[c][r], 16)
                    elif mds_matrix[row][index] == '0b':
                        temp_value = int(self.multi_b[c][r], 16)
                    elif mds_matrix[row][index] == '0d':
                        temp_value = int(self.multi_d[c][r], 16)
                    elif mds_matrix[row][index] == '0e':
                        temp_value = int(self.multi_e[c][r], 16)

                    temp_hex = temp_hex ^ temp_value
                temp_input[column][row] = hex(temp_hex)
        self.input = [['0' + index[2:] if len(index[2:]) < 2 else index[2:] for index in each] for each in temp_input]

    def key_expansion(self, key: list) -> list:
        '''
        This method is the same for Encrypt and Decrypt classes
        Expand the cipher key to be 44 bytes long
        :arg key: A list of words [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
                  Where 1-4 is word 1, 5-6 is word 2, 7-8 is word 3...
        :except No exceptions thrown by this method
        :return List of the expanded key as 4 byte words
        '''
        # This is the list of round constants DO NOT MODIFY
        RCON = [['01', '00', '00', '00'], ['02', '00', '00', '00'],
                ['04', '00', '00', '00'], ['08', '00', '00', '00'],
                ['10', '00', '00', '00'], ['20', '00', '00', '00'],
                ['40', '00', '00', '00'], ['80', '00', '00', '00'],
                ['1B', '00', '00', '00'], ['36', '00', '00', '00']]

        expanded_w = []
        temp = []
        four_ago = []

        # Copy the key into the first four words of the expanded key
        for i in range(0, 4):
            expanded_w.append(key[i])

        # Iterate over the key generating new words to append
        for j in range(4, 44):
            for each in range(0, 4):
                temp.append(expanded_w[j - 1][each])
                four_ago.append(expanded_w[j - 4][each])
            # Every fourth round the _sub_word and _rot_word methods are applied
            # and an extra XOR operation is carried out between the current word and RCON
            if j % 4 == 0:
                temp = self._sub_word(self._rot_word(temp))
                for byte in range(0, len(temp)):
                    temp[byte] = hex(int(temp[byte], 16) ^ int(RCON[int(j / 4) - 1][byte], 16))[2:]
            # Each round ends with current word XOR word from 4 rounds ago
            more_temp = []
            for each in range(0, len(four_ago)):
                most_temp = hex(int(four_ago[each], 16) ^ int(temp[each], 16))[2:]
                if len(most_temp) < 2:
                    most_temp = '0' + most_temp
                more_temp.append(most_temp)
            # Add current word to the expanded word list and reset the temporary lists
            expanded_w.append(more_temp)
            temp.clear()
            four_ago.clear()
        return expanded_w

    def _add_round_key(self, round_num: int) -> None:
        '''
        Using an XOR operation combines the data to be encrypted
        with the key.
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        if round_num > 0:
            round_num = round_num * 4
        for column in range(0, len(self.input)):
            for row in range(0, len(self.input[column])):
                self.input[column][row] = hex(
                    int(self.input[column][row], 16) ^ int(self.expanded_key[round_num + column][row], 16))[2:]
                if len(self.input[column][row]) < 2:
                    self.input[column][row] = '0' + self.input[column][row]

    def apply_cipher(self) -> str:
        '''
        Calls the other methods to implement the AES 128 Cipher.
        This is not exact to the FIPS 197 specification of AES,
        specifically, the cipher typically runs for 10 rounds,
        whereas our implementation runs one round of decryption
        due to time constraints in implementation.
        :arg self: Required by Python
        :except No exceptions thrown by this method
        :return:None
        '''

        self._add_round_key(0)
        self._inv_mix_columns()
        self._inv_shift_rows()
        self._inv_sub_bytes()

        str_value = self.hex_to_str(self.input)
        str_value = str_value.strip('\0')
        return str_value


if __name__ == '__main__':
    the_key_1 = [['2b', '7e', '15', '16'], ['28', 'ae', 'd2', 'a6'], ['ab', 'f7', '15', '88'], ['09', 'cf', '4f', '3c']]
    input_password = input("Please enter a password:")
    print("Password before encryption:", input_password)
    encrypt_imp = Encryption(input_password, the_key_1)
    encrypted = encrypt_imp.apply_cipher()
    print("Password after encryption:", encrypted.upper())
    the_key_2 = [['2b', '7e', '15', '16'], ['28', 'ae', 'd2', 'a6'], ['ab', 'f7', '15', '88'], ['09', 'cf', '4f', '3c']]
    decrypt_imp = Decryption(encrypted, the_key_2)
    original = decrypt_imp.apply_cipher()
    print("Password after decryption:", original)
