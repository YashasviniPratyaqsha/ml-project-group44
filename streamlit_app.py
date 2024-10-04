import streamlit as st

st.title('Project Proposal')

st.header('Introduction')
st.markdown('''In today's competitive retail landscape, customers have no dearth of options. 
Boosting sales hinges on strategies spanning effective product placement, efficient inventory management 
that ensures product availability, and compelling promotions to induce customers to buy more. 
Analyzing purchase history can reveal valuable insights that are often not intuitive, 
such as the surprising correlation between diapers and beer found in a case study. Instacart, 
a popular grocery ordering platform, has open-sourced their anonymized transactional data spanning 
3 million grocery orders from more than 200,000 users. The dataset is ideal for analysis as it 
provides user-specific purchase history and captures purchase sequence, re-ordered items, and order 
placement times. Previous work in this domain has utilized association rule algorithms and regression 
models. In this project, we will build on these approaches to identify frequently purchased items, 
re-ordering patterns, peak purchase times, and other trends.''')

st.header("Problem Definition")
st.write("""
The objective of this project is to convert data given in the form of past customer orders 
to actionable knowledge/insights, which can be used to provide a better experience to the customers, 
while at the same time growing sales/revenue for the company.

We aim to achieve this by targeting two key objectives:
""")

st.write("""
1. **Purchase Trend Discovery** - Given a user and past user order history, identify purchasing patterns (ex. Clustering users with similar 
         purchasing behavior for product recommendation) through unsupervised learning algorithms. 
         This could be a useful input for product re-order prediction.

2. **Product Re-order Prediction** - Given a user, product and user order history, predict if the user will re-order the given product in 
         their next order through supervised learning algorithms.
""")


st.write("""
Solving for these objectives would provide valuable insights, which can be used for product inventory 
         management and improving customer experience (through bundled offers and effective product 
         recommendation).

""")