import streamlit as st
import pandas as pd
import sqlite3

# color pallette
cnf, dth, rec, act = '#393e46', '#ff2e63', '#21bf73', '#fe9801'

# Full width
st.set_page_config(layout="wide")

def from_data():
    conn = sqlite3.connect('./database/covid.db')
    # Load the data from a SQL query
    query = "SELECT * FROM covid"
    data = pd.read_sql(query, conn)
    return data

def intro():
    st.write("# Сovid Data analysis!")

    st.markdown(
        """
        All about the project
    """
    )

if __name__ == '__main__':
    intro()