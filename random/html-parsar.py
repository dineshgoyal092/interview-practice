import requests
from bs4 import BeautifulSoup
from collections import Counter


def count_most_freq_word(url,min_word_length=3,no_most_used_word=5):
    '''Function will scrape a given website and print top # most
    commonly used word whose length is grater than min_word_length '''

    wordlist = []
    scrap_data = requests.get(url).text

    # BeautifulSoup object which will
    # ping the requested url for data
    data = BeautifulSoup(scrap_data, 'html.parser')
    # print(data.get_text().strip())

    #extracting all the text from a page
    content = data.get_text().strip()
    words = content.lower().split()

    # we are only considering word whose length is greater than min_word_length
    for each_word in words:
        if len(each_word) > min_word_length:
            wordlist.append(each_word)

    c = Counter(wordlist)

    # returns the most occuring elements
    top = c.most_common(no_most_used_word)
    print(top)


# main code
if __name__ == '__main__':
    count_most_freq_word("https://acko.com/", 3,5)
