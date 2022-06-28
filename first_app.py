
import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & blueberry Oatmeal 🥣')
streamlit.text('🥗 Kale, Spinach, Rocket Smoothie 🥗')
streamlit.text('🐔 Hard-Boiled Free-Range Egg 🐔')
streamlit.text('🥑Avo Toast Bitch 🥑')
streamlit.header('Build Your Own Fruit Smoothie')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
