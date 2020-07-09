#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[2]:


#%matplotlib inline
#IPython import get_ipython

#from IPython.core.pylabtools import figsize


#figsize(12, 8)

#sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[2]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# ## Inicie sua análise a partir da parte 1 a partir daqui

# ### Distribuição Normal

# In[3]:


# Sua análise da parte 1 começa aqui.
sns.distplot(dataframe['normal'])


# ### Distribuição Binomial

# In[4]:


sns.distplot(dataframe['binomial'], bins=range(4, 40), kde=False, hist_kws={"alpha": 0.9})


# #### Resolução Questão 01

# In[5]:


df_normal_quartis = dataframe['normal'].describe().loc[['25%','50%','75%']]
df_normal_quartis


# In[ ]:





# In[6]:


df_binomial_quartis = dataframe['binomial'].describe().loc[['25%','50%','75%']]
df_binomial_quartis


# In[7]:


sub_quartis = df_normal_quartis - df_binomial_quartis
sub_quartis = sub_quartis.round(3)
sub_quartis


# In[8]:


quartis = tuple(list(sub_quartis))
quartis


# #### Resolução Questão 02

# In[47]:


norm = dataframe['normal']
ecdf = ECDF(norm)
prob_norm = ecdf(norm.mean() + norm.std()) - ecdf(norm.mean() - norm.std())
prob_norm = prob_norm.round(3)
prob_norm


# #### Resolução da Questão 03

# In[40]:


norm = dataframe['normal']
binom = dataframe['binomial']


# ##### Criando um dataframe com os resultados da média e variância da normal

# In[55]:


dn = {'media':[norm.mean()], 'variancia':[norm.var()]}
df_norm = pd.DataFrame(data = dn)
df_norm


# ##### Criando um dataframe com os resultados da média e variância da binomial

# In[56]:


db = {'media':[binom.mean()], 'variancia':[binom.var()]}
df_binom = pd.DataFrame(data = db)
df_binom


# In[62]:


result = df_binom.loc[0] - df_norm.loc[0]
result = result.round(3)
result = tuple(list(result))
result


# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[5]:


def q1():
    # Retorne aqui o resultado da questão 1.
    df_normal_quartis = dataframe['normal'].describe().loc[['25%','50%','75%']]
    df_binomial_quartis = dataframe['binomial'].describe().loc[['25%','50%','75%']]
    sub_quartis = df_normal_quartis - df_binomial_quartis
    sub_quartis = sub_quartis.round(3)
    quartis = tuple(list(sub_quartis))
    
    return quartis


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[14]:


def q2():
    # Retorne aqui o resultado da questão 2.
    norm = dataframe['normal']
    ecdf = ECDF(norm)
    prob_norm = ecdf(norm.mean() + norm.std()) - ecdf(norm.mean() - norm.std())
    prob_norm = prob_norm.round(3)
    
    return float(prob_norm)


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[7]:


def q3():
    # Retorne aqui o resultado da questão 3.
    norm = dataframe['normal']
    binom = dataframe['binomial']
    dn = {'media':[norm.mean()], 'variancia':[norm.var()]}
    df_norm = pd.DataFrame(data = dn)
    db = {'media':[binom.mean()], 'variancia':[binom.var()]}
    df_binom = pd.DataFrame(data = db)
    result = df_binom.loc[0] - df_norm.loc[0]
    result = result.round(3)
    result = tuple(list(result))   
    
    return result


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# ## Parte 2

# ### _Setup_ da parte 2

# In[32]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[33]:


# Sua análise da parte 2 começa aqui.
stars.head()


# In[34]:


stars.shape


# #### Resolução questão 04

# In[35]:


not_pulsar = stars.loc[stars['target'] == False]
mean_not_pulsar = not_pulsar['mean_profile']


# In[36]:


x = mean_not_pulsar
false_pulsar_mean_profile_standardized = (x-x.mean()) / x.std()


# ##### Quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função norm.ppf() disponível em scipy.stats

# In[39]:


