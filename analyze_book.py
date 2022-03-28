from pickle import NONE
import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    result = 0
    for v in hist.values():
        result += v
    return result


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    stopwords = process_file('data/stopwords.txt', skip_header=False)
    lst = list()
    for k, v in hist.items():
        if excluding_stopwords:
            if k in stopwords:
                continue
            else:
                lst.append((v, k))
    lst.sort(reverse=True)

    return lst



def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    # print(hist)
    for freq, word in hist[0:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """
    Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    ex_search = dict()
    for k, v in d1.items():
        if not k in d2.keys():
            ex_search[k] = v
    
    return ex_search


def random_word(hist):
    """
    Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    counter = 0
    for _ in hist.items():
        counter += 1
    # index -> from 0 to counter - 1

    random_number = random.randint(0, counter - 1)
    print(random_number)
    list_keys = list(hist.keys())
    # print(type(list_keys), list_keys)
    list_values = list(hist.values())


    return list_keys[random_number], str((list_values[random_number]/counter)*100) + '%'

    


def main():
    hist = process_file('data/Pride and Prejudice.txt', skip_header=True)
    # print(hist[0])
    # print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    print()
    print_most_common(t, num = 10)

    words = process_file('data/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    # main()
    pass
