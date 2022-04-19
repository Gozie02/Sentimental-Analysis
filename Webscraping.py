#Import relevant libraries

import csv
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize

from Dictionaries import stopwords, positive, negative
from Variables import tokenizer, positive_score, negative_score, polarity_score, subjectivity_score, average_sentence_length, percentage_complex_word, fog_index, avg_words_per_sentence, complex_word_count, total_word_count, syllables_per_word, avg_word_length
    
a = 'URL' #This is to ignore any rows containing URL in text
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
#header workaround for security error

with open(r'C:/Users/HP/Desktop/Output Data.csv', 'w', newline='') as file:#creating our output data file
    writer = csv.writer(file)
    writer.writerow(["URL_ID", "URL", "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE", 
                     "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX", "AVG NUMBER OF WORDS PER SENTENCE", 
                     "COMPLEX WORD COUNT", "WORD COUNT", "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH" ])

read_file = pd.read_excel (r'C:/Users/HP/Downloads/Input.xlsx')
read_file.to_csv (r'C:/Users/HP/Downloads/Input.csv', index = None, header=True)
with open('C:/Users/HP/Downloads/Input.csv', encoding='utf-8') as csvfile:#open csv
    reader = csv.reader(csvfile, delimiter = ',') #checks csv with delimiter and reads accurately
    for row in reader: #for all the rows in the csv
        if any([a in row]):#if any of the rows have URL
            pass #ignore them for now
        else:
            url = row[1] #gets all links in the url column one by one
            response = requests.get(url, headers = headers)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser') #parse the html file from the link
            souptitle = soup.find("h1", class_ = 'entry-title').get_text().encode("utf-8") #get title by using tags on the html page, this is only used bc the structure of all the sites are the same
            souptext = soup.find("div", class_ = 'td-post-content').get_text().encode("utf-8") #get body, same explanation here#
            soupresult = souptitle + souptext #combine the gotten texts for easier coding
            cleanedsoupresult = BeautifulSoup(soupresult, "lxml").get_text(strip = True) #remove extraneous characters
            pScore = positive_score(cleanedsoupresult) #calculate positive score for each cleaned text
            nScore = negative_score(cleanedsoupresult) #calculate negative score for each cleaned text
            #nltk.download('punkt') #only uncomment this line when your nltk packages are incomplete
            averageSentenceLength = average_sentence_length(cleanedsoupresult) #calculation for each text
            percentageComplexWord = percentage_complex_word(cleanedsoupresult) #calculation for each text
            urlfilename = f'{row[0]}.txt' #this gives url_id.txt
            savetopath = os.path.join('C:/Users/HP/Desktop/Blackcoffer' , urlfilename) #sending each txt file to a folder
            with open(savetopath, "w", encoding = "utf-8") as file:
                file.write(str(cleanedsoupresult))#write cleaned text in each txt file
            with open(r'C:/Users/HP/Desktop/Output Data.csv', 'a') as file:
                writer = csv.writer(file)     
                writer.writerow([row[0], row[1], pScore, nScore, polarity_score(pScore, nScore), 
                                 subjectivity_score(pScore, nScore, cleanedsoupresult), averageSentenceLength, 
                                 percentageComplexWord, fog_index(averageSentenceLength, percentageComplexWord), 
                                 avg_words_per_sentence(cleanedsoupresult), complex_word_count(cleanedsoupresult), 
                                 total_word_count(cleanedsoupresult), syllables_per_word(cleanedsoupresult), 
                                 personal_pronouns(cleanedsoupresult), avg_word_length(cleanedsoupresult)]) #calculate variables
                
