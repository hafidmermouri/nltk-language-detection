#!/usr/bin/env python
#coding:utf-8
# Author: Hafid Mermouri
# Created: 09/02/2017

import sys

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

def _calc_ratios(text):

    ratios = {}

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    for lang in stopwords.fileids():
        stopwords_set = set(stopwords.words(lang))
        words_set = set(words)
        common_words = words_set.intersection(stopwords_set)

        ratios[lang] = len(common_words)

    return ratios


def detect_language(text):

    ratios = _calc_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)
    most_common_words = ratios[most_rated_language]
    del ratios[most_rated_language]
    second_most_rated_language = max(ratios, key=ratios.get)
    second_most_common_words = ratios[second_most_rated_language]

    print("there is %s%% chances for this text to be writen in %s" %(_calc_probability(most_common_words, second_most_common_words), most_rated_language))


def _calc_probability(most, secode_most) :
    proba = (float(most) /(most + secode_most) * 100)
    return round(proba)

if __name__=='__main__':

    #text snipet from http://latta.blog.lemonde.fr/2017/02/08/goal-line-technology-un-nouveau-bug-contre-son-camp/
    text = '''
    Le match de Ligue 1 Bordeaux-Rennes, ce week-end, a été le théâtre du troisième incident significatif
    lié à l’usage de la Goal Line Technology depuis sa mise en œuvre dans divers championnats depuis deux saisons.
    La montre de l’arbitre central Sébastien Desiage a vibré à la 44e minute, indiquant que le ballon était
    entièrement entré dans la cage bordelaise au moment où le gardien Cédric Carrasso se saisissait de celui-ci,
    pourtant nettement devant la ligne de but. Sébastien Desiage a heureusement choisi d’ignorer l’alerte et de ne
    pas valider ce but virtuel, au grand soulagement du gardien des Girondins.

    '''

    detect_language(text)
