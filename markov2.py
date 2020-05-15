from random import random, randint

import numpy as np

# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
trump = open('nathan_for_you.txt', encoding='utf8').read()

corpus = trump.split()


def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield corpus[i], corpus[i + 1]


pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]


if __name__ == '__main__':
    for k in range(50):

        first_word = 'Hot'
        first_phrase = ['Hot', 'Pockets']
        chain = first_phrase + [np.random.choice(corpus) for k in range(randint(0, 2))]
        title = ' '.join(chain)

        n_words = randint(25, 100)

        for i in range(n_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))

        rabble = ' '.join(chain)
        print(f'The {title}:', end='\n\n')
        print(' '.join(chain).replace('.', '.\n'), end='\n\n')
        print('-'*250)
