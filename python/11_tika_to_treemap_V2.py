#!/usr/bin/env python
# coding: utf-8

# # Launch treemap from result of Step3

# In[1]:


import os
from tika import parser
from datetime import datetime
import numpy as np
import pandas as pd
import re
import time
import psutil
import os
import signal
import glob
import matplotlib.pyplot as plt
import seaborn as sns

start_time = time.time()


# In[2]:


import global_variables as g
g.init()

category=g.category

output_directory=category+'_results'


# ## Prepare list of file to load

# In[3]:


now = datetime.now()
 
#parallelism =  4 

if g.DEBUG_OL >= 2:
    print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)

#category="doc-engineering"
#category="doc-consoles"
#category="doc-electro"
#category="doc-photo"
#category="doc-airbus"
#category="doc-tests"
#dirlist = os.listdir(category+'_*.csv')
my_input_file=output_directory+'/'+category+'__total__wordcounts.csv'


#print(dirlist)
#for i in range(len(dirlist)):
#    dirlist[i]=''.join(dirlist[i].split())
    
if g.DEBUG_OL >= 1:
    print(my_input_file,'à traiter\n')


# In[4]:


my_loaded_array = pd.read_csv(my_input_file,encoding='utf-8')
df_words = my_loaded_array
df_words


# In[5]:


n = 30
pal = list(sns.color_palette(palette='Reds_r', n_colors=n).as_hex())

import plotly.express as px
fig = px.pie(df_words[0:30], values='count', names='words',
             color_discrete_sequence=pal)

fig.update_traces(textposition='outside', textinfo='percent+label', 
                  hole=.6, hoverinfo="label+percent+name")

fig.update_layout(width = 800, height = 600,
                  margin = dict(t=0, l=0, r=0, b=0))
import plotly.io as pio

pio.renderers.default = 'iframe'
fig.show()


# In[7]:


import plotly.express as px

aa= len(df_words)
if aa < 100:
    fin=aa
else:
    fin=100
#print(df_words[0:fin])
import plotly.express as px
fig = px.treemap(df_words[0:100], path=[px.Constant(category), 'words'],
                 values='count',
                 color='count',
                 color_continuous_scale='viridis',
                 color_continuous_midpoint=np.average(df_words['count'])
                )
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

import plotly.io as pio
pio.renderers.default = 'iframe'


fig.show()
fig.write_image(output_directory+'/'+category+'__treemap__wordscount.png')


# In[ ]:




