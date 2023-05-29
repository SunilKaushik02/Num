# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:17:45 2023

@author: sunilkaushik02
"""
import pandas as pd
import streamlit as st

st.title('Numerology Calculator (Chaldean and Pythogorean)')

num_dict={'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':1,
    'K':2,
    'L':3,
    'M':4,
    'N':5,
    'O':6,
    'P':7,
    'Q':8,
    'R':9,
    'S':1,
    'T':2,
    'U':3,
    'V':4,
    'W':5,
    'X':6,
    'Y':7,
    'Z':8}

chal_dict={'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':8,
    'G':3,
    'H':5,
    'I':1,
    'J':1,
    'K':2,
    'L':3,
    'M':4,
    'N':5,
    'O':7,
    'P':8,
    'Q':1,
    'R':2,
    'S':3,
    'T':4,
    'U':6,
    'V':6,
    'W':6,
    'X':5,
    'Y':1,
    'Z':7}

# def num_func():
    
    
try:
    name=st.text_input("Please enter name (in any case) to convert to numerology: ")
    name=name.replace(' ','').upper()
    
    count=0
    for x in name:
        count+=num_dict.get(x)
        
    c_count=0
    for x in name:
        c_count+=chal_dict.get(x)
        
    #     print(f'''Pythogorean numerology is: {count} and 
    #     chaldean numerology is: {c_count}''')
    
    
    
    st.write(f'''According to widely used **Chaldean numerology** value is: {c_count} with final value {sum([int(x) for x in str(sum([int(x) for x in str(c_count)]))])} \n and for *Pythogorean numerology* value is: {count} with final value {sum([int(x) for x in str(sum([int(x) for x in str(count)]))])}''')
    st.write('''**How to use**: 
             Please check the final value above and compare it with your *birth date* eg: if you birth date is 3 and final value above show 3 then your name might push you ahead in life 
             *Please consult a numerologist for further questions as this is a nuanced topic and this insight is just a drop in the ocean*''') 
    
except:
    
    st.write('Please enter only characters and no numbers/special characters')
