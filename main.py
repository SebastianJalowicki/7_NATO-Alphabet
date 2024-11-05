import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
dict_data = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dict_data)

def generate_phonetic():
    user_input = input('Enter a word: ').upper()
    try:
        list_alphabet = [dict_data[letter] for letter in user_input]
    except KeyError:
        is_true = False
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(list_alphabet)

generate_phonetic()