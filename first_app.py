
import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('ð¥£ Omega 3 & blueberry Oatmeal ð¥£')
streamlit.text('ð¥ Kale, Spinach, Rocket Smoothie ð¥')
streamlit.text('ð Hard-Boiled Free-Range Egg ð')
streamlit.text('ð¥Avo Toast Bitch ð¥')
streamlit.header('Build Your Own Fruit Smoothie')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.dataframe(my_fruit_list)
steamlist.multiselect("Pick Some Fruits:", list(my_fruit_list.index))
