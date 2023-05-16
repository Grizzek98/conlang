import random as r

SIMPLE_CONSONANTS = 'p', 'b', 'v', 'm', 'w', 'th', 'tj', 't', 'd', 's', 'n', 'l', 'sh', 'sj', 'ch', 'cj','j', 'k', 'g', 'h'
ALL_CONSONANTS = 'p', 'b', 'v', 'm', 'w', 'th', 'tj', 't', 'd', 's', 'n', 'l', 'sh', 'sj', 'ch', 'cj','j', 'k', 'g', 'h', 'ts', 'tl', 'hl', 'r'
VOWELS = 'a', 'e', 'i', 'o', 'u'

SYLLABLE_TYPES = 'CVC', 'CVC', 'CVC', 'CV', 'CV', 'CV', 'VC','VC','VC', 'V','V'
VERB_END_SYLLABLE_TYPES = 'CV','CV','CV', 'V', 'V', 'V', 'CCV', 'CCV'


def create_syllable(s_type, c_type):
    r_syl = r.sample(s_type, 1)[0]
    temp_result = ''
    for i in range(len(r_syl)):
        match r_syl[i]:
            case 'C':
                temp_result = temp_result + r.sample(c_type, 1)[0]
            case 'V':
                temp_result = temp_result + r.sample(VOWELS, 1)[0]
    return temp_result

def create_adjective(num_words):
    while True:
        print('Number of syllables? (must be > 1)')
        num_syl = input('>')
        try: num_syl = int(num_syl)
        except: print('Enter an int.')

        print('Related to noun? (y/n)')
        noun_rel = input('> ')
        if noun_rel in ['y', 'n']:
            if noun_rel == 'n': noun_rel = False

            if num_syl >= 2:
                for i in range(num_words):
                    f_syl = True
                    result = ''
                    temp_syl = num_syl
                    for syl in range(num_syl):
                        if f_syl: 
                            if noun_rel: result = result + 'du'
                            else: result = result + 'dia'
                            temp_syl -= 1
                            f_syl = False
                        elif syl == num_syl - 1:
                            result = result + create_syllable(SYLLABLE_TYPES, SIMPLE_CONSONANTS)
                            temp_syl -= 1
                        else:
                            result = result + create_syllable(SYLLABLE_TYPES, ALL_CONSONANTS)
                            temp_syl -= 1
                    print(result)
                return

def create_noun(num_words):
    while True:
        print('Number of syllables?')
        num_syl = input('>')
        try: num_syl = int(num_syl)
        except: print('Enter an int.')
        if num_syl >= 1:
            for i in range(num_words):
                f_syl = True
                result = ''
                temp_syl = num_syl
                for syl in range(num_syl):
                    if f_syl or syl == num_syl - 1: 
                        result = result + create_syllable(SYLLABLE_TYPES, SIMPLE_CONSONANTS)
                        temp_syl -= 1
                        f_syl = False
                    else:
                        result = result + create_syllable(SYLLABLE_TYPES, ALL_CONSONANTS)
                        temp_syl -= 1
                print(result)
            return
    
def create_verb(num_words):
    while True:
        print('Number of syllables?')
        num_syl = input('>')
        try: num_syl = int(num_syl)
        except: print('Enter an int.')
        if num_syl >= 1:
            for i in range(num_words):
                f_syl = True
                result = ''
                temp_syl = num_syl
                if temp_syl == 1 and f_syl: result = result + create_syllable(VERB_END_SYLLABLE_TYPES, SIMPLE_CONSONANTS) + 'l'
                else:
                    for syl in range(num_syl):
                        if f_syl: 
                            result = result + create_syllable(SYLLABLE_TYPES, SIMPLE_CONSONANTS)
                            temp_syl -= 1
                            f_syl = False
                        elif temp_syl == 1:
                            result = result + create_syllable(VERB_END_SYLLABLE_TYPES, ALL_CONSONANTS) + 'l'
                            temp_syl -= 1
                        else:
                            result = result + create_syllable(SYLLABLE_TYPES, ALL_CONSONANTS)
                            temp_syl -= 1
                print(result)
            return

def main():
    print('Welcome to the Elothian Word Generator!')
    while True:
        print('verb, noun, or adjective?')
        word_type = input('> ')
        if word_type in ['verb', 'noun', 'adjective', 'test']:
            num_words = '0'
            while num_words == 0 or num_words != type(int):
                print('Number of words?')
                num_words = input('> ')
                try: num_words = int(num_words)
                except: print('Enter an int.')
                if num_words != 0 and isinstance(num_words, int):
                    match word_type:
                        case 'verb':
                            create_verb(num_words)
                        case 'noun':
                            create_noun(num_words)
                        case 'adjective':
                            create_adjective(num_words)
                break

if __name__ == '__main__':
    main()