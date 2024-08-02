#load dataset
import pandas
data = pandas.read_csv('SMSSpamCollection.txt', sep='\t', header=None, names=["label", "sms"])


#load stopwords and punctuation
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')

stopwords = nltk.corpus.stopwords.words('english')
punctuation = string.punctuation

#pre-process sms content
def pre_process(sms):
    lowercase = "".join([char.lower() for char in sms if char not in punctuation])
    tokenize = nltk.tokenize.word_tokenize(lowercase)
    remove_stopwords = [word for word in tokenize if word not in stopwords]
    return remove_stopwords

data['processed'] = data['sms'].apply(lambda x: pre_process(x))

#categorizing ham/spam associated words
def categorize_words():
    spam_words = []
    ham_words = []

    #spam associated words
    for sms in data['processed'][data['label'] == 'spam']:
        for word in sms:
            spam_words.append(word)

    #ham associated words
    for sms in data['processed'][data['label'] == 'ham']:
        for word in sms:
            ham_words.append(word)
    
    return spam_words, ham_words

spam_words, ham_words = categorize_words()

#itterate over all the words from the user input and count their occurances in both spam_words and ham_words
def predict(user_input):
    spam_counter = 0
    ham_counter = 0

    for word in user_input:
        spam_counter += spam_words.count(word)
        ham_counter += ham_words.count(word)

    print('****************RESULT****************')
    if ham_counter > spam_counter:
        #adding accuracy
        accuracy = round((ham_counter/(ham_counter + spam_counter)) * 100, 2)
        print('The message is not Spam, with {}% accuracy'.format(accuracy))
    elif spam_counter > ham_counter:
        accuracy = round((spam_counter/(ham_counter + spam_counter)) * 100, 2)
        print('The message is Spam with {}% accuracy'.format(accuracy))
    else:
        print('The message could be Spam with 50% accuracy')

#collect user input
user_input = input('Please type a spam or ham message to make sure the function works properly\n')
processed_input = pre_process(user_input)
predict(processed_input)