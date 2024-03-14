'''
Primary Author: Jake Mitton
Contributor(s): N/A

An implementation of AES (Advanced Encryption System) for the
encryption of user passwords.

Sources:
https://csrc.nist.gov/files/pubs/fips/197/final/docs/fips-197.pdf
'''


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
    pass


class Encryption:
    '''
    Implements AES to encrypt passwords for storage in database
    METHODS:
        sub_bytes(self)
        shift_rows(self)
        mix_columns(self)
        add_round_key(self)
    '''

    def __init__(self, input: str) -> None:
        self.sbox = [
            ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
            ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
            ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
            ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
            ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
            ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
            ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
            ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
            ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
            ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
            ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
            ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
            ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
            ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
            ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
            ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

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

    def _sub_bytes(self) -> None:
        '''
        Substitutes each byte using the SBOX substitution table
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        print("PRE", self.input)

        for column in range(0, len(self.input)):
            for index in range(len(self.input[column])):
                x = int(self.input[column][index][0], 16)
                y = int(self.input[column][index][1], 16)
                self.input[column][index] = self.sbox[x][y]

        print(self.input)

    def _shift_rows(self) -> None:
        '''
        Applies a wrapped around left shift to the bytes
        of each row of the input grid
            00 01 02 03         00 01 02 03     * 0 shift *
            10 11 12 13    ->   11 12 13 10     * 1 shift *
            20 21 22 23         22 23 20 21     * 2 shift *
            30 31 32 33         33 30 31 32     * 3 shift *
        :arg self: description
        :except No exceptions thrown by this method
        :return None
        '''
        pass

    def _mix_columns(self) -> None:
        '''
        Treats each column as a four term polynomial and multiplied
        modulo x^4+1 with a(x) = {03}x^3+{01}x^2+{01}x+{02}
        :arg self: Required by python
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
        pass


class Decryption:
    '''
    Implements inverse AES to decrypt passwords for storage in database
    METHODS:
        sub_bytes(self)
        shift_rows(self)
        mix_columns(self)
        add_round_key(self)
    '''

    def __init__(self, input: list) -> None:
        self.inverse_sbox = [
            ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
            ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', '39', 'cb'],
            ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
            ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
            ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
            ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
            ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', '34', '58', '05', 'b8', 'b3', '45', '06'],
            ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
            ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', '72', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
            ['96', 'ac', '74', '22', '37', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
            ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'b3', '1b'],
            ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
            ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
            ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
            ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
            ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']]

        # Input is received as a list of lists in the format:
        #    [0][0]  [1][0]  [2][0]  [3][0]
        #    [0][1]  [1][1]  [2][1]  [3][1]
        #    [0][2]  [1][2]  [2][2]  [3][2]
        #    [0][3]  [1][3]  [2][3]  [3][3]
        # Where each number is the index if the data was a single list
        self.input = input

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
        pass

    def _inv_sub_bytes(self) -> None:
        '''
        Substitutes each byte using the Inverse SBOX substitution table
        :arg self: Required by python
        :except NA No exceptions thrown by this method
        :return None
        '''
        print("PRE", self.input)

        for column in range(0, len(self.input)):
            for index in range(len(self.input[column])):
                x = int(self.input[column][index][0], 16)
                y = int(self.input[column][index][1], 16)
                self.input[column][index] = self.inverse_sbox[x][y]

        print(self.input)

    def _inv_mix_columns(self) -> None:
        '''
        Treats each column as a four term polynomial and multiplied
        modulo x^4+1 with a(x) = {0b}x^3+{0d}x^2+{09}x+{03}
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        pass

    def _add_round_key(self) -> None:
        '''
        Desc.
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        pass

    def apply_cipher(self) -> str:
        pass


if __name__ == '__main__':
    cypher_text = Encryption('Jake')
    cypher_text._sub_bytes()
    temp = cypher_text.input
    cipher_text = Decryption(temp)
    cipher_text._inv_sub_bytes()

