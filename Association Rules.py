# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

itempath = 'C:/Users/Tehmeer Ali Paryani/Desktop/Tensorflow/U Recommender Systems PS/EB-build-goods.sql'
receiptspath = 'C:/Users/Tehmeer Ali Paryani/Desktop/Tensorflow/U Recommender Systems PS/75000i.csv'

with open(receiptspath, "r") as receiptsfile:
    receiptsdata = receiptsfile.read().split('\n')
    
receiptsdata

baskets = [line.split(", ")[1:] for line in receiptsdata[0:-1]]



