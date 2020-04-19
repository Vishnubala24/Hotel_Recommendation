import xlrd 
import nltk

# Read file
loc = ('../Datasets/Preprocessed_data.xls') 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
review_text = sheet.col_values(1)
#review_text = preprocess.preprocess(review_text)
#print(review_text[:3])

# Grouping the hotels : with hotel name as key and value is review tokens as list 
def group_by_hotel():
    hotels = sheet.col_values(0)
    unique_hotel = set(hotels) # 256 - total no. of hotels
    print(len(unique_hotel))
    review_dict = {}
    reviews = review_text
    for i in range(1,len(reviews)):
        if hotels[i] in review_dict:
            review_dict[hotels[i]] += reviews[i].split()
        else:
            review_dict[hotels[i]] = reviews[i].split()
    #print(review_dict)
    return review_dict #print(review_dict['Accord Metropolitan'])

import gensim
from gensim import corpora

# Extraction of features through LDA from the preprocessed data - For all the hotels
def topic_modelling():
    hotel_rev_dict = group_by_hotel()
    doc_clean = []
    for k,v in hotel_rev_dict.items():
        val = []
        v = nltk.pos_tag(v)
        #print(v)
        for x,y in v:
            #if(y=='NN'):
            val.append(x)
        doc_clean.append(val)
    #print(doc_clean[0]) # size: 256
    dictionary = corpora.Dictionary(doc_clean)
    dictionary.save('foobar.txtdic')
    #print(hotel_rev_dict)
    #print(dictionary)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    #print("="*80)
    #print(doc_term_matrix)
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=10, id2word = dictionary, passes=50)
    print(ldamodel.print_topics(num_topics=10, num_words=3))
    #topics = ldamodel.print_topics(num_topics=10, num_words=3)
    topics = ['good room', 'good staff', 'comfort stay', 'food']

topic_modelling()
print("*"* 80)
from sklearn.preprocessing import MinMaxScaler


def filteredValues(recommended, hotel_rev_dict):
    hotels = []
    scores = []
    for (h,s) in recommended:
        hotels.append(h)
        scores.append(s)
    return [hotels, hotel_rev_dict, scores]


def extract_reviews(feature, hotel_name=None):    
    # Read file
    loc1 = ('../Datasets/review_scores.xlsx') 
    wb1 = xlrd.open_workbook(loc1) 
    sheet1 = wb1.sheet_by_index(0)
    hotels = sheet1.col_values(0)
    reviews = sheet1.col_values(1)
    scores = sheet1.col_values(4)
    print(hotel_name)
    pos_feature = {}
    hotel_review_dict = {}
    pos_scores = []
    pos = 0
    for i in range(1, len(hotels)):
        if(hotel_name != None):
            if(hotel_name == hotels[i] and (feature in reviews[i].split()) and scores[i]>0):
                pos += scores[i]
                #print(reviews[i])
                #print('\n\n')
        else:
            if((feature in reviews[i].split()) and scores[i]>0):
                #print(str(hotels[i])+' : '+str(reviews[i]))
                #print('\n\n')
                if(hotels[i] not in pos_feature):
                    pos_feature[hotels[i]] = scores[i]
                    hotel_review_dict[hotels[i]] = [reviews[i]]
                else:
                    pos_feature[hotels[i]] += scores[i]
                    hotel_review_dict[hotels[i]].append(reviews[i])

    if(hotel_name==None):
        for k,v in pos_feature.items():
            pos_scores.append([v])
        scaler = MinMaxScaler(feature_range=(0,5))
        scaler.fit(pos_scores)
        pos_scores = scaler.transform(pos_scores)
        i = 0
        for k,v in pos_feature.items():
            pos_feature[k] = round(pos_scores[i][0])
            i += 1
        recommend = sorted(pos_feature.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
        
        return filteredValues(recommend, hotel_review_dict)

# extract_reviews('room')


'''
def topic_modelling_particular_hotel(hotel_name):
    hotel_rev_dict = group_by_hotel()
    doc_clean = []
    value = hotel_rev_dict[hotel_name]
    #print(value)
    doc_clean.append(value)
    dictionary = corpora.Dictionary(doc_clean)
    #print(hotel_rev_dict)
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
    print(ldamodel.print_topics(num_topics=5, num_words=3))
#topic_modelling_particular_hotel('Accord Metropolitan')
'''
#topic_modelling()

