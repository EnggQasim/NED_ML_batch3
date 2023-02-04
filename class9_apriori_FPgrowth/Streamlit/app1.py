import streamlit as st

data = [["Milk","Onion","Nutmeg","Kidney Beans","Eggs","Yogurt"],
       ["Dill","Onion","Nutmeg","Kidney Beans","Eggs","Yogurt"],
       ["Milk","Apple","Kidney Beans","Eggs"],
       ["Milk","Unicorn","Corn","Kidney Beans","Yogurt"],
       ["Corn","Onion","Onion","Kidney Beans","Ice Cream","Eggs"]]

import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()

te_arry = te.fit(data).transform(data)
df = pd.DataFrame(te_arry, columns=te.columns_)

from mlxtend.frequent_patterns import apriori, fpgrowth





st.title("NED Machine Learning Recommendation System")





purchase_item = st.radio('Pick one', te.columns_)
ratio = 0.5

st.header("FpGrowth")
rec1 = fpgrowth(df, min_support=ratio, use_colnames=True)
rec1['itemsets'] = rec1['itemsets'].apply(str)
rec1 = rec1[rec1['itemsets'].str.contains(purchase_item)]

rec2 = apriori(df, min_support=ratio, use_colnames=True, low_memory=True)
rec2['itemsets'] = rec2['itemsets'].apply(str)
rec2 = rec2[rec2['itemsets'].str.contains(purchase_item)]

st.table(rec1)
st.header("Apriori")
st.table(rec2)
