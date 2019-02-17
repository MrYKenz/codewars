import unittest

def rot13(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    caps = letters.upper()
    string = [i for i in string]
    for i in range(len(string)):
        if string[i] in caps:
            if (caps.index(string[i])+13) > 25:
                string[i] = caps[caps.index(string[i])-13]
            else:
                string[i] = caps[caps.index(string[i])+13]
        elif string[i] in letters:
            if (letters.index(string[i])+13) > 25:
                string[i] = letters[letters.index(string[i])-13]
            else:
                string[i] = letters[letters.index(string[i])+13]
    return ''.join(string)

### tests ###
class Test(unittest.TestCase):

    def testOneLetter(self):
        self.assertEqual('n', rot13('a'))

    def testSentence(self):
        self.assertEqual('Som!text*', rot13('Fbz!grkg*'))

unittest.main()
