# BUSINESS SCIENCE UNIVERSITY
# COURSE: DS4B 201-P PYTHON MACHINE LEARNING
# MODULE 2: DATA UNDERSTANDING: EXPLORATORY
# 
# ----

# LIBRARIES ----
#%%
import pandas as pd
import numpy as np


# Data

import email_lead_scoring as els


df = els.db_read_els_data()
df.head()

#%%
# Function: Explore Sales By Category  
def explore_sales_by_category(data, category = 'country_code', sort_by = ['Sales', 'prop_in_group' ]):
    """
    Explore Sales by Category
    """
    
    # handle sort_by
    if type(sort_by) is list:
        sort_by = sort_by[0]
    
        
    # Data Manipulation
    
    ret = data \
        .groupby(category) \
        .agg(dict(made_purchase = ['sum', lambda x: sum(x) / len(x)])) \
        .set_axis(['sales', 'prop_in_group'], axis=1) \
        .assign(prop_overall = lambda x: x['sales'] / sum(x['sales'])) \
        .sort_values(by= sort_by, ascending=False) \
        .assign(prop_cumsum = lambda x: x['prop_overall'].cumsum() 
        ) 
        
    return ret
    
    #%%
    explore_sales_by_category(
        data =df,
        category = 'country_code',
        sort_by = 'sales'
    )
    # Group By Category

    

    df.head()

#%%
# Function: Explore Sales by Numeric Feature
def explore_sales_by_numeric(
    data,
    numeric = 'tag_count',
    q = [0.10, 0.50, 0.90]
):
    if type(numeric) is list:
        feature_list = ['made_purchase', *numeric ]
    else:
        feature_list = ['made_purchase', numeric]
        
    ret = data[feature_list] \
        .groupby('made_purchase') \
        .quantile(q=q, numeric_only=True)
        
    return ret


explore_sales_by_numeric(
    data = df,
    numeric = ['member_rating', 'tag_count'],
    q= [0.05, 0.25, 0.5, 0.75, 0.95]
) 

#  TEST THEM OUT ---- 


# %%
import email_lead_scoring as els
els.explore_sales_by_category
# %%
els.explore_sales_by_numeric

explore_sales_by_numeric(
    data = df,
    numeric = ['member_rating', 'tag_count'],
    q= [0.05, 0.25, 0.5, 0.75, 0.95]
)