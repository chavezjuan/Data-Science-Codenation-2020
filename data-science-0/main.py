#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.head(5)


# ### Counting null values

# In[6]:


missing_data = black_friday.isnull()
missing_data.head(5)


# In[22]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# #### Question 01 Resolution

# In[6]:


black_friday.shape


# #### Question 02 Resolution

# In[11]:


gender_age = black_friday[['Gender', 'Age']]
female_age_filter = gender_age[(gender_age['Gender'] == 'F') & (gender_age['Age'] == '26-35')]
female_count = female_age_filter.groupby(['Age']).count()
int(female_count.values[0][0])


# #### Question 03 Resolution -revisar

# In[51]:


user_id_unique = pd.unique(black_friday["User_ID"])
len(user_id_unique)
#user_id = black_friday['User_ID'].values
#user_id_unique = pd.unique(gender_age)
#len(user_id_unique)


# In[18]:


black_friday.nunique()


# #### Question 04 Resolution

# In[8]:


data_types = black_friday.dtypes
data_types.nunique()


# #### Question 05 Resolution

# In[5]:


#counter = 0
#df_val = black_friday.values
#df_size = black_friday.shape[0]

#for i in range(0,df_size):
#    if black_friday.iloc[[i]].isnull().values.any():
#        counter += 1 
        
#result = counter/df_size
#result
black_friday.isnull().sum().max() / black_friday.shape[0]


# In[ ]:





# #### Question 06 Resolution

# In[13]:


biggest_null = 0
columns_null = black_friday.isnull()

for column in columns_null.columns.values.tolist():
    values_null = columns_null[column].value_counts()
    print(values_null)
    if len(values_null) > 1:
        if values_null[0] > biggest_null:
            biggest_null = values_null[0]
print(biggest_null)    


# ### Right One

# In[ ]:


df_columns = black_friday.columns
max_value = 0
for column in df_columns:
    null_number = black_friday[column].isna().sum()
    if null_number > max_value:
        max_value = null_number
print(max_value)    


# In[ ]:


columns_null = black_friday.isnull()

for column in columns_null.columns.values.tolist():
    values_null = columns_null[column].value_counts().reset_index()
    values_null.columns = [column, 'count']
    print(values_null.values)


# #### Question 7 Resolution

# In[ ]:


freq_values = black_friday['Product_Category_3'].value_counts().to_list()
print(freq_values[0])


# #### Question 8 Resolution

# In[14]:


df = black_friday["Purchase"]
df_norm = (df - df.mean())/(df.max() - df.min())
df_norm.mean()


# In[15]:


((black_friday['Purchase'] - black_friday['Purchase'].min())/
           (black_friday['Purchase'].max()-black_friday['Purchase'].min())).mean()


# #### Question 9 Resolution

# In[16]:


df = black_friday["Purchase"]
df_std = (df - df.mean())/df.std()
ranges = [-1, 1]
df_std_range = df_std.groupby(pd.cut(df_std, ranges, include_lowest=True)).count()
df_std_result = df_std_range.to_list()
df_std_result[0]


# In[ ]:





# #### Question 10 Resolution

# In[46]:


counter = 0
ct02_val = black_friday["Product_Category_2"].values.tolist()
ct03_val = black_friday["Product_Category_3"].values.tolist()

for i in range(0,len(ct02_val)):
    if black_friday["Product_Category_2"].iloc[[i]].isnull().values.any():
        counter += 1
        if not(black_friday["Product_Category_3"].iloc[[0]].isnull().values.any()):
            print(False)
            break
print(True)


# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[7]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[10]:


def q2():
    # Retorne aqui o resultado da questão 2.
    gender_age = black_friday[['Gender', 'Age']]
    female_age_filter = gender_age[(gender_age['Gender'] == 'F') & (gender_age['Age'] == '26-35')]
    female_count = female_age_filter.groupby(['Age']).count()
    return int(female_count.values[0][0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[25]:


def q3():
    # Retorne aqui o resultado da questão 3.
    user_id_unique = pd.unique(black_friday["User_ID"])
    return len(user_id_unique)


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[32]:


def q4():
    # Retorne aqui o resultado da questão 4.
    data_types = black_friday.dtypes
    return data_types.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    #counter = 0
    #df_val = black_friday.values
    #df_size = len(df_val)

    #for i in range(0,len(df_val)):
    #    if black_friday.iloc[[i]].isnull().values.any():
    #        counter += 1 

    #result = counter/df_size
    return float(black_friday.isnull().sum().max() / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    df_columns = black_friday.columns
    max_value = 0
    for column in df_columns:
        null_number = black_friday[column].isna().sum()
        if null_number > max_value:
            max_value = null_number  
    return int(max_value)


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    freq_values = black_friday['Product_Category_3'].value_counts().to_list()
    return freq_values[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[16]:


def q8():
    # Retorne aqui o resultado da questão 8.
    df = black_friday["Purchase"]
    df_norm = ((black_friday['Purchase'] - black_friday['Purchase'].min())/
           (black_friday['Purchase'].max()-black_friday['Purchase'].min()))
    return float(df_norm.mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    df = black_friday["Purchase"]
    df_std = (df - df.mean())/df.std()
    ranges = [-1, 1]
    df_std_range = df_std.groupby(pd.cut(df_std, ranges, include_lowest=True)).count()
    df_std_result = df_std_range.to_list()
    return df_std_result[0]


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    counter = 0
    ct02_val = black_friday["Product_Category_2"].values.tolist()
    ct03_val = black_friday["Product_Category_3"].values.tolist()

    for i in range(0,len(ct02_val)):
        if black_friday["Product_Category_2"].iloc[[i]].isnull().values.any():
            counter += 1
            if not(black_friday["Product_Category_3"].iloc[[0]].isnull().values.any()):
                return False
                break
    return True

