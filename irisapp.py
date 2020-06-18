#run the file using streamlit run


import streamlit as st
from sklearn import datasets
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""# Simple Iris Flower Prediction App""")                             # '#' used to signify header text
st.sidebar.header('User input parameters')                                      #header to be placed in the sidebar panel 

def user_input_features():                                                      #customized function to take in user values
    #four flower characteristics accepted from user by means of the slider bar
    sepal_length=st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)               #label text,  minimum value , maximum value , default 
    sepal_width=st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length=st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width=st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width':petal_width}
    features = pd.DataFrame(data,index=[0])
    return features



df=user_input_features()
st.subheader('User input parameters')                                           #assign subheader text
st.write(df)

iris=datasets.load_iris()
X=iris.data                                                                     #four flower features
Y=iris.target                                                                   #iris class labels    

clf=RandomForestClassifier()
clf.fit(X,Y)                                                                    #train the model using X, Y as the training set

prediction=clf.predict(df)
prediction_proba=clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
st.write(prediction)

st.subheader('Prediction Probability')                                          #relative confidence for the predicted class labels
st.write(prediction_proba)