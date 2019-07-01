import re
import numpy as np
import pickle

word2index = pickle.load(open('model/word2index.pkl','rb'))
model = pickle.load(open('model/linear_svm.pkl','rb'))
prob_model = pickle.load(open('model/prob_linear_svm.pkl','rb'))

def reduce_lengthening(text):
    '''
    An ad-hoc spellcheck. No swedish words contains more than two identical characters
    in a sequence. This method finds those and shortens them to two - irregardless of
    whether it's a noun or whatever. ALL occurrences are reduced to only two in order to
    ensure words that are commonly emphazised, i.e såååååå, are included in the vocabulary.
    '''
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

def cleanTweet(tweet):

    # Here we have each tweet. Process and add to file.

    # Replaces various URLs with "<URL>"
    filtered = re.sub(r"http\S+", " <URL>", tweet)

    # Replace mentions with anonymous <ID>
    filtered = re.sub(r"@\S+", " <ID>", filtered)

    # Replace haschtags with anonymous <HASCHTAG>
    filtered = re.sub(r"#\S+", " <HASCHTAG>", filtered)

    filtered = reduce_lengthening(filtered)

    # Replace each '-' and '/' with ' - ' and ' / ' because they are common in text
    filtered = filtered.replace("-", " - ")
    filtered = filtered.replace("/", " / ")

    filtered = re.sub('[\'&]+', '', filtered)

    #Remove non-alpha numerical and <> from tweet
    filtered = re.sub('[^0-9a-zA-Z åäöÅÄÖ<>]+', ' ', filtered)

    prev = ''
    sentence = ''
    for word in filtered.split():
        word = word.strip().lower()
        #word = stemmer.stem(word) #This stems the word

        if not (word == prev and (word == '<id>' or word == '<haschtag>' or word == '<url>')) and not word == 'amp':

            sentence = sentence + ' ' + word
        prev = word

    #print(sentence)
    return sentence.strip()

def getVector(tweet):
    vec = np.zeros([len(word2index), 1])
    for word in tweet.split():
        if word2index.get(word) is not None:
            vec[word2index.get(word)] += 1
        else:
            vec[word2index.get('UNK')] += 1
    return vec.reshape(1, len(word2index))
