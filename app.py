# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd

def main():
    st.title('Air Pessangers')

    #read data 
    df = pd.read_csv('AirPassengers.csv')
    print(df['Month']) #read
    
    #obtain your data
    df['Year'] = df['Month'].apply(lambda x :x.split('-')[0])
    #df.head()
    #show unique year 
    year = st.selectbox('Select year',df['Year'].unique() )
    
    #button trigger
    button = st.button('Show results')
    if button:
        #if if button is pressed subset data on selected data
        subset = df[df['Year']== year]
        #show subset table
        st.table(subset)

if __name__ == '__main__':   
    main()
    
