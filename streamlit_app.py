#created file

import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')
  
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

#pick list
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display list
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


# formats json data for UI
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# displays json data in panda dataframe 
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("the fruit load list contains:")
streamlit.dataframe(my_data_row)


fruit_choice = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('The user entered ', fruit_choice)
#my_cur.execute(f"insert into pc_rivery_db.public.FRUIT_LOAD_LIST values ('jackfruit')")
streamlit.text("the fruit load list contains:")
my_cur.execute("select * from FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)

