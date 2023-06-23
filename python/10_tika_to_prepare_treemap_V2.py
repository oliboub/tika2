#!/usr/bin/env python
# coding: utf-8

# # Prepare file source for a treemap display based on a directory of files already preparfed thrue ika step1
# - Files directory in category
# 
# Creation of files:<br>
#  |name |description|
#  |---|---|
#  | **category__total__wordscount.csv** | one file by filename containing all metadata and qtt of words found inthis file|
#  | **category__wordcounts__with_files.csv** | one file by filename containing all metadata and qtt of words found inthis file|
# 

# # This program intends:
# ## Step 1
# - To get multiple files in pandas dataframe wrods, count, butr link to a category name
# - To concatenate all of these datframe in one dataframe
# - To prepare a treemap
# - To generate a file for the treemap
# <br>
# ## Step2
# - To create treemap
# <br>

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

dirlist = [f for f in glob.glob(output_directory+'/'+category+'_*.csv')]
my_output_file=output_directory+'/'+category+'__total__wordcounts.csv'
my_full_output_file=output_directory+'/'+category+'__wordcounts__with_files.csv'

my_file_list = [s for s in dirlist if "__wordscount.csv" in s]

#print(dirlist)
#for i in range(len(dirlist)):
#    dirlist[i]=''.join(dirlist[i].split())
    
if g.DEBUG_OL >= 1:
    print(len(my_file_list),' fichier(s) à traiter\n', my_file_list)


# ## load pandas dataframe file(s)

# In[4]:


list_of_dataframes = []
full_list_with_files = []

for filename in my_file_list:

    start_str = filename.find('__')
    end_str=filename.find('__',start_str+1)
    my_file=filename[start_str+2:end_str]
    if g.DEBUG_OL >= 2:
        print(start_str+1,end_str,my_file)
    
    
    full_current_dataframe=pd.read_csv(filename,encoding='utf-8')
    full_current_dataframe['file']=my_file
    full_list_with_files.append(full_current_dataframe)
    my_list_array = pd.concat(full_list_with_files)
    if g.DEBUG_OL >= 2:
        print(my_list_array)
        display(full_current_dataframe)
    
    current_dataframe=pd.read_csv(filename)
    list_of_dataframes.append(current_dataframe)
my_list_array.to_csv(my_full_output_file,header=True,index=False,encoding='utf-8')


# In[5]:


if g.DEBUG_OL >= 2:
    display(list_of_dataframes)
my_loaded_array = pd.concat(list_of_dataframes)


# In[6]:


if g.DEBUG_OL >= 2:
    print(my_loaded_array)


# In[7]:


my_output_array=my_loaded_array.groupby(['words']).sum().reset_index()
my_output_array.sort_values('count', ascending=False, inplace=True)
if g.DEBUG_OL >= 2:
        display(my_output_array)


# ## save file

# In[8]:


my_output_array.to_csv(my_output_file,header=True,index=False,encoding='utf-8')


# In[9]:


print('Process terminé.')

