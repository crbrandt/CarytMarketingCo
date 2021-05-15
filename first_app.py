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




