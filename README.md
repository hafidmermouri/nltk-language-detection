# nltk-language-detection

[![N|Solid](http://www.le-geek.com/wp-content/uploads/2017/02/geek.png)](https://www.le-geek.com/)

Automatic detection of text language with Python and NLTK.
This script uses a very simple approach based on stopwords comparaison. The stopwords list with the most commun words win the association.
## Dependencies
you have to install [NLTK package](http://www.nltk.org/api/nltk.html) for Python to run this script.

## How it works
just give the script a brunch of text to analyse and the script will :
  - Parse and tokenize you text
  - Compare the tokens with all stopwords lists contained in NLTK corpus in all language available
  - Select the most relevant language
  - Calculate the relevancy level of the selected language

## Documentation
If you want to know how this script works, just have a look at this blog post titled [Detection de langue en NLP](https://www.le-geek.com/detection-de-langue-en-nlp-natural-language-processing/) i wrote (in french) on my personnal blog [le-geek.com](https://www.le-geek.com/)