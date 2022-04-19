import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize

def tokenizer(text):
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    filtered_words = list(filter(lambda token: token not in stopwords, tokens))
    return filtered_words
    
def positive_score(text):
    Positive_Words = 0
    token = tokenizer(text)
    for word in token:
        if word in positive:
            Positive_Words  += 1
    
    sum_of_positive = Positive_Words
    return sum_of_positive
   
def negative_score(text):
    Negative_Words=0
    Token = tokenizer(text)
    for word in Token:
        if word in negative:
            Negative_Words -=1
    sum_of_negative = Negative_Words 
    sum_of_negative = sum_of_negative * -1
    return sum_of_negative
    
def polarity_score(positiveScore, negativeScore):
    polarity_score = (positiveScore - negativeScore) / ((positiveScore + negativeScore) + 0.000001)
    return polarity_score
    
def subjectivity_score(positiveScore, negativeScore, text):
    filtered_words = len(text)
    subjective_score = (positiveScore + negativeScore)/ ((filtered_words) + 0.000001)
    return subjective_score
   
def average_sentence_length(text):
    sentences = sent_tokenize(text)
    tokens = tokenizer(text)
    WordCount = len(tokens)
    totalSentences = len(sentences)
    avg_sentence = 0
    if totalSentences != 0:
        avg_sentence = WordCount / totalSentences
    avg_sentence_length = avg_sentence
    return round(avg_sentence_length)
    
def percentage_complex_word(text):
    tokens = tokenizer(text)
    complexWord = 0
    complex_word_percentage = 0
    
    for word in tokens:
        vowels=0
        if word.endswith(('es','ed')):
            pass
        else:
            for w in word:
                if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
                    vowels += 1
            if(vowels > 2):
                complexWord += 1
    if len(tokens) != 0:
        complex_word_percentage = complexWord/len(tokens)
    return complex_word_percentage
    
def fog_index(avgSentenceLength, percentageComplexWord):
    fogIndex = 0.4 * (avgSentenceLength + percentageComplexWord)
    return fogIndex
    
def avg_words_per_sentence(text):
    sentences = sent_tokenize(text)
    tokens = tokenizer(text)
    WordCount = len(tokens)
    totalSentences = len(sentences)
    avg_sentence = 0
    if totalSentences != 0:
        words_per_sentence = WordCount/totalSentences
    words_per_sentence_avg = words_per_sentence
    
    return round(words_per_sentence_avg)

def complex_word_count(text):
    tokens = tokenizer(text)
    complexWord = 0
    
    for word in tokens:
        vowels=0
        if word.endswith(('es','ed')):
            pass
        else:
            for w in word:
                if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
                    vowels += 1
            if(vowels > 2):
                complexWord += 1
    return complexWord
   
def total_word_count(text):
    tokens = tokenizer(text)
    return len(tokens)
    
def syllables_per_word(text):
    tokens = tokenizer(text)
    syllables = 0
    
    for word in tokens:
        if word.endswith(('es','ed')):
            pass
        else:
            for w in word:
                if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
                    syllables += 1
    syllable_per_word = syllables/len(tokens)
    return syllable_per_word
    
    
def syllables_per_word(text):
    tokens = tokenizer(text)
    syllables = 0
    
    for word in tokens:
        if word.endswith(('es','ed')):
            pass
        else:
            for w in word:
                if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
                    syllables += 1
    syllable_per_word = syllables/len(tokens)
    return syllable_per_word
    
def avg_word_length(text):
    tokens = tokenizer(text)
    word_count = len(tokens)
    word_avg_length = len(text)/word_count
    return word_avg_length
