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
import plotly.express as px

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
my_input_file=output_directory+'/'+category+'__wordcounts__with_files.csv'


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


import plotly.express as px
#fig = px.treemap(df_words, path=[px.Constant("test1-1.odt","test1-2.odt"), 'file','words'],
fig = px.treemap(df_words, path=['file','words'],
                 values='count',
                 color='count', hover_data=['count'],
                 color_continuous_scale='viridis',
                 color_continuous_midpoint=np.average(df_words['count']),
                 maxdepth=10
                )
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))


import plotly.io as pio
pio.renderers.default = 'iframe'

fig.show()
fig.write_image(output_directory+'/'+category+'__treemap__files_wordscount.png')


# In[ ]:




