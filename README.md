# <span style="color:orange">README.md</span>

## <span style="color:blue">Introduction</span>
This git is used to try apache tika on different documents format.<br>
the aim is to collect all words, out of stopwords, in the content of the documents and create files with metadata.<br>

stopwords can be changed to other language, just check on this site:
https://countwordsfree.com/stopwords/french

Drawings are based on this information:
https://towardsdatascience.com/beyond-the-cloud-4-visualizations-to-use-instead-of-word-cloud-960dd516f215

cloudword tutorial:
https://www.youtube.com/watch?v=l7w7unBNAeU



a category is needed. it means a subdirectory of the home directory with your images files to transform in words.
## <span style="color:blue">Files usage </span>
4 files have been developped,
| FIle | Description |
| --- | --- |
| jupyter_files/**00_tika_init_for treemap_and_wordcloud_V2_step1.ipynb** | tika parsing of files in category, Initialisation of pandas dataframe for future analysis and display first level of cloudwords |
|jupyter_files/**01_tika_for_wordcloud_lvl2_V2_step2.ipynb** | search a word seen in the first level of cloudword to dig in the results |
| jupyter_files/**10_tika_to_prepare_treemap_V2.ipynb** | prepare files to be used through plotly-express to display a treemap |
| jupyter_files/**11_tika_to_treemap_V2.ipynb** | Display treemap based on files poreviously created |
| jupyter_files/**12_tika_to_treemap_with_files_V2.ipynb** | Display treemap with file names based on files poreviously created |


## <span style="color:blue">result </span>
| FIle | Description |
| --- | --- |
| category__cloudword_level1.csv | file with all treated files words including the file name and category. Words are unique, the quantity for each file is not handled volontarly |
| category__cloudword_dest1.csv | file without category and filename to be trated by cloudword. Words are unique, the quantity for each file is not handled volontarly |
| category_file__wordscount.csv | one file by file treated it includes the wordsd and number of words found|
| category__cloudword_level2.csv | file with second level of check. All treated files words including the file name and category. Words are unique, the quantity for each file is not handled volontarly |
| category__cloudword_dest2.csv | file with second level of check. File without category and filename to be trated by cloudword. Words are unique, the quantity for each file is not handled volontarly |
| category__cloudword_dest2.png | cloudword png file as result of the second level of check file |
| category__total__wordcounts.csv | csv file with all words of the category with the number of words found |
| doc-tests__wordcounts__with_files.csv | csv file with all words found but by file with filename |


## <span style="color:blue">Development environment</span>
- using ubuntu 23 with python 3.11 and openjava sdk 17<br>
- using jupyter lab<br>
- working in a venv (virtual environment)<br>
- To use jupyter files, you need to add the subdirectory **python** in the PYTHONPATH variable.<br>

- for tika, java jdk is needed


## <span style="color:blue">additional libraries used</span>
to be added in the vitrual environment with pip.
- **tika**
- **jupyterlab**
- **pandas**
- **numpy**
- **plotly-express**  
- **matplotlib**
- **seaborn**
- 
## <span style="color:blue">log mod</span>
to change the log level and get more print:<br>
- change **DEBUG_OL** value to **2** in the file ./python/global_variables.py

## <span style="color:blue">debug mode</span>
to check function or different steps of the code, it can be done inside jupyter lab, by executing some steps and creating to launch unitary tests.<br>

## backlog and issues
Local follow-up is in the file:
[backlog & issues](./todo_list.md)