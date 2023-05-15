import streamlit as st 
import pandas 

st.set_page_config(layout='wide')


st.image('images/photo.png') #main image


st.title('Don-fortune Tangban')


content = """ I am a DevOps engineer, Python programmer, and Salesforce administrator with a passion for delivering high-quality software solutions. Don-Fortune is a skilled professional who specializes in designing and implementing DevOps processes that streamline collaboration between development and operations teams.
With a deep understanding of Python programming, Don-Fortune is well-versed in building robust and scalable software applications that meet the evolving needs of businesses. Their expertise in Salesforce administration also makes them proficient in managing complex CRM implementations that help businesses grow and succeed."""
st.write(content)

st.write('Below you can find some of the apps i ave built with python. feel free to contact me!')

col1, empty_col,  col2 = st.columns(3)
data = pandas.read_csv('data.csv', sep=';')
with col1:
    for index, row in data[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")






with col2:
    for index, row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])

        st.write(f"[Source Code]({row['url']})")

