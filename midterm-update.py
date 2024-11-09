import streamlit as st

st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Project Midterm Update')

#----- Feature Engineering ------

st.header('Feature Engineering')
st.markdown('''
<p class="justified-text">
Feature engineering is essential to come up with meaningful features that capture product-specific, user-centric insights from the 
raw transactional data. The main broad categories of the features explored are:
1. <strong>Product-Level Features</strong> - 
    Aims to capture the popularity and purchase trends for a product.
    Sample Features: reorder percentage, number of unique buyers, etc
<br><br>
2. <strong>User-Level Features</strong> - 
    Aims to capture user shopping cycles.
    Sample Features: days before reorder, number of reordered items, etc
<br><br>
3. <strong>Aisle and Department Features</strong> - 
    Aims to capture the correlation of purchases from the same broader aisle/department
</p>
''', unsafe_allow_html=True)
