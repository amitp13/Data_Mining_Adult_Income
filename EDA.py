# #### 2. Exploratory Data Analysis

# In[51]:


df.head()


# In[52]:


sns.pairplot(df)


# In[85]:


fig = plt.figure(figsize=(10,10)) 
sns.boxplot(x="income", y="age", data=df)
plt.title("Income vs Age")
plt.show()


# In[82]:


fig = plt.figure(figsize=(10,10)) 
ax = sns.countplot(y="workclass", hue="income", data=df).set_title("workclass vs count")


# In[86]:


fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,16))
sns.countplot(y="education", hue="income",data=df, ax = ax1).set_title("Income vs Education");
sns.countplot(y="relationship", hue="income",data=df, ax = ax2).set_title("Income vs Relationship");
plt.show()


# In[92]:


sns.catplot(x="sex", hue="income", kind="count",data=df)
plt.title("Income vs Sex");


# In[93]:


sns.catplot(x='income',y='hours.per.week',data=df)
plt.title("Income vs Hours per Week")


# In[ ]:




