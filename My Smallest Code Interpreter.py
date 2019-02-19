plusminus_value = {'+': 1, '-': -1}
lessmore_value = {'<': -1, '>': 1}
brc_value = {'[': 1, ']': -1}
brc_pair = {'[': ']', ']': '['}

def brain_luck(code, inputs):
    inputl = list(inputs)
    code_ptr = data_ptr = 0
    data = [0]
    output = ''

    while code_ptr != len(code):
        inst = code[code_ptr]

        if inst == '.':
            output += chr(data[data_ptr])

        if inst == ',':
            data[data_ptr] = ord(inputl.pop(0))

        if inst in lessmore_value:
            data_ptr += lessmore_value[inst]
            if data_ptr == len(data):
                data.append(0)

        if inst in plusminus_value:
            data[data_ptr] += plusminus_value[inst]
            data[data_ptr] %= 256

        if (inst == '[' and data[data_ptr] == 0) or (inst == ']' and data[data_ptr] != 0):
            direction = bracket_counter = brc_value[inst]
            while not (code[code_ptr] == brc_pair[inst] and bracket_counter == 0):
                code_ptr += direction
                if code[code_ptr] in brc_value:
                    bracket_counter += brc_value[code[code_ptr]]

        code_ptr += 1

    return output
