import streamlit as st
#conda install statsmodels
#pip install statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats


st.set_page_config(page_title='Caryt Marketing Co. Super Bowl Advertisement Optimizer',
                   page_icon='https://i.ibb.co/ry0gwGD/caryt-logo-secondary.png',
                   layout="wide")


# streamlit run C:\Users\brown\Desktop\MSDS\Capstone\predict.py

model = sm.load('./usa_today_model')

model_inputs = {
    'mood_funny':0,
    'industry_virtual_assistants':0,
    'industry_cars1':0,
    'mood_heartwarming':0,
    'mood_weird':0,
    'n_nfl':0,
    'industry_entertainment':0,
    'industry_soft_drinks':0,
    'industry_sports_leagues':0,
    'industry_computer_software':0,
    'industry_fast_food':0,
    'mood_informative':0,
    'n_top_actors':0,
    'industry_beer':0,
    'industry_light_beer':0,
    'mood_emotional':0,
    'industry_games':0,
    'industry_snacks1':0,
    'mood_inspirational':0,
    'industry_loans':0
}

def predict(industry,moods):
    model_inputs[industry_map[industry]] = 1

    for mood in moods:
        model_inputs[mood_map[mood]] = 1

    prediction = round(model.predict(model_inputs)[0]*100,2)
    
    return prediction

industry_map = {
    'Beer':'industry_beer',
    'Cars':'industry_cars1',
    'Computer Software':'industry_computer_software',
    'Entertainment':'industry_entertainment',
    'Fast Food':'industry_fast_food',
    'Games':'industry_games',
    'Loans':'industry_loans',
    'Snacks':'industry_snacks1',
    'Soft Drinks':'industry_soft_drinks',
    'Sports Leagues':'industry_sports_leagues',
    'Virtual Assistants':'industry_virtual_assistants'
    }

mood_map = {
    'Emotional':'mood_emotional',
    'Funny':'mood_funny',
    'Heartwarming':'mood_heartwarming',
    'Informative':'mood_informative',
    'Inspirational':'mood_inspirational'
    }


st.title('Super Bowl Advertisement Optimizer')

st.markdown(' ## Powered by Caryt Marketing Co.')


industry = st.selectbox(
    'Select an Industry',
    (
        'Beer',
        'Cars',
        'Computer Software',
        'Entertainment',
        'Fast Food',
        'Games',
        'Loans',
        'Snacks',
        'Soft Drinks',
        'Sports Leagues',
        'Other'
        )
    )

moods = st.multiselect(
    'Select Mood(s) (Up to 3)',
    [x for x in mood_map.keys()]
    )

button = st.button('Predict')

if button:
    result = predict(industry,moods)
    st.write('Your Predicted Ad Score is {}'.format(result))
    st.write('**Cluster Profile: (INSERT NAME)**')
    st.write('(CLUSTER DESCRIPTION)')
    col1, col2 = st.beta_columns(2)
    with col1:
      st.header("**Best Ad of Cluster: (INSERT AD SCORE)**")
      st.video("https://www.youtube.com/embed/xxNxqveseyI")
    with col2:
      st.header("**Worst Ad of Cluster: (INSERT AD SCORE)**")
      st.video("https://www.youtube.com/embed/xxNxqveseyI")


if button == false:
  st.write('\n \n \n \n \n \n')
    

# Bottom Row ------------------------------------------------------------------------
st.markdown('___')
about = st.beta_expander('About/Additional Info')
with about:
    '''
    Thank you for visiting the Super Bowl Advertisement Optimizer, powered by Caryt Marketing Co. For more information, please visit our team's [Github repository] (https://github.com/crbrandt/CarytMarketingCo).
    
    Curated by the Caryt Marketing Co. Analytics team: \n
    Cole Brandt \n
    Anton Averin \n
    Ranaa Ansari \n
    Young Jang \n
    Tyrone Brown
    '''
    
st.image("https://i.ibb.co/9qDzx87/Sunrise-Abstract-Shapes-Logo-Template-copy.png",
    width= 100, caption='2021 Caryt Marketing Co.')
