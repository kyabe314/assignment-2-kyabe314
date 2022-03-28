import urllib.request
import io
import string
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Project Gutenberg
# main_url = https://www.gutenberg.org

# The Wealth of Nations by Adam Smith
# Retrieve the content from the Internet and make it parsable by Python

url = 'https://www.gutenberg.org/files/3300/3300-0.txt'
response = urllib.request.urlopen(url)
data = response.read( ) # This is a 'bytes' object, not the text itself
WON_text = data.decode('utf-8')


nlines = WON_text.count('\n')
# print(nlines)



def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    filename = filename.split('\n')

    if skip_header:
        skip_gutenberg_header(filename)

    strippables = string.punctuation + string.whitespace
    # print(filename)
    for line in filename:
        line = line.strip()
        if line.startswith('*** END OF THIS PROJECT'):
            break
        
        line = line.replace('-', ' ')
        for word in line.split():
            # word could be 'Sussex.'

            # print(word)

            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    
    return hist


def skip_gutenberg_header(fp):
    """
    Reads from fp until it finds the line that ends the header.

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


def most_common(hist, excluding_stopwords=False, num=10):
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
    # print(lst)
    for i in range(0, num - 1):
        # print(i)
        # print(lst[i])
        print(f'The word "{lst[i][1]}" appears {lst[i][0]} times in this book.')

    return lst

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    # print(hist)
    for freq, word in hist[0:num]:
        print(word, '\t', freq)

def all_dictionary():
    """
    Read in the word.txt file and create a dictionary of it
    """
    
    dictionary = dict()
    fp = open('data/words.txt', encoding='UTF8')
    print(fp)
    fp = fp.split()

    for line in fp:
        dictionary[line] = dictionary.get(line, 0) + 1

    return dictionary

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

def sentiment_analysis(filename, skip_header):
    """
    
    """
    filename = filename.split('\n')

    if skip_header:
        skip_gutenberg_header(filename)

    # print(filename)
    for line in filename:
        line = line.strip()
        if line.startswith('*** END OF THIS PROJECT'):
            break
        
        line = line.replace('-', ' ')
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        print(score)



def main():
    hist = process_file(WON_text, skip_header=True)
    # print(hist)
    print('This book is an statistical analysis of The Wealth of Nations by Adam Smith')
    print(f'The total number of words included in this text is {total_words(hist)} words.')
    print(f'The number of unique words included in this text is {different_words(hist)} words.')
    unique_to_total = different_words(hist)/total_words(hist)*100
    print(f'The percentage of unique words within this text are {unique_to_total:.2f}%.')
    print(f'On average, each unique word is used {100/unique_to_total:.2f} times in the text.')
    print()
    print(f'The 10 most common words used in this text are as follows:')
    most_common(hist, excluding_stopwords=True)
    # print(most_common(hist, excluding_stopwords=True))
    # print(all_dictionary())
    # sentiment_analysis(WON_text,skip_header=True)
    # sentence = 'Software Design is my favorite class because learning Python is so cool!'
    # score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    # print(score)
    

if __name__ == '__main__':
    main()