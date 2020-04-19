import xlrd 
import nltk
from sklearn.preprocessing import LabelEncoder
import pandas as pd

from afinn import Afinn
import textwrap
import openpyxl
 
# Calculating AFINN scores for all the reviews and generating a new file 'review_scores.xlsx'
def afinn_score():
    afinn = Afinn()
    loc1 = ('../Datasets/chennai_reviews.xlsx') 
    wb1 = xlrd.open_workbook(loc1) 
    sheet1 = wb1.sheet_by_index(0) 
    reviews = sheet1.col_values(1)
    wbkName = '../Datasets/review_scores.xlsx'
    wbk = openpyxl.load_workbook(wbkName)
    scored_reviews = []
    for review in reviews:
        scored_reviews.append((review, afinn.score(review)))
    for wks in wbk.worksheets:
        for i in range(len(scored_reviews)):
            x,y = scored_reviews[i]
            #print(scored_reviews[i])
            wks.cell(row=i+1, column=5).value = y
    wbk.save(wbkName)
    wbk.close
    #print(scored_reviews[:5])
#afinn_score()


# Grouping and generating scores for hotels : score_dict = { 'hotel_name' : [pos, neg] }
def hotel_score():
    loc1 = ('../Datasets/review_scores.xlsx') 
    wb1 = xlrd.open_workbook(loc1) 
    sheet1 = wb1.sheet_by_index(0) 
    hotel = sheet1.col_values(0)
    scores = sheet1.col_values(4)
    score_dict = {} 
    for i in range(1,len(scores)):
        if(hotel[i] in score_dict):
            if(scores[i] >= 0):
                score_dict[hotel[i]][0] = score_dict[hotel[i]][0] + scores[i]
            else:
                score_dict[hotel[i]][1] = score_dict[hotel[i]][1] + scores[i]
        else:
            if(scores[i] >= 0):
                score_dict[hotel[i]] = [scores[i], 0]
            else:
                score_dict[hotel[i]] = [0, scores[i]]
    #print(score_dict)
    return score_dict

from sklearn.preprocessing import MinMaxScaler

# Normalizing the scores in range (-5,0) for negative and (0,5) for positive reviews
def normalize(score_dict):
    pos_scores = []
    neg_scores = []
    for k, v in score_dict.items():
        pos_scores.append([v[0]])
        neg_scores.append([v[1]])
    scaler = MinMaxScaler(feature_range=(0,5))
    scaler.fit(pos_scores)
    pos_scores = scaler.transform(pos_scores)
    scaler = MinMaxScaler(feature_range=(-5,0))
    scaler.fit(neg_scores)
    neg_scores = scaler.transform(neg_scores)
    i = 0
    for k,v in score_dict.items():
        score_dict[k] = [round(pos_scores[i][0], 2), round(neg_scores[i][0], 2)]
        i += 1
    #print(score_dict)
    return score_dict

import numpy as np
import matplotlib.pyplot as plt

# Ploting the graph for top 5 recommended hotels
def plot_graph(hotel, pos, neg):
    n_groups = 5
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    positive_bar = plt.bar(index, pos, bar_width,
    alpha=opacity,
    color='g',
    label='Positive')

    negative_bar = plt.bar(index + bar_width, neg, bar_width,
    alpha=opacity,
    color='r',
    label='Negative')

    plt.xlabel('Hotel')
    plt.ylabel('Scores')
    plt.title('Hotel scores')
    plt.xticks(index , hotel)
    plt.legend()
    plt.tight_layout()
    plt.show()

hotel_rating = {}

# Recommends the hotels 
def recommend_hotel():
    scores = hotel_score()
    score_dict = normalize(scores)
    recommend = sorted(score_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    global hotel_rating 
    hotel_rating = recommend
    #print(recommend)
    hotel = []
    pos = []
    neg = []
    for i in range(len(recommend)):
        x , y = recommend[i]
        if(len(hotel)>=5):
            break
        hotel.append(x)
        pos.append(y[0])
        neg.append(y[1])
    print("*"*50)
    print('Recommended Hotels')
    print("*"*50)
    for h in hotel:
        print(h)
    print("*"*50)
    return recommend
    #plot_graph(hotel, pos, neg)
    
def group_reviews():
    loc1 = ('../Datasets/chennai_reviews.xlsx') 
    wb1 = xlrd.open_workbook(loc1) 
    sheet = wb1.sheet_by_index(0)
    reviews = sheet.col_values(1)
    hotels = sheet.col_values(0)
    unique_hotel = set(hotels) # 256 - total no. of hotels
    print(len(unique_hotel))
    review_dict = {}
    for i in range(1,len(reviews)):
        if hotels[i] in review_dict:
            review_dict[hotels[i]].append(reviews[i])
        else:
            review_dict[hotels[i]] = [reviews[i]]
    #print(review_dict)
    return review_dict #print(review_dict['Accord Metropolitan'])

def summarize():
    recommend = recommend_hotel()
    hotels = []
    scores = []
    reviews = group_reviews()
    for i in range(len(recommend)):
        x , y = recommend[i]
        hotels.append(x)
        scores.append(y[0])
    return [hotels, reviews, scores]


print(hotel_rating)
#lstm_classifier()
import nltk
from nltk.corpus import wordnet

def find_related_words():
    words = []
    for w in wordnet.synsets('food'):
        for l in w.hyponyms():
            words.append(l.name())
    print('\n\n')
    print(set(words))
# find_related_words()