import xlrd 
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def svm_classifier(reviews, sentiment):
    clf = svm.SVC()
    encoder = LabelEncoder()
    reviews = encoder.fit_transform(reviews)
    sentiment = encoder.fit_transform(sentiment)

    sentence = []
    for w in reviews:
        sentence.append([w])

    X_train, X_test, y_train, y_test = train_test_split(sentence, sentiment, test_size=0.2)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print('Accuracy score : ' + str(accuracy_score(y_test,y_pred)))
    print('\nConfusion matrix :\n' + str(confusion_matrix(y_test,y_pred)))
    print('\n\nClassification Report : \n' + str(classification_report(y_test, y_pred)))

from skle3arn.linear_model import LogisticRegression

def lr_classifier(reviews, sentiment):
    encoder = LabelEncoder()
    reviews = encoder.fit_transform(reviews)
    sentiment = encoder.fit_transform(sentiment)

    sentence = []
    for w in reviews:  
        sentence.append([w])
    X_train, X_test, y_train, y_test = train_test_split(sentence, sentiment, test_size=0.2)
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print('Accuracy score : ' + str(accuracy_score(y_test,y_pred)))
    print('\nConfusion matrix :\n' + str(confusion_matrix(y_test,y_pred)))
    print('\n\nClassification Report : \n' + str(classification_report(y_test, y_pred)))

#import tensorflow as tf
#from keras.models import Sequential
#from keras.layers import Dense, LSTM

def text_classification():
    loc = ('../Datasets/Preprocessed_data.xls') 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    reviews = sheet.col_values(1)
    sentiment = sheet.col_values(2)
    print('Logistic regression ')
    lr_classifier(reviews, sentiment)
    print("*" * 80)
    print('\nSupport vector machine')
    svm_classifier(reviews, sentiment)
    '''
    embed_dim = 128
    lstm_out = 200
    batch_size = 32

    model = Sequential()
    model.add(Embedding(2500, embed_dim,input_length = reviews.shape[1], dropout = 0.2))
    model.add(LSTM(lstm_out, dropout_U = 0.2, dropout_W = 0.2))
    model.add(Dense(2,activation='softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
    print(model.summary())
    X_train, X_valid, Y_train, Y_valid = train_test_split(reviews, sentiment, test_size = 0.20, random_state = 36)
    model.fit(X_train,Y_train,batch_size= batch_size, 1, 1, validation_data=(X_valid, Y_valid), shuffle=True)
    predicted = model.predict(X_valid, batch_size=batch_size)
    print('Accuracy score : ' + str(accuracy_score(Y_valid,predicted)))
    print('\nConfusion matrix :\n' + str(confusion_matrix(Y_valid,predicted)))
    print('\n\nClassification Report : \n' + str(classification_report(Y_valid,predicted)))
    '''

text_classification()