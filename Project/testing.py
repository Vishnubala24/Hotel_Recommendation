# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:22:02 2019

@author: dell
"""

from afinn import Afinn
afinn = Afinn()

sentence = "I love cats, but I am allergic to them."
print(afinn.score(sentence))
print(afinn.comparative(sentence))
print(afinn.calculation(sentence))
print(afinn.tokens(sentence))
print(afinn.words(sentence))
'''
import spacy 
from spacy_symspell import SpellingCorrector

nlp = spacy.load('en_core_web_sm') 
corrector = SpellingCorrector() 
nlp.add_pipe(corrector) 
doc = nlp('What doyuoknowabout antyhing')
for s in doc._.suggestions:
    print(s) #What doyon about anything
'''
'''
import xlrd 
import re
import string
# Read file
loc = ('./real_data.xlsx') 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) # sheet contains reference
#print(sheet.cell_value(0, 0))
#print(sheet.nrows)
#print(sheet.ncols)  
#print(sheet.row_values(1))
#print(sheet.col_values(1))

review_text = sheet.col_values(4)
#print(review_text[1])

def conv_to_lowercase(reviews):
    for i in range(0,len(reviews)):
        reviews[i] = reviews[i].lower()
    return reviews

def remove_noise(reviews):
    for i in range(0,len(reviews)):
        reviews[i] =re.sub(r'\d+', '',reviews[i]) # Replaces one or many matches with a string
        reviews[i] = reviews[i].translate((str.maketrans('', '', string.punctuation))) # Removing punctuations
        reviews[i] = reviews[i].strip()
    return reviews

def preprocess(reviews):
    reviews = conv_to_lowercase(reviews)
    #print(reviews[1])
    reviews = remove_noise(reviews)
    print(reviews[1])
    
#preprocess(review_text)

city_type = {}
city = sheet.col_values(1)
hotel = sheet.col_values(2)
for c in city:
    if c in city_type:
        city_type[c] += 1
    else:
        city_type[c] = 1
#print(len(city_type))
#print(sorted(city_type.items(), key = lambda kv:(kv[1], kv[0])))   

hotel_dict = {}
max_city   = ('Orlando')#, 'San Francisco','New Orleans','Atlanta', 'Orlando')
#max_city   = ('San Diego')#, 'San Francisco','New Orleans','Atlanta', 'Orlando')
for i in range(len(hotel)):
    if city[i] in max_city:
        if hotel[i] in hotel_dict:
           hotel_dict[hotel[i]] += 1
        else:
            hotel_dict[hotel[i]] = 1
#print(len(hotel_dict))
#print(sorted(hotel_dict.items(), key = lambda kv:(kv[1], kv[0])))   

max_hotel = ('Homewood Suites by Hilton Lake Buena Vista-Orlando', 'Hilton Garden Inn Orlando Airport', 'Hampton Inn & Suites Orlando at SeaWorld', 'Days Inn By Wyndham Orlando/International Drive', 'Best Western Orlando East Inn & Suites',
             'Best Western Seven Seas', 'Hampton Inn San Diego Del Mar', 'Ocean Park Inn', 'The Pearl Hotel', 'Best Western Mission Bay', 
             'Galleria Park Hotel', 'Hotel Diva', 'Hotel Abri', 'The Orchard Garden Hotel', 'The St. Regis San Francisco', 
             'French Market Inn', 'St. James Hotel, an Ascend Hotel Collection Member', 'Drury Inn & Suites New Orleans', 'Best Western Plus French Quarter Landmark Hotel', 'Best Western Plus St Charles Inn', 
             'JW Marriott Atlanta Buckhead', 'Renaissance Atlanta Waverly Hotel & Convention Center','The Ritz-Carlton, Atlanta',
             'Wingate By Wyndham Atlanta Galleria Center','Quality Suites Buckhead Village')
             
data = []
for i in range(len(hotel)):
    if hotel[i] in max_hotel:
        data.append(sheet.row_values(i))

print(len(data))
#writing list into new excel sheet
#import pandas as pd
#pd.DataFrame(data).to_excel('real_data1.xlsx', header=False, index=False)
'''

'''
# Filtering out the words that exist only in word dict.
def generate_file():
    reviews = review_text
    path = ('train.xlsx') 
    wb1 = xlrd.open_workbook(path) 
    sheet1 = wb1.sheet_by_index(0) 
    words = sheet1.col_values(0)
    for review in reviews:
        for token in review:
            if token not in words:
                review.remove(token)
    return reviews
    #print(reviews[:5])
    #pd.DataFrame(reviews).to_excel('chennai_view2.xlsx', header=False, index=False)

from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import ngrams

def sentiment_analyser():
    loc1 = ('../Datasets/chennai_reviews.xlsx') 
    wb1 = xlrd.open_workbook(loc1) 
    sheet1 = wb1.sheet_by_index(0) 
    reviews = sheet1.col_values(1)
    sid = SentimentIntensityAnalyzer()
    for i in range(len(reviews)):
        print(reviews[i])
        tokens = ngrams(reviews[i].split(), 2)
        pos = neg = neu = 0
        for token in tokens:
            token = ' '.join(token)
            ss = sid.polarity_scores(token)
            pos += ss['pos']
            neg += ss['neg']
            neu += ss['neu']
        print('Positive : '+str(pos), end=' ')
        print('Negative : '+str(neg), end=' ')
        print('Neutral : '+str(neu), end='\n\n')
        if(i>5):
            break

#sentiment_analyser()
'''