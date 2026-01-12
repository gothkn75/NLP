import nltk
import re
import string  
# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
#input_text 
input_text = "Hello everyone, my name is Kieu Nhu. I am 20 years old and I come from Quang Ngai province, Vietnam. I am currently a student at HUFLIT (Ho Chi Minh City University of Foreign Languages – Information Technology), majoring in English Language." 
print("ORIGINAL TEXT:\n", input_text)
#Tokenization
tokens = word_tokenize(input_text)
print("\nTOKENIZED TEXT:\n", tokens)    
#Lowercasing
lowercased_tokens = [token.lower() for token in tokens]
print("\nLOWERCASED TEXT:\n", lowercased_tokens)
#stopword removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lowercased_tokens if token not in stop_words]
print("\nTEXT AFTER STOPWORD REMOVAL:\n", filtered_tokens)
#stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
print("\nSTEMMED TEXT:\n", stemmed_tokens)
#lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
print("\nLEMMATIZED TEXT:\n", lemmatized_tokens)
#punctuation removal
punctuation_removed_tokens = [token for token in filtered_tokens if token not in string.punctuation]
print("\nTEXT AFTER PUNCTUATION REMOVAL:\n", punctuation_removed_tokens)
#text normalization function
def normalize_text(text):
    tokens = word_tokenize(text)
    lowercased_tokens = [token.lower() for token in tokens]
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in lowercased_tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    punctuation_removed_tokens = [token for token in lemmatized_tokens if token not in string.punctuation]
    return punctuation_removed_tokens   
print("\nNORMALIZED TEXT:\n", normalize_text(input_text))   
print("\nPROCESSING COMPLETE.")
print("Thank you for using the text processing script!")
