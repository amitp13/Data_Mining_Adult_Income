# 3. Model Building

# From the EDA we can see that certain variables affect income catagory, hence we will using those variables. Our dependant variable(y) which is income is split in two catagories. Hence our best bet would be to use logistic regression and random forests for classification and prediction.   

# In[846]:


uad_df = df


# In[847]:


uad_df = uad_df.drop(['fnlwgt','native.country','relationship','marital.status','race','education'], axis=1)
uad_df = uad_df.dropna()


# In[848]:


uad_df


# In[849]:


rf_df = pd.get_dummies(uad_df, columns=["workclass",'occupation'],   #"native.country","race","relationship,"education",'marital.status'
                         prefix=["is_workclass","is_occupation"]) #"is_race","is_native.country","is_relationship","is_education",'is_marital.status'


# In[850]:


rf_df


# In[851]:


y = rf_df['income']
x = rf_df.drop(['income'], axis=1)


# In[852]:


train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.20, random_state = 42)


# <b>Random Forest Classifier</b>
# 
# The first algorithm we will test is the random forrest classifier. We will check its performance using metric like accuracy, confusion matrix, precision and recall. 

# In[853]:


randomforest = RandomForestClassifier()
fit=randomforest.fit(train_x,train_y)
y_pred = fit.predict(test_x)


# In[854]:


def plot_confusion_matrix(cm, classes, normalize=False):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    cmap = plt.cm.Blues
    title = "Confusion Matrix"
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        cm = np.around(cm, decimals=3)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


# In[855]:


cfm = confusion_matrix(test_y,y_pred)
plot_confusion_matrix(cfm,classes=["<=50K", ">50K"], normalize=True)


# In[856]:


print("Accuracy:",metrics.accuracy_score(test_y, y_pred))


# <b>Logistic Regression</b>
# 
# The second algorithm we will test is logisitc regression to predict our dependent variable. We will check its performance using metrics like rmse and r2 values. 

# In[857]:


logreg = LogisticRegression()
fit2 = logreg.fit(train_x,train_y)
y_pred2=fit2.predict(test_x)
warnings.filterwarnings('ignore')


# In[858]:


cfm = confusion_matrix(test_y,y_pred2)
plot_confusion_matrix(cfm,classes=["<=50K", ">50K"], normalize=True)


# In[859]:


print(classification_report(test_y,y_pred2))


# In[860]:


print("Accuracy:", accuracy_score(test_y, y_pred2))


# In[ ]: