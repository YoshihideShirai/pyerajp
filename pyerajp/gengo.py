# -*- coding: utf-8 -*-
import datetime

class GengoNotFoundException(Exception):
    pass

class _gengo:
    def __init__(self,name,since,alpha=None):
        self.name = name
        self.since = since
        self.alpha = alpha

_gengo_list = [
        _gengo('令和',datetime.datetime(2019, 5, 1),alpha='R'),
        _gengo('平成',datetime.datetime(1989, 1, 8),alpha='H'),
        _gengo('昭和',datetime.datetime(1926,12,25),alpha='S'),
        _gengo('大正',datetime.datetime(1912, 7,30),alpha='T'),
        _gengo('明治',datetime.datetime(1868, 9, 8),alpha='M'),
        _gengo('慶応',datetime.datetime(1865, 5, 1)),
        _gengo('元治',datetime.datetime(1864, 3,27)),
        _gengo('文久',datetime.datetime(1861, 3,29)),
        _gengo('万延',datetime.datetime(1860, 4, 8)),
        _gengo('安政',datetime.datetime(1855, 1,15)),
        _gengo('嘉永',datetime.datetime(1848, 4, 1)),
        _gengo('弘化',datetime.datetime(1845, 1, 8)),
        _gengo('天保',datetime.datetime(1831, 1,23)),
        _gengo('文政',datetime.datetime(1818, 5,26)),
        _gengo('文化',datetime.datetime(1804, 3,22)),
        _gengo('享和',datetime.datetime(1801, 3,19)),
        _gengo('寛政',datetime.datetime(1789, 2,19)),
        _gengo('天明',datetime.datetime(1781, 4,25)),
        _gengo('安永',datetime.datetime(1772,12,10)),
        _gengo('明和',datetime.datetime(1764, 6, 2)),
        _gengo('宝暦',datetime.datetime(1751,12,14)),
    ]

class Gengo:
    def __init__(self,name):
        self.name = name
        self.alpha = None
        self.since = None
        self.end = None
        for g in _gengo_list:
            if g.name == name:
                self.since = g.since
                self.alpha = g.alpha
                break
            self.end = g.since
        if self.since == None:
            raise GengoNotFoundException()

def strjpftime(time=datetime.datetime.today(), format="%o%E.%m.%d"):
    """
    Convert to Japanese era
    :param time:
    :param format: strftime format
        New available here
            - %o  : alphabet era
            - %O  : Chinese character era
            - %E  : era year
    :return:
    """
    era_year = None
    gengo = None
    for g in _gengo_list:
        if time >= g.since:
            gengo = g
            break

    if gengo == None:
        raise GengoNotFoundException()

    era_year = time.year - gengo.since.year + 1
    if era_year == 1 and format.find("%O") > -1:
        era_year = '元'
    else:
        era_year = str(era_year)

    if gengo.alpha != None:
        format = format.replace("%o" ,gengo.alpha)
    else :
        format = format.replace("%o" ,gengo.name)
    format = format.replace("%O" ,gengo.name )
    format = format.replace("%E" ,era_year   )
    return time.strftime(format)

