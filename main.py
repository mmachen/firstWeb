

import streamlit as st

st.write('You have three bags, each containing two marbles. Bag A contains two white marbles, Bag B contains two black marbles, and Bag C contains one white marble and one black marble.') 
x = st.text_input('Enter fraction with no spaces:')
if len(x) != 0:
    if x == "2/3":
        st.write('I love you Xiaoxi!')
    else:
        st.write('Try again :frowning:')

# heroku login
# heroku create
# git push heroku master
# heroku open 