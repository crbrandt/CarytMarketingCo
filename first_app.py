#!/usr/bin/env python
# coding: utf-8

# In[51]:


import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Caryt Marketing Co. Super Bowl Advertisement Optimizer',
                   page_icon='https://i.ibb.co/ry0gwGD/caryt-logo-secondary.png',
                   layout="wide")
#https://i.ibb.co/d55RjZp/Sunrise-Abstract-Shapes-Logo-Template.png
#https://i.ibb.co/ry0gwGD/caryt-logo-secondary.png
st.title('Super Bowl Advertisement Optimizer')

st.markdown(' ## Powered by Caryt Marketing Co.')

row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.beta_columns(
    (.1, 2, 1.5, 1, .1)
    )

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




# ROW 5 ------------------------------------------------------------------------
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
    '''
    ##st.image("https://www.nflfastr.com/reference/figures/logo.png",
    ##width= 100, caption='nflfastR')

