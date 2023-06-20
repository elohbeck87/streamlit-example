import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page title and favicon
st.set_page_config(page_title='Streamlit Latest Features', page_icon=':rocket:')

# Add a title and description
st.title('Streamlit Latest Features')
st.markdown("""
This Streamlit app demonstrates some of the latest features of Streamlit.
Feel free to explore and experiment with the different components!
""")

# Sidebar
st.sidebar.subheader('Components')
selected_component = st.sidebar.selectbox('Select a component', ['Widgets', 'Plots', 'DataFrame'])

# Widgets Section
if selected_component == 'Widgets':
    st.header('Widgets')
    st.subheader('Interactive Widgets')
    
    # Slider
    st.slider('Select a value', 0, 10)

    # Checkbox
    st.checkbox('Check me!')

    # Selectbox
    st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])

    # Radio button
    st.radio('Choose one', ['A', 'B', 'C'])

    # Date input
    st.date_input('Select a date')

    # Time input
    st.time_input('Select a time')

    # File uploader
    st.file_uploader('Upload a file')

    st.subheader('Display Widgets')
    
    # Text
    st.text('This is a text widget.')

    # Markdown
    st.markdown('**This** is a markdown widget.')

    # Code
    st.code('print("Hello, Streamlit!")')

# Plots Section
if selected_component == 'Plots':
    st.header('Plots')
    st.subheader('Interactive Charts')
    
    # Line chart
    df = pd.DataFrame({'x': np.arange(10), 'y': np.random.randn(10)})
    fig = px.line(df, x='x', y='y')
    st.plotly_chart(fig, use_container_width=True)

    # Bar chart
    df = pd.DataFrame({'category': ['A', 'B', 'C'], 'count': [3, 6, 9]})
    fig = px.bar(df, x='category', y='count')
    st.plotly_chart(fig, use_container_width=True)

    # Scatter plot
    df = pd.DataFrame({'x': np.random.randn(50), 'y': np.random.randn(50)})
    fig = px.scatter(df, x='x', y='y')
    st.plotly_chart(fig, use_container_width=True)

# DataFrame Section
if selected_component == 'DataFrame':
    st.header('DataFrame')
    st.subheader('Interactive Table')
    
    # Create sample DataFrame
    df = pd.DataFrame({'Name': ['John', 'Alice', 'Bob'],
                       'Age': [25, 30, 35],
                       'City': ['New York', 'London', 'Paris']})
    
    # Display DataFrame
    st.dataframe(df)

    # Display table with style
    st.table(df.style.highlight_max(axis=0))

# Show Streamlit logo and footer
st.image('streamlit_logo.png', width=150)
st.markdown("---")
st.markdown("Powered by [Streamlit](https://streamlit.io/)")