q_80 = sct.norm.ppf(0.8, loc=0, scale=1)
q_90 = sct.norm.ppf(0.9, loc=0, scale=1)
q_95 = sct.norm.ppf(0.95, loc=0, scale=1)
#calculando média e desvio padrão para a tabela normalizada da questão
#media_pulsar = false_pulsar_mean_profile_standardized.mean()
#dpadrao_pulsar = false_pulsar_mean_profile_standardized.std()
#cálculo das probabilidades usando os quantis ideais com as medias e desvio padrão da questão
#prob_80 = sct.norm.cdf(q_80, loc=media_pulsar, scale=dpadrao_pulsar).round(3)
#prob_90 = sct.norm.cdf(q_90, loc=media_pulsar, scale=dpadrao_pulsar).round(3)
#prob_95 = sct.norm.cdf(q_95, loc=media_pulsar, scale=dpadrao_pulsar).round(3)
#prob_tuple = (prob_80, prob_90, prob_95)
#prob_tuple


# ##### Probabilidade associadas a esses quantis utilizando a CDF empírica da variável false_pulsar_mean_profile_standardized

# In[42]:


ecdf = ECDF(false_pulsar_mean_profile_standardized)
prob_quantis = (ecdf(q_80).round(3), ecdf(q_90).round(3), ecdf(q_95).round(3))
prob_quantis


# #### Resolução questão 05

# #### Qual a diferença entre os quantis Q1, Q2 e Q3 de false_pulsar_mean_profile_standardized e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1?

# In[82]:


false_pulsar_mean_profile_standardized


# In[170]:


pulsar_quartis = false_pulsar_mean_profile_standardized.describe().loc[['25%','50%','75%']]
pulsar_quartis


# In[171]:


q_25 = sct.norm.ppf(0.25, loc=0, scale=1)
q_50 = sct.norm.ppf(0.50, loc=0, scale=1)
q_75 = sct.norm.ppf(0.75, loc=0, scale=1)
normal_quartis_list = [q_25, q_50, q_75]
labels = ["25%", "50%", "75%"]
d = {'mean_profile': [q_25, q_50, q_75]}

normal_quartis = pd.DataFrame(data=d,index=labels)
normal_quartis = normal_quartis["mean_profile"]
normal_quartis


# In[173]:


sub_quartis = pulsar_quartis - normal_quartis
sub_quartis = sub_quartis.round(3)
result = tuple(list(sub_quartis))
result


# In[ ]:





# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[10]:


def q4():
    # Retorne aqui o resultado da questão 4.
    #Configurando padronização
    not_pulsar = stars.loc[stars['target'] == False]
    mean_not_pulsar = not_pulsar['mean_profile']
    x = mean_not_pulsar
    false_pulsar_mean_profile_standardized = (x-x.mean()) / x.std()
    #quantis para média = 0 e desvio padrão = 1
    q_80 = sct.norm.ppf(0.8, loc=0, scale=1)
    q_90 = sct.norm.ppf(0.9, loc=0, scale=1)
    q_95 = sct.norm.ppf(0.95, loc=0, scale=1)
    #Probabilidades associadas aos quantis
    ecdf = ECDF(false_pulsar_mean_profile_standardized)
    prob_quantis = (ecdf(q_80).round(3), ecdf(q_90).round(3), ecdf(q_95).round(3))
    prob_quantis
    
    return prob_quantis


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[11]:


def q5():
    # Retorne aqui o resultado da questão 5.
    #Configurando padronização
    not_pulsar = stars.loc[stars['target'] == False]
    mean_not_pulsar = not_pulsar['mean_profile']
    x = mean_not_pulsar
    false_pulsar_mean_profile_standardized = (x-x.mean()) / x.std()
    #Calculando os Quartis do false_pulsar_mean_profile_standardized
    pulsar_quartis = false_pulsar_mean_profile_standardized.describe().loc[['25%','50%','75%']]
    #Calculando os Quartis de uma distribuição normal
    q_25 = sct.norm.ppf(0.25, loc=0, scale=1)
    q_50 = sct.norm.ppf(0.50, loc=0, scale=1)
    q_75 = sct.norm.ppf(0.75, loc=0, scale=1)
    #Criando um dataframe para os Quartis da distribuição normal
    normal_quartis_list = [q_25, q_50, q_75]
    labels = ["25%", "50%", "75%"]
    d = {'mean_profile': [q_25, q_50, q_75]}
    normal_quartis = pd.DataFrame(data=d,index=labels)
    normal_quartis = normal_quartis["mean_profile"]
    #Realizando a subtração entre os dataframes
    sub_quartis = pulsar_quartis - normal_quartis
    sub_quartis = sub_quartis.round(3)
    result = tuple(list(sub_quartis))
    
    return result


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.
