
# coding: utf-8

# In[4]:


from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopword
import sys


# In[5]:


tokenizer = RegexpTokenizer(r'\w+')


# In[8]:


en_stop = set(stopwords.words('english'))
ps =PorterStemmer()


# In[9]:


def StemmedReview(review):
    review = review.lower()
    review = review.replace("<br /><br />"," ")
    
    tokens = tokenizer.tokenize(review)
    
    new_tok = [tok for tok in tokens if token not in en_stop]
    
    stemmed_tokens = [ps.stem(token) for token in new_tok]
    
    final_rev  = ' '.join(stemmed_tokens)
    
    return final_rev



# In[ ]:


def stemmedDoc(inputFile,outputFile):
	with open(inputFile,encoding="utf8") as f:
		reviews = f.readline()

	out = open(outputFile,'w',encoding = " utf8")
	for review in reviews:
		clean_review = StemmedReview(review)
		print((clean_review),file = out)


    out.close()


inputFile = sys.argv[1]
outputFile = sys.argv[2]

       

