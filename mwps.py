import pickle
import streamlit  as st
from streamlit-option-menu import option_menu

#loading the saved models.
wine_red_model = pickle.load(open('wine_quality_red.sav','rb'))
white_wine_model = pickle.load(open('white_wine_quality.sav','rb'))
#sidebar for navigate.

with st.sidebar:
    selected = option_menu('Multiple Wine Quality Prediction System',
    ['Red Wine Quality prediction','White Wine Quality prediction'],
    icons=['activity','person'],default_index=0)

#Red Wine Prediction Page.
if (selected=='Red Wine Quality prediction'):
    #Page title.
    st.title('Red Wine Quality prediction using ML.')

    #Getting the input data from the user.
    #columns for input fields.
    col1,col2,col3 =  st.columns(3)

    with col1:
        fixed_acidity = st.text_input("Fixed Acidity")
    with col2:
        volatile_acidity = st.text_input("Volatile Acidity")
    with col3:
        citric_acid = st.text_input("Citric Acidity")
    with col1:
        residual_sugar = st.text_input("Residual Sugar")
    with col2:
        chlorides = st.text_input("Chlorides")
    with col3:
        Free_sulfur_dioxide = st.text_input("Free Sulfur Dioxide")
    with col1:
        total_sulfur_dioxide = st.text_input("Total_Sulfur_Dioxide")
    with col2:
        density = st.text_input("Density")
    with col3:
        pH = st.text_input("PH value")
    with col1:
        sulphates = st.text_input("Sulphates")
    with col2:
        alcohol = st.text_input("Alcohol")
    
    #Code for prediction.
    wine_red = ""
    #creating a button for prediction.
    if st.button('Best Wine quality result'):
        wine_red_prediction = wine_red_model.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,Free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])

        if (wine_red_prediction[0]==1):
            wine_red="This Red Wine Quality is Best."
        else:
            wine_red="This Red Wine Quality is Poor."
    st.success(wine_red)

#White Wine Prediction Page.
if (selected=='White Wine Quality prediction'):
    #Page title.
    st.title('White Wine Quality prediction using ML.')

    #Getting the input data from the user.
    #columns for input fields.
    col1,col2,col3 =  st.columns(3)

    with col1:
        fixed_acidity = st.text_input("Fixed Acidity")
    with col2:
        volatile_acidity = st.text_input("Volatile Acidity")
    with col3:
        citric_acid = st.text_input("Citric Acidity")
    with col1:
        residual_sugar = st.text_input("Residual Sugar")
    with col2:
        chlorides = st.text_input("Chlorides")
    with col3:
        Free_sulfur_dioxide = st.text_input("Free Sulfur Dioxide")
    with col1:
        total_sulfur_dioxide = st.text_input("Total_Sulfur_Dioxide")
    with col2:
        density = st.text_input("Density")
    with col3:
        pH = st.text_input("PH value")
    with col1:
        sulphates = st.text_input("Sulphates")
    with col2:
        alcohol = st.text_input("Alcohol")
    
    #Code for prediction.
    wine_white = ""
    #creating a button for prediction.
    if st.button('Best Wine quality result'):
        wine_white_prediction = white_wine_model.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,Free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])

        if (wine_white_prediction[0]==1):
            wine_white="This White Wine Quality is Best."
        else:
            wine_white="This White Wine Quality is Poor."
    st.success(wine_white)
