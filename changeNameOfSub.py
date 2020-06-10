# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:47:51 2020

@author: niloofar
"""

import glob
import os


def changeSubName(filmType, filePath):
    FilmList = []
    for x in filmType.split(','):
        FilmList += glob.glob(filePath+'/*.'+x)
    SubList = glob.glob(filePath+'/*.srt')
    for i in range(len(FilmList)):
        os.rename(SubList[i], '.'.join(FilmList[i].split('.')[:-1])+'.srt')

if __name__ == '__main__':
    
    filmType = input('try writing type of films(for example mkv or mp4,mkv --> do not use space): ')
    filePath = input('enter the path of files. for example C:/Users/user/downloads : ')
    changeSubName(filmType, filePath)
