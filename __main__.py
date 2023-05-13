import random as r

V = 'a', 'e', 'i', 'o', 'u'
C = 'p', 'b', 'v', 'm', 'w', 'th', 'tj', 't', 'd', 's', 'ts', 'tl', 'n', 'l', 'sh', 'sj', 'ch', 'cj', 'r', 'j', 'k', 'g', 'h', 'hl'
E = 'p', 'b', 'v', 'm', 'w', 'th', 'tj', 't', 'd', 's', 'n', 'l', 'sh', 'sj', 'ch', 'cj', 'j', 'k', 'g', 'h'

starting_syllable_types = 'EVC', 'EV', 'V', 'VC'
syllable_types = 'CVC', 'CV', 'VC', 'V', 'VV'

adjective_prefixes = 'du', 'dia'

# must be set to 'verb', 'adjective', or 'noun'
word_type = 'noun'

word_count = 10

def main():
    for word in range(word_count):

        syllable_count = 0
        if word_type == 'verb':
            syllable_count = r.randint(1,3)
        else:
            syllable_count = r.randint(1,4)
        result = ''

        for syllable in range(syllable_count):
            temp_result = ''
            if syllable == 0 and word_type != 'adjective':
                temp_result = temp_result + create_starting_syllable()
            elif syllable == 0 and word_type == 'adjective':
                temp_result = temp_result + r.sample(adjective_prefixes, 1)[0]
            else:
                temp_result = temp_result + create_syllable()
            
            result = result + temp_result
            # print(temp_result)
        if word_type == 'verb':
            result = result + r.sample(V, 1)[0] + 'l'
        print(result)

def create_starting_syllable():
    r_syllable = r.sample(starting_syllable_types, 1)[0]
    # print('STARTING SYLLABLE: ', r_syllable)
    temp_result = ''
    for i in range(len(r_syllable)):
        match r_syllable[i]:
            case 'E':
                temp_result = temp_result + r.sample(E, 1)[0]
            case 'V':
                temp_result = temp_result + r.sample(V, 1)[0]
            case 'C':
                temp_result = temp_result + r.sample(C, 1)[0]
    return temp_result

def create_syllable():
    r_syllable = r.sample(syllable_types, 1)[0]
    # print('SYLLABLE: ', r_syllable)
    temp_result = ''
    for i in range(len(r_syllable)):
        match r_syllable[i]:
            case 'E':
                temp_result = temp_result + r.sample(E, 1)[0]
            case 'V':
                temp_result = temp_result + r.sample(V, 1)[0]
            case 'C':
                temp_result = temp_result + r.sample(C, 1)[0]
    return temp_result
                
if __name__ == '__main__':
    main()

