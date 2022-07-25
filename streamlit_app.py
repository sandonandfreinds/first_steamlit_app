#created file

import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

#get fruity vice data for a given fruit
def get_fruity_vice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.title('My Parents New Healthy Diner')
  
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)


#pick list
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display list
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    function_return = get_fruity_vice_data(fruit_choice)
    streamlit.dataframe(function_return)
except URLError as e:
  streamlit.error()

streamlit.text("the fruit load list contains:")

#get fruit load list
def get_fruit_load_list():
    with my_cnx.cursor as my_cur:
        my_cur.execute("select * from FRUIT_LOAD_LIST")
        return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

streamlit.stop()
##############


fruit_choice = streamlit.text_input('What fruit would you like to add?', '')
streamlit.write('The user entered ', fruit_choice)
my_cur.execute("insert into pc_rivery_db.public.FRUIT_LOAD_LIST values ('from streamlit')")
streamlit.text("the fruit load list contains:")
my_cur.execute("select * from FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)

