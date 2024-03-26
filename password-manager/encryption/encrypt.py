'''
Primary Author: Jake Mitton
Contributor(s): N/A

An implementation of AES (Advanced Encryption System) for the
encryption of user passwords.

Sources:
https://csrc.nist.gov/files/pubs/fips/197/final/docs/fips-197.pdf
'''

from tables import Tables


def str_to_hex(input: str):
    hex_val = [hex(ord(character))[2:] for character in input]
    if len(hex_val) < 17:
        if len(hex_val) < 16:
            for each in range(16 - len(hex_val)):
                hex_val.insert(0, '00')
        return hex_val
    else:
        return None


def hex_to_str(input: list):
    result_string = ''
    for sub_list in input:
        for item in sub_list:
            result_string += chr(int(item, 16))
    return result_string


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

    def __init__(self, input: str) -> None:
        super().__init__()
        input = str_to_hex(input)
        # Each sublist in input is a COLUMN of the input so the input actually looks like:
        #    [0]  [4]  [8]   [12]
        #    [1]  [5]  [9]   [13]
        #    [2]  [6]  [10]  [14]
        #    [3]  [7]  [11]  [15]
        self.input = [[input[0], input[1], input[2], input[3]],
                      [input[4], input[5], input[6], input[7]],
                      [input[8], input[9], input[10], input[11]],
                      [input[12], input[13], input[14], input[15]]]
        # print("\nAt Start of Encryption")
        # print_that_input(self.input)

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

        # print("\nAfter _sub_bytes:")
        # print_that_input(self.input)

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

        # print("\nAfter _shift_rows:")
        # print_that_input(self.input)

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
                    # print("  ", temp_input[column][row], "XOR", hex(temp_value), "=", hex(temp_hex))
                temp_input[column][row] = hex(temp_hex)
                # print("    temp_input[", column, "][", row, "] =", temp_hex)

        self.input = [['0' + index[2:] if len(index[2:]) < 2 else index[2:] for index in each] for each in temp_input]

        # print("\nAfter _mix_columns:")
        # print_that_input(self.input)

    def key_expansion(self, key: list, ky: int) -> None:
        '''
        This method is the same for Encrypt and Decrypt classes
        Expand the cipher key to be 44 bytes long
        :arg key: Required by python
        :arg ky: not sure what this is for ATM
        :except No exceptions thrown by this method
        :return None
        '''
        pass

    def _add_round_key(self) -> None:
        '''
        This method is the same for Encrypt and Decrypt classes
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        pass

    def apply_cipher(self) -> str:
        self._sub_bytes()
        self._shift_rows()
        self._mix_columns()
        # Add round key
        return self.input


class Decryption(Tables):
    '''
    Implements inverse AES to decrypt passwords for storage in database
    METHODS:
        sub_bytes(self)
        shift_rows(self)
        mix_columns(self)
        add_round_key(self)
    '''

    def __init__(self, input: list) -> None:
        super().__init__()

        # Input is received as a list of lists in the format:
        #    [0][0]  [1][0]  [2][0]  [3][0]
        #    [0][1]  [1][1]  [2][1]  [3][1]
        #    [0][2]  [1][2]  [2][2]  [3][2]
        #    [0][3]  [1][3]  [2][3]  [3][3]
        # Where each number is the index if the data was a single list

        self.input = [[index for index in each] for each in input]
        # print("\nAt start of Decryption:")
        # print_that_input(self.input)

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

        # print("\nAfter _inv_shift_rows:")
        # print_that_input(self.input)

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

        # print("\nAfter _inv_sub_bytes:")
        # print_that_input(self.input)

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
                    # print("  ", temp_input[column][row], "XOR", hex(temp_value), "=", hex(temp_hex))
                temp_input[column][row] = hex(temp_hex)
                # print("    temp_input[", column, "][", row, "] =", temp_hex)

        self.input = [['0' + index[2:] if len(index[2:]) < 2 else index[2:] for index in each] for each in temp_input]

        # print("\nAfter _inv_mix_columns:")
        # print_that_input(self.input)

    def _add_round_key(self) -> None:
        '''
        Desc.
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        pass

    def apply_cipher(self) -> str:
        self._inv_mix_columns()
        self._inv_shift_rows()
        self._inv_sub_bytes()
        # Add round key
        str_value = hex_to_str(self.input)
        return str_value


if __name__ == '__main__':
    encrypt_imp = Encryption('Ô¿]0à´R®¸A      ')
    encrypted = encrypt_imp.apply_cipher()
    decrypt_imp = Decryption(encrypted)
    original = decrypt_imp.apply_cipher()
    # rotated_word = encrypt_imp._rot_word(['01', '02', '03', '04'])
    # print(rotated_word)
    # substituted_word = encrypt_imp._sub_word(rotated_word)
    # print(substituted_word)
