# from operator import itemgetter
import itertools # Cartesian Product using itertools.product()

def get_pins(observed):
    dic = { '1': ['1','2','4'],
            '2': ['1','2','3','5'],
            '3': ['2','3','6'],
            '4': ['1','4','5','7'],
            '5': ['2','4','5','6','8'],
            '6': ['3','5','6','9'],
            '7': ['4','7','8'],
            '8': ['5','7','8','9','0'],
            '9': ['6','8','9'],
            '0': ['8','0'] }

    # keys = [i for i in observed]
    # vals = itemgetter(*keys)(dic) 
    vals = [dic[i] for i in observed] 
    
    ### TESTING ITERTOOLS ### return list(itertools.product(dic['1'],dic['1']))
    ### UNFORMATTED RESULT ### return list(itertools.product(*vals))
    return [''.join(i) for i in list(itertools.product(*vals))]

print(get_pins('11'))
