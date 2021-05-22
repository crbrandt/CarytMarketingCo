import streamlit as st
#conda install statsmodels
#pip install statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats


##Updating Page Logo and Tab Title
st.set_page_config(page_title='Caryt Marketing Co. Super Bowl Advertisement Analyzer',
                   page_icon='https://i.ibb.co/ry0gwGD/caryt-logo-secondary.png',
                   layout="wide")


##Creating Text format options with orange colors
def highlight(text):
     st.markdown(f'<p style="text-align: center;color:#f19e28;font-size:22px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def color(text):
     st.markdown(f'<p style="color:#f19e28;font-size:20px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)


##Loading in USA Today scoring model from Github
model = sm.load('./usa_today_model')

##Setting initial values for inputs to the regression model.
model_inputs = {
  'industry_virtual_assistants':0,
  'industry_cars1':0,
  'industry_entertainment':0,
  'industry_soft_drinks':0,
  'industry_sports_leagues':0,
  'industry_computer_software':0,
  'industry_fast_food':0,
  'industry_games':0,
  'industry_snacks1':0,
  'industry_mortgages':0,
  'industry_mortgages * mood_funny':0,
  'industry_cars1 * mood_funny':0,
  'mood_funny':0,
  'mood_heartwarming':0,
  'mood_weird':0,
  'mood_emotional':0,
  'mood_inspirational':0,
  'mood_cute_adorable':0,
  'mood_unique':0,
  'n_nfl':0,
  'n_top_actors':0,
  'n_politician':0
}

##Creating prediction functions
def predict(industry,moods,celebs):
    if industry_map[industry] in model_inputs:
        model_inputs[industry_map[industry]] = 1

    for mood in moods:
        if mood_map[mood] in model_inputs:
          model_inputs[mood_map[mood]] = 1
          
    # Interaction Inputs
    model_inputs['industry_mortgages * mood_funny'] = model_inputs['industry_mortgages'] * model_inputs['mood_funny']
    model_inputs['industry_cars1 * mood_funny'] = model_inputs['industry_cars1'] * model_inputs['mood_funny']

    prediction = round(model.predict(model_inputs)[0]*100,2)
    if prediction < 0:
      prediction = 0
    if prediction > 100:
      prediction = 100
    
    return prediction

###Mapping industry values in the data to their display options on the application
industry_map = {
    'Auto Parts & Accessories':'industry_auto_parts_accessories',
    'Airlines':'industry_airline_industry',
    'Beauty':'industry_beauty',
    'Beer':'industry_beer',
    'Beverages':'industry_beverages',
    'Candy':'industry_candy',
    'Cars':'industry_cars1',
    'Cellular, Internet, and TV Providers': 'industry_cellular',
    'Cleaning Supplies':'industry_cleaning_supplies',
    'Cola Drinks': 'industry_cola_drinks',
    'Software and Technology':'industry_computer_software',
    'Computer Hardware':'industry_computer_hardware',
    'Credit Cards':'industry_credit_cards',
    'Deodorant':'industry_deodorant',
    'Dips':'industry_dips',
    'Music, Movies, and Entertainment':'industry_entertainment',
    'Energy Drinks':'industry_energy_drinks',
    'Restaurants and Fast Food':'industry_fast_food',
    'Financial Services':'industry_financial_services',
    'Food Delivery':'industry_food_delivery',
    'Freelancers':'industry_freelancers',
    'Games':'industry_games',
    'Home Security':'industry_home_security',
    'Hotels':'industry_hotels',
    'Hygiene':'industry_hygiene',
    'Insurance':'industry_insurance',
    'Investments':'industry_investments',
    'Job Search':'industry_job_search',
    'Lawn Care':'industry_lawn_care',
    'Liquors':'industry_alcoholic_beverages',
    'Loans':'industry_loans',
    'Mobile Phones':'industry_mobile_phones',
    'Mortgages':'industry_mortgages',
    'Movies':'industry_movies',
    'Nuts':'industry_nuts',
    'Online Retailers':'industry_online_retailers',
    'Online Streaming Services':'industry_online_streaming',
    'Pizza':'industry_pizza',
    'Potato Chips':'industry_potato_chips',
    'Retail Stores':'industry_retail_stores',
    'Search Engines':'industry_search_engines',
    'Shoes':'industry_shoes',
    'Snacks':'industry_snacks1',
    'Soap':'industry_soap',
    'Social Media':'industry_social_media',
    'Soft Drinks':'industry_soft_drinks',
    'Sports Leagues':'industry_sports_leagues',
    'Taxes':'industry_taxes',
    'Travel':'industry_travel_industry',
    'Trucks':'industry_trucks',
    'TV Providers':'industry_TV_providers',
    'Virtual Assistants':'industry_virtual_assistants',
    'Water':'industry_water',
    'Yogurt':'industry_yogurt',
    'Other':'other'
    }

mood_map = {
    'Adventurous':'mood_adventurous',
    'Alluring':'mood_alluring',
    'Boring':'mood_boring',
    'Controversial':'mood_controversial',
    'Cute/Adorable':'mood_cute\adorable',
    'Dramatic':'mood_dramatic',
    'Emotional':'mood_emotional',
    'Exciting':'mood_exciting',
    'Flirty':'mood_flirty',
    'Funny':'mood_funny',
    'Goofy':'mood_goofy',
    'Gross':'mood_gross',
    'Heartwarming':'mood_heartwarming',
    'Informative':'mood_informative',
    'Inspirational':'mood_inspirational',
    'Light-hearted':'mood_light hearted',
    'Mysterious':'mood_mysterious',
    'Party-themed':'mood_party themed',
    'Patriotic':'mood_patriotic',
    'Romantic':'mood_romantic',
    'Scary':'mood_scary',
    'Serious':'mood_serious',
    'Sexy':'mood_sexy',
    'Shocking':'mood_shocking',
    'Somber':'mood_somber',
    'Suspenseful':'mood_suspenseful',
    'Unique':'mood_unique',
    'Weird':'mood_weird'
    }

celeb_map = {
    'Athletes':'n_athlete',
    'Bands':'n_band',
    'Business Leaders':'n_business_leader',
    'Comedians':'n_comedian',
    'Football Coaches':'n_football_coaches',
    'Historical Figures':'n_historical_figures',
    'Models':'n_models',
    'Musicians':'n_musician',
    'NFL Players':'n_nfl',
    'Politicians':'n_politician',
    'Reality TV Stars':'n_reality_tv_stars',
    'Sports Commentators':'n_sports_commentators',
    'Talk Show Hosts':'n_talk_show_hosts',
    'Top Actors':'n_top_actors'
    }



##--------------------------------------------------------Application Displayed Portion-----------------------------------------

##Header and Logo
col_title, col_logo = st.beta_columns([4,1])
with col_title:
  st.title('Super Bowl Advertisement Analyzer')
  st.markdown(' ## Powered by Caryt Marketing Co.')
with col_logo:
  st.image("https://i.ibb.co/ry0gwGD/caryt-logo-secondary.png")
st.write("#")



#Selectbox for Industry
industry = 'Choose an option'

if industry == 'Choose an option':
    industry = st.selectbox(
            'Select an Industry',
            (
                'Choose an Option'
                'Beer',
                'Cars',
                'Cellular, Internet, and TV Providers',
                'Restaurants and Fast Food',
                'Games',
                'Loans',
                'Music, Movies, and Entertainment',
                'Online Streaming Services',
                'Snacks',
                'Soft Drinks',
                'Software and Technology',
                'Sports Leagues',
                'Virtual Assistants',
                'Other'
            ), index = 14
            )
else:
  industry = st.selectbox(
        'Select an Industry',
        (
            'Beer',
            'Cars',
            'Cellular, Internet, and TV Providers',
            'Restaurants and Fast Food',
            'Games',
            'Loans',
            'Music, Movies, and Entertainment',
            'Online Streaming Services',
            'Snacks',
            'Soft Drinks',
            'Software and Technology',
            'Sports Leagues',
            'Virtual Assistants',
            'Other'
        )
        )

##Selectbox for mood (note: if more than three moods are selected, users will not be able to continue)
moods = st.multiselect(
    'Select Mood(s) (Up to 3)',
    [x for x in mood_map.keys()]
    )

if len(moods) > 3:
  color('Please limit your mood selections to three or less.')


##Multiselect for celebrity types. When celebrities are selected, their specific count values will be editable using sliders.
celebs = st.multiselect(
    'Select Types of Celebrities in Your Advertisement',
    [x for x in celeb_map.keys()]
    )

celeb_sliders = []
for celeb in celebs:
    celeb_slider = st.slider(f'Number of {celeb}: ' , min_value=1, max_value=10)
    model_inputs[celeb_map[celeb]] = celeb_slider
    

##Predictions for score and cluster
if len(moods) <= 3:
    button = st.button('Predict')
    
    #Setting initial cluster text values
    best_ad_link = worst_ad_link = best_ad_title = worst_ad_title = best_ad_score = worst_ad_score = ''


    #cluster_info = st.slider('Cluster Number: ', min_value = 0, max_value = 5)
    cluster_info = 0;
    cluster_text = ''

    if button:
      result = predict(industry,moods, celeb_sliders)
      highlight(('Your Predicted Ad Score is {}'.format(result) + ' out of 100'))
          #
      #
      #
      #Cluster value determinant, based on findings from the Clustering model:
      #
      if industry == 'Beer' and not ('Inspirational' in moods or 'Heartwarming' in moods or 'Dramatic' in moods or 'Somber' in moods or 'Serious' in moods):
        cluster_info = 5
      if industry == 'Beer' and ('Inspirational' in moods or 'Heartwarming' in moods or 'Dramatic' in moods or 'Somber' in moods or 'Serious' in moods):
        cluster_info = 1
      if industry == 'Cars':
        cluster_info = 3
      if industry == 'Cellular, Internet, and TV Providers':
        cluster_info = 5
      if industry == 'Restaurants and Fast Food':
        cluster_info = 2
      if industry == 'Games':
        cluster_info = 3
      if industry == 'Loans':
        cluster_info = 1
      if industry == 'Music, Movies, and Entertainment':
        cluster_info = 2
      if industry == 'Online Streaming Services':
        cluster_info = 4
      if industry == 'Snacks':
        cluster_info = 2
      if industry == 'Soft Drinks':
        cluster_info = 2
      if industry == 'Software and Technology' and ('Funny' in moods or 'Goofy' in moods or 'Party-themed' in moods):
        cluster_info = 5
      if industry == 'Software and Technology' and not ('Funny' in moods or 'Goofy' in moods or 'Party-themed' in moods):
        cluster_info = 1
      if industry == 'Virtual Assistants' and ('Funny' in moods or 'Goofy' in moods or 'Party-themed' in moods):
        cluster_info = 2
      if industry == 'Virtual Assistants' and not ('Funny' in moods or 'Goofy' in moods or 'Party-themed' in moods):
        cluster_info = 1
      if industry == 'Other' or (model_inputs[celeb_map['Politicians']] > 0 and not ('Funny' in moods or 'Goofy' in moods or 'Sexy' in moods)):
        cluster_info = 1
      if industry == 'Sports Leagues' or model_inputs[celeb_map['NFL Players']] > 2:
        cluster_info = 0
      #
      #
      #
      ##Cluster descriptions:
      #
      if cluster_info == 0:
        best_ad_title = 'NFL - The 100-Year Game'
        worst_ad_title = 'Jublia - Best Kept Secret'
        best_ad_link = 'https://www.youtube.com/watch?v=tJjiIuH1VnY'
        worst_ad_link = 'https://www.youtube.com/watch?v=AXCCmCwzRPs'
        best_ad_score = '77 out of 100'
        worst_ad_score = '32 out of 100'
        cluster_name = 'Superbowl/NFL Advertisements'
        cluster_text = """
          - This cluster had the highest average rating among all the clusters.
          - Primarily composed of advertisements in regards to the Superbowl or involving NFL actors.
          - A common theme is the advertisement showcasing some sort of party theme.
          - Exciting or funny moods are the most likely.
          """
      elif cluster_info == 1:
        best_ad_title = 'Budweiser - Lost Dog'
        worst_ad_title = 'Donald Trump - Criminal Justice Reform'
        best_ad_link = 'https://www.youtube.com/watch?v=TPKgC8KPBMg'
        worst_ad_link = 'https://www.youtube.com/watch?v=Xtv_PJE8xns'
        best_ad_score = '81 out of 100'
        worst_ad_score = '33 out of 100'
        cluster_name = '\'The Unique\''
        cluster_text = """
          - Largest cluster out of all of them and thus contained the most variety in all the attributes. However this was an indication that this cluster contained the advertisements that were most unique.
          - While popular industries are present here, this cluster contains industries that are not very popular or common such as sex paraphernalia and politics.
          - Athletes in general are commonly found as actors here along with politicians and other famous personnel.
          - The moods vary with the biggest two being funny and exciting, but the variety stretching from light hearted to patriotic to emotional.
          """
      elif cluster_info == 2:
        best_ad_title = 'M&M\'S - Bad Passengers'
        worst_ad_title = 'Burger King - Eat like Andy'
        best_ad_link = 'https://www.youtube.com/watch?v=w7FIka-jYM8'
        worst_ad_link = 'https://www.youtube.com/watch?v=HcbWkcDRJjc'
        best_ad_score = '65 out of 100'
        worst_ad_score = '46 out of 100'
        cluster_name = 'Food, Drink, and Movies'
        cluster_text = """
          - This Cluster was primarily composed of advertisements for a variety of beverages and snacks. Full meals were not prevalent in general but specifically snacks and drinks were quite common.
          - This cluster contained advertisements that used the highest amount of actors, both of the well-known fame level and of a lesser level.
          - This cluster was far more likely to contain some sort of comedian either in the story or as an actor.
          - Funny and exciting were the predominant moods.
          """
      elif cluster_info == 3:
        best_ad_title = 'Kia Niro - Hero\'s Journey'
        worst_ad_title = 'Lexus LS 500 F SPORT - Blank Panther'
        best_ad_link = 'https://www.youtube.com/watch?v=pVxmT2x3Od4'
        worst_ad_link = 'https://www.youtube.com/watch?v=1isIeJy6lTE'
        best_ad_score = '77 out of 100'
        worst_ad_score = '51 out of 100'
        cluster_name = 'Cars, Cars, and More Cars'
        cluster_text = """
          - This cluster was predominantly made up of advertisements for specific car models and car manufacturers. There was also a non-insignificant amount of movie  and game focused ads.
          - This cluster had the most talk show hosts involved as part of the story or in the capacity of an actor.
          - These advertisements involved the most actors on a number basis (i.e on set and on screen).
          - Dramatic and adventurous were the most common moods.
          """
      elif cluster_info == 4:
        best_ad_title = 'Netflix - Our Planet'
        worst_ad_title = 'Quibi - Bank Heist'
        best_ad_link = 'https://www.youtube.com/watch?v=BSLzGgFbHZE'
        worst_ad_link = 'https://www.youtube.com/watch?v=cBlKObT5dv0'
        best_ad_score = '61 out of 100'
        worst_ad_score = '44 out of 100'
        cluster_name = 'Streaming Services'
        cluster_text = """
          - This group is mainly composed of streaming services
          - There tend to be musicians either involved in the story on screen.
          - Only category with wrestlers involved in either the story or as actors.
          - Funny or inspirational moods are the most likely.
          """
      elif cluster_info == 5:
        best_ad_title = 'Bud Light - Special Delivery'
        worst_ad_title = 'Michelob Ultra - Breathe'
        best_ad_link = 'https://www.youtube.com/watch?v=JZC3K6qk4wY'
        worst_ad_link = 'https://www.youtube.com/watch?v=s4A_BsWnY8w'
        best_ad_score = '61 out of 100'
        worst_ad_score = '41 out of 100'
        cluster_name = 'Chatting with Beer'
        cluster_text = """
          - This cluster was composed of two industries primarily, the alcohol industry with a focus on beer, and on the mobile providers and new phone models.
          - Contained one of the smallest amounts of well-known actors, and in general, used very few actors on set.
          - Following along with the beer grouping, this cluster also had a high amount of potato chip advertisements paired with it.
          - The predominant mood was funny by a very large margin with goofy and adorable being the only two significant moods following it.
          """
      st.markdown(f'### Cluster Profile: {cluster_name}')
      st.write(cluster_text)
      col1, col2 = st.beta_columns(2)
      with col1:
        st.markdown('### Ad from this cluster which performed well:')
        color(f'{best_ad_title}')
        st.write(f'Ad Score: {best_ad_score}')
        st.video(best_ad_link)
      with col2:
        st.markdown('### Ad from this cluster which performed poorly:')
        color(f'{worst_ad_title}')
        st.write(f'Ad Score: {worst_ad_score}')
        st.video(worst_ad_link)
    else:
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")

if len(moods)> 3:
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")
      st.write("#")    

# Bottom info bar ------------------------------------------------------------------------
st.markdown('___')
about = st.beta_expander('About')
with about:
    '''
    Thank you for visiting the Super Bowl Advertisement Optimizer, powered by Caryt Marketing Co. For more information, please visit our team's [Github repository] (https://github.com/crbrandt/CarytMarketingCo).
    
    Curated by the Caryt Marketing Co. Analytics team: \n
    Cole Brandt, Anton Averin, Ranaa Ansari, Young Jang, Tyrone Brown
    '''
    
st.image("https://i.ibb.co/9qDzx87/Sunrise-Abstract-Shapes-Logo-Template-copy.png",
    width= 100, caption='2021 Caryt Marketing Co.')
