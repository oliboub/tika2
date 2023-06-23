#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PySimpleGUI as sg
import pandas as pd


# In[2]:


import global_variables as g
g.init()

category=g.category

output_directory=category+'_results'


# In[6]:


import PySimpleGUI as sg
title='Selected category:'+category
layout = [[sg.T('Please select a file:'), sg.I(key='-CSV-', enable_events=True),sg.FileBrowse(initial_folder=output_directory,file_types=(('csv files',['*.csv']),('CSV','*.csv')))],
         [sg.Text('Entrer le mot recherché:'), sg.I(key='-MOT-')],
         [ sg.Ok(), sg.Cancel()]]
window=sg.Window(title, layout)
while True:
    events, values = window.read()
    if events == 'Cancel' or events == sg.WIN_CLOSED:
        window.close()
        break
    elif events == 'Ok':
        if g.DEBUG_OL >= 2:
            print(events,values)
        input_file = values['-CSV-']
        recherche_mot = values['-MOT-']
        if g.DEBUG_OL >= 2:
            print(input_file,recherche_mot)        
        window.close()


# In[7]:


import pandas as pd
import numpy as np
import csv


#category='doc-photo'
#category='doc-engineering'
#category="doc-airbus"

#input_file = category+'__cloudword__level1.csv'

output_file = output_directory+'/'+category+'__search__result__'+recherche_mot+'.csv'
#output_dest2 = category+'__cloudword__dest2.csv'

if g.DEBUG_OL >= 2:
    print('input_file: ',input_file)
    print('output_file:',output_file)

reader = csv.reader(open(input_file))

max_columns=0

for row in reader:
    if g.DEBUG_OL >= 2:
        print(row)
        print(len(row),row)
    if len(row) > max_columns:
        max_columns=len(row)
print("max_columns:",max_columns)


# In[8]:


reader = csv.reader(open(input_file))
numlines = len(list(reader))
if g.DEBUG_OL >= 1:
    print("Lines:",numlines)


# In[9]:


col_headers= ['category','file']
for aa in range(max_columns-1):
    col_headers.append('M'+str(aa))

if g.DEBUG_OL >= 2:
    print('Col_headers:',col_headers)
    

#my_loaded_array = pd.read_csv(input_file,dtype=str,header=None,names=col_headers)
my_loaded_array = pd.read_csv(input_file,dtype=str,names=col_headers)

my_loaded_array=my_loaded_array.fillna('')
if g.DEBUG_OL >= 2:
    display(my_loaded_array)
    
array_values = my_loaded_array.values
if g.DEBUG_OL >= 2:
    print(array_values)

if g.DEBUG_OL >= 2:
    print(recherche_mot)

toto=array_values[:,0:max_columns] == recherche_mot
if g.DEBUG_OL >= 2:
    print(toto)
    
cloud_word_lvl2 = open(output_file, 'w')
coltitle= ','.join(col_headers)
cloud_word_lvl2.write(coltitle)
cloud_word_lvl2.write('\x0A')
for i in range(my_loaded_array.shape[0]):
#    print(i,'\t', toto[i,:])
    if True in toto[i,:]:
        if g.DEBUG_OL >= 2:
            print(i,'OK')
            print(array_values[i,0:])
        TEMPstring = ','.join(array_values[i,:])
        if g.DEBUG_OL >= 2:
            print(TEMPstring)
        cloud_word_lvl2.write(TEMPstring)
        cloud_word_lvl2.write('\x0A')
#    else:
#        if g.DEBUG_OL >= 2:
#            print(i,'Not OK',array_values[i,0:])
        
cloud_word_lvl2.close()

print('***** Fini! fichier:',output_file,' généré *****')


# In[ ]:





# In[ ]:





# In[ ]:




