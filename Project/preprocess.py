# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:02:57 2019

@author: User
"""

import xlrd 
from xlwt import Workbook 
import re
import string
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Read file
loc = ('../Datasets/chennai_reviews.xlsx') 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) # sheet contains reference
#print(sheet.cell_value(0, 0))
#print(sheet.nrows)
#print(sheet.ncols)  
#print(sheet.row_values(1))
#print(sheet.col_values(1))

review_text = sheet.col_values(1)
#print(review_text[1])

def conv_to_lowercase(reviews):
    for i in range(0,len(reviews)):
        reviews[i] = reviews[i].lower()
    return reviews

def remove_noise(reviews):
    for i in range(0,len(reviews)):
        reviews[i] = re.sub(r'\d+', '',reviews[i]) # Replaces one or many matches with a string - Removes numbers
        reviews[i] = reviews[i].translate((str.maketrans('', '', string.punctuation))) # Removing punctuations
        reviews[i] = reviews[i].strip()
    return reviews

def remove_stopwords(reviews):
    stop_words = set(stopwords.words('english'))
    filtered_reviews = []
    for i in range(0,len(reviews)):
        text = reviews[i]
        tokens = nltk.word_tokenize(text)
        filtered_tokens = []
        for word in tokens:
            if word not in stop_words:
                filtered_tokens.append(word)
        filtered_reviews.append(filtered_tokens)
    return filtered_reviews

def stemming(filt_reviews):
    stemmer= PorterStemmer()
    for i in range(len(filt_reviews)):
        for j in range(len(filt_reviews[i])):
            filt_reviews[i][j] = stemmer.stem(filt_reviews[i][j])
    return filt_reviews

def lemmatization(filt_reviews):
    lemmatizer=WordNetLemmatizer()
    for i in range(len(filt_reviews)):
        for j in range(len(filt_reviews[i])):
            filt_reviews[i][j] = lemmatizer.lemmatize(filt_reviews[i][j])
    return filt_reviews

def write_to_file(reviews):
    pd.DataFrame(reviews).to_excel('preprocessed_reviews.xlsx', header=False, index=False)

def pos_tagging(reviews):
    tagged_reviews = []
    #nltk.download('averaged_perceptron_tagger')
    for review in reviews:
        tagged_reviews.append(nltk.pos_tag(review))
    return tagged_reviews

def extract_feature(reviews,feature):
    feature_list = []
    r_idx = []
    for i in range(1,len(reviews)):
        for x,y in reviews[i]:
            if(y=='NN' and x==(feature.lower())):
                feature_list.append(reviews[i])
                r_idx += [i]
                break
    print(feature_list[:5])
    for i in range(0,5):
        print(review_text[r_idx[i]])

def write_preprocessed_data(reviews):
    wb1 = Workbook() 
    sheet1 = wb1.add_sheet('Sheet 1') 
    hotelname = sheet.col_values(0)
    sentiment = sheet.col_values(2)
    rating_percent = sheet.col_values(3)
    for i in range(len(reviews)):
        sheet1.write(i, 0, hotelname[i])
        sheet1.write(i, 1, ' '.join(reviews[i]))
        sheet1.write(i, 2, sentiment[i])
        sheet1.write(i, 3, rating_percent[i])
    wb1.save('../Datasets/Preprocessed_data.xls') 

def preprocess(reviews):
    reviews = conv_to_lowercase(reviews)
    print('Converted to Lower case')
    print(reviews[1])
    reviews = remove_noise(reviews)
    print('Removed noise ')
    print(reviews[1])
    filtered_reviews = remove_stopwords(reviews)
    print('Stop words removed')
    print(filtered_reviews[1])
    stem_reviews = stemming(filtered_reviews)
    print('After stemming')
    print(stem_reviews[:5])
    tagged_reviews = pos_tagging(stem_reviews)
    print('POS tagging')
    print(tagged_reviews[1])
    print("\n\n")
    #write_preprocessed_data(stem_reviews)
    #return stem_reviews

    #extract_feature(tagged_reviews,'place')
    #print(tagged_reviews[:5])
    #lem_reviews = lemmatization(filtered_reviews)
    #print(lem_reviews[1])
    #write_to_file(stem_reviews)



preprocess(review_text)

'''
# generating training dataset ( word dictionary)

def stemm(filt_reviews):
    stemmer= PorterStemmer()
    for i in range(1,len(filt_reviews)):
        filt_reviews[i] = stemmer.stem(filt_reviews[i])
    return filt_reviews

words = ('../Datasets/positive.xlsx')
wb = xlrd.open_workbook(words)
sheet = wb.sheet_by_index(0)
positive = sheet.col_values(0)
negative = sheet.col_values(2)
s_pos = stemm(positive)
s_neg = stemm(negative)

#print(set(s_pos))
s_pos = list(set(s_pos))
s_neg = list(set(s_neg))
l_pos = []
l_neg = []
for p in s_pos:
    t = [p]
    t.append('positive')
    l_pos.append(t)

for n in s_neg:
    t = [n]
    t.append('negative')
    l_neg.append(t)
print(l_neg)

for neg in l_neg:
    l_pos.append(neg)

import pandas as pd
pd.DataFrame(l_pos).to_excel('train.xlsx', header=False, index=False)
'''