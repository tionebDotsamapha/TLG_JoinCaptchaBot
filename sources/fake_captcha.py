#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    fake_captcha.py
Description: "The objective of this function is to change the captcha validation numbers"
Author: "From PhalaTeamFR community"
Creation date: 04/11/2022
Last modified date: 04/11/2022
Version: 1.0
'''

import re

# Supported option in faking captcha numberslist
CAPTCHA_OPTION = ["ascending", 
                  "descending",
                  "reverse", 
                  "odd-even",
                  "even-odd"]

def fake_number_changed(captcha_option, captcha_num):
    captcha_list= re.findall('.',captcha_num)
    captcha_sorted = sorted(captcha_list)
    captcha_sorted_reversed = sorted(captcha_list, reverse=True)
    captcha_valid = ""

    # Case captcha numbers in ascending order
    if captcha_option == "ascending":
        for i in range(0, len(captcha_list)):     
           captcha_valid += captcha_sorted[i]
        print("ascending", captcha_valid)
        return captcha_valid

    # Case captcha numbers in descending order
    elif captcha_option == "descending":
        for i in range(0, len(captcha_list)):     
           captcha_valid += captcha_sorted_reversed[i]
        print("descending", captcha_valid)
        return captcha_valid

    # Case captcha numbers in reverse order      
    elif captcha_option == "reverse":
        for i in range(0, len(captcha_num)):     
           captcha_valid += captcha_num[len(captcha_num)-i-1]
        return captcha_valid

    else:
        odd_list = ""
        even_list = ""
        for i in range(0, len(captcha_num)):
            if int(captcha_sorted_reversed[i])%2 == 0:
                even_list = even_list + captcha_sorted_reversed[i]
            else :
                odd_list = odd_list + captcha_sorted_reversed[i]

        if captcha_option == "odd-even":
            return odd_list + even_list

        elif captcha_option == "even-odd":
            return even_list + odd_list
        else:
            return captcha_num