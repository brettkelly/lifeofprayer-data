#!/usr/bin/env/python3

import csv

infile = './1945lectionary.csv'


class LectionaryEntry(object):
    def __init__(self,
                 season,
                 week,
                 day,
                 date,
                 m_psalm,
                 m_first,
                 m_second,
                 e_psalm,
                 e_first,
                 e_second,
                 ):
        self.season = season
        self.week = week
        self.day = day
        self.date = date
        self.m_psalm = m_psalm
        self.m_first = m_first
        self.m_second = m_second
        self.e_psalm = e_psalm
        self.e_first = e_first
        self.e_second = e_second
