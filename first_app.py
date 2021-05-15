#!/usr/bin/env python
# coding: utf-8

# In[51]:


import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Caryt Marketing Co. Super Bowl Advertisement Optimizer',
                   page_icon='https://i.ibb.co/02x1bQN/Sunrise-Abstract-Shapes-Logo-Template-copy-2.png'
                   layout="wide")

st.title('Super Bowl Advertisement Optimizer')

st.markdown(' ## Powered by Caryt Marketing Co.')


# In[46]:


records = ['Beer', 'Cars', 'Medicine']
type(records)


# In[54]:


selected_data = st.selectbox('Select an Industry', options=records)


# In[48]:


result = ""
if selected_data == 'Beer' :
    result = 'Comedy'
elif selected_data == 'Cars' :
    result = 'Dramatic'
else :
    result = 'Serious'


# In[49]:


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# In[55]:


st.markdown("Your ad should be: " + result)


# In[58]:


vid = ""
if selected_data == 'Beer' :
    vid = 'https://youtu.be/q-QTDm1kdwo'
elif selected_data == 'Cars' :
    vid = 'https://youtu.be/8QEAA94FjHc'
else :
    vid = 'https://youtu.be/NdN0HKUAg78'

st.markdown("\nExample: \n")
st.video(vid)


# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[51]:


import streamlit as st
import pandas as pd
import numpy as np

st.title('Super Bowl Advertisement Optimizer')

st.markdown(' ## Powered by Caryt Marketing Co.')


# In[46]:


records = ['Beer', 'Cars', 'Medicine']
type(records)


# In[54]:


selected_data = st.selectbox('Select an Industry', options=records)


# In[48]:


result = ""
if selected_data == 'Beer' :
    result = 'Comedy'
elif selected_data == 'Cars' :
    result = 'Dramatic'
else :
    result = 'Serious'


# In[49]:


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# In[55]:


st.markdown("Your ad should be: " + result)


# In[58]:


vid = ""
if selected_data == 'Beer' :
    vid = 'https://youtu.be/q-QTDm1kdwo'
elif selected_data == 'Cars' :
    vid = 'https://youtu.be/8QEAA94FjHc'
else :
    vid = 'https://youtu.be/NdN0HKUAg78'

st.markdown("\nExample: \n")
st.video(vid)


# In[ ]:




# ROW 5 ------------------------------------------------------------------------
row5_spacer1, row5_1, row5_spacer2 = st.beta_columns((.1, 3.2, .1))

with row5_1:
    st.markdown('___')
    about = st.beta_expander('About/Additional Info')
    with about:
        '''
        Thanks for checking out my app! It was built entirely using [nflfastR]
        (https://www.nflfastr.com/) data. Special thanks to [Ben Baldwin]
        (https://twitter.com/benbbaldwin) and [Sebastian Carl]
        (https://twitter.com/mrcaseb) who do a great job maintaining this public
        data, making the barrier to entry for NFL analytics incredibly low! This
        is the first time I have ever built something like this, so any comments
        or feedback is greatly appreciated. I hope you enjoy!
        ---
        This app is a dashboard that runs an analysis on any desired WR or TE who
        has logged at least 30 total targets in the 2020 season. Player info,
        a game log, and six visualizations of various statistics are displayed
        for the selected player. They are briefly described below:
        **Player Info** - Headshot along with the name, college,
        position, height,  and weight of the selected player.
        **Game Log** - A boxscore for each game the selected player appeared in.
        **Air Yards Distribution** - A density plot of air yards for the
        selected player. NFL Average in gray.
        (NFL Average takes into account every pass)
        **Binned Air Yards** - A Bar graph of target counts with five discrete
        air yards bins for the selected player.
        **Air Yards as a Function of targets** - A scatterplot of air yards
        as a function of targets. Selected player is colored. Trend line is
        shown to indicate whether a player is seeing more (or less) air yards
        than their target count suggests based on the sample.
        (Only players available in this dashboard are charted)
        **PPR Points by Week** - A line chart of PPR fantasy points the selected
        player has scored each week using vanilla fantasy socring. A missing
        week label means the selected player did not play or was on BYE.
        (Does *not* include fantasy points from passing, but *does* include 6
        point bonuses for rush and return touchdowns, which aren't shown on the
        game log)
        **EPA/Target** - A scatterplot of EPA/Target as a function of success
        rate (success = epa>0 on a given play). Size is a function of targets.
        Dotted lines are averages of the charted players.
        (Only players available in this dashboard are charted)
        **Catch Rate** - A scatterplot of catch rate as a function of target
        depth. Size is a function of targets. NFL average in gray. Smoothed
        using a locally weighted linear regression (LOWESS).
        (NFL Average takes into account every pass)
        *Tip - To get a better look at any individual chart, click the
        expander box!*
        *Disclaimer - Some of the air yards data might not be perfectly correct.
        The NFL has logged some incorrect air yards values this season and as a
        result, there may be some occurences where air yards values are within
        a +/-5 margain. Also, since this app is using nflfastR data, new games
        and data won't show up until they are scraped by the nflfastR team. If
        you aren't seeing new data yet, it will be updated soon.*
        ### Max Bolger, 2020
        '''
        st.image("https://www.nflfastr.com/reference/figures/logo.png",
        width= 100, caption='nflfastR')

