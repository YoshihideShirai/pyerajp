# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from unittest import TestCase

from nose.tools import eq_, raises

from pyerajp.gengo import strjpftime, GengoNotFoundException


class TestConverter(TestCase):
    @raises(GengoNotFoundException)
    def test_not_excepted_time(self):
        exception_time = datetime.datetime(1600, 9, 7)
        strjpftime(exception_time)

    def test_excepted_time(self):
        first_genna_time = datetime.datetime(1615, 9, 5)
        eq_(strjpftime(first_genna_time, "%O%E年"), "元和元年")
        
        first_kyouwa_time = datetime.datetime(1801, 3, 19)
        eq_(strjpftime(first_kyouwa_time, "%O%E年"), "享和元年")
        
        last_meiji_time = datetime.datetime(1912, 7, 29)
        eq_(strjpftime(last_meiji_time), "M45.07.29")
        eq_(strjpftime(last_meiji_time, "%O%E年"), "明治45年")

        first_taisho_time = datetime.datetime(1912, 7, 30)
        eq_(strjpftime(first_taisho_time), "T1.07.30")
        eq_(strjpftime(first_taisho_time, "%O%E年"), "大正元年")

        last_taisho_time = datetime.datetime(1926, 12, 24)
        eq_(strjpftime(last_taisho_time), "T15.12.24")
        eq_(strjpftime(last_taisho_time, "%O%E年"), "大正15年")

        first_showa_time = datetime.datetime(1926, 12, 25)
        eq_(strjpftime(first_showa_time), "S1.12.25")
        eq_(strjpftime(first_showa_time, "%O%E年"), "昭和元年")

        last_showa_time = datetime.datetime(1989, 1, 7)
        eq_(strjpftime(last_showa_time), "S64.01.07")
        eq_(strjpftime(last_showa_time, "%O%E年"), "昭和64年")


        first_heisei_time = datetime.datetime(1989, 1, 8)
        eq_(strjpftime(first_heisei_time), "H1.01.08")
        eq_(strjpftime(first_heisei_time, "%O%E年"), "平成元年")

        heisei_time = datetime.datetime(2015, 8, 5)
        eq_(strjpftime(heisei_time), "H27.08.05")
        eq_(strjpftime(heisei_time, "%O%E年"), "平成27年")

        first_reiwa_time = datetime.datetime(2019, 5, 1)
        eq_(strjpftime(first_reiwa_time), "R1.05.01")
        eq_(strjpftime(first_reiwa_time, "%O%E年"), "令和元年")

        reiwa_time = datetime.datetime(2022, 12, 23)
        eq_(strjpftime(reiwa_time), "R4.12.23")
        eq_(strjpftime(reiwa_time, "%O%E年"), "令和4年")
