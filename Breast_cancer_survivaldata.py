#!/usr/bin/env python
# coding: utf-8

# # **Breast Cancer Survival Data**
# 
# **Introduction**
# 
# The dataset contains cases from a study that was conducted between 1958 and 1970 at the University of Chicago's Billings Hospital on the survival of patients who had undergone surgery for breast cancer.
# 
# The objective of this notebook is to find the problem statement and do EDA to find insights of the breast cancer Survival data. The attached data has 306 records.  This data has four Attributes.   
# 1. Age of patient at time of operation (numerical) 
# 2. Patient's year of operation (year - 1900, numerical) 
# 3. Number of positive axillary nodes detected (numerical) 
# 4. Survival status (class attribute) 
# -- 1 = the patient survived 5 years or longer 
# -- 2 = the patient died within 5 year
# 

# ![title](https://raw.githubusercontent.com/jahnavirayapati/Breast_cancer_survivaldata/master/images/BC.png)

# ###  Load the packages & data

# In[1]:


import numpy as np                                                 # Implemennts milti-dimensional array and matrices
import pandas as pd                                                # For data manipulation and analysis
import pandas_profiling
import matplotlib.pyplot as plt                                    # Plotting library for Python programming language and it's numerical mathematics extension NumPy
import seaborn as sns                                              # Provides a high level interface for drawing attractive and informative statistical graphics
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()

from subprocess import check_output


# In[6]:


Breast_cancer_surdata=pd.read_csv("C:/Users/jahna/OneDrive/Documents/Desktop/DS/Project/Breast_cancer_survival.csv")


# ###  Data Profiling

# In[7]:


Breast_cancer_surdata.shape


# In[8]:


Breast_cancer_surdata.head


# In[9]:


Breast_cancer_surdata.tail()


# In[10]:


Breast_cancer_surdata.info()


# In[11]:


Breast_cancer_surdata.describe()


# ####  Pre profiling

# In[19]:


profile_bsd = pandas_profiling.ProfileReport(Breast_cancer_surdata)
profile_bsd.to_file("bsd_preprofile = Breast_cancer_surdata_before_preprocessing.html")


# In[21]:


profile_bsd


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




