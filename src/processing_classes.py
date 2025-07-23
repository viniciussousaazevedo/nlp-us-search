import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import re
import pandas as pd

class HTML:
    def __init__(self, filepath: str):
        self.noum_tags = ["mat-label", "mat-hint", "mat-option", "button"]
        self.stemmer = PorterStemmer()
        self.filename = filepath
        self.original = self.load()
        self.processed = self.get_tags_text()
    
    def get_tags_text(self) -> str:
        soup = BeautifulSoup(self.original, "html.parser")
        extracted_texts = []
        for tag_name in self.noum_tags:
            noum_tags = soup.find_all(tag_name)
            for tag in noum_tags:
                extracted_texts.append(tag.get_text(separator=" ").strip())
        extracted_text = " ".join(extracted_texts).lower()
        stemmed_extraction = self.stemmer.stem(extracted_text)
        return stemmed_extraction
    
    def load(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

class UserStory:
    def __init__(self, original: str):
        self.nlp_model = spacy.load("en_core_web_sm")
        self.stemmer = PorterStemmer()
        self.original = original
        self.processed = self.get_weighted_chunks()
        self.total_weight = self.get_total_weight()
    
    def get_weighted_chunks(self) -> dict:
        # Extracting noum chunks from US
        doc = self.nlp_model(self.original)
        weighted_chunks = dict()

        for chunk in doc.noun_chunks:
            chunk_text = chunk.text.strip()

            # Replacing acronyms
            glossary = pd.read_csv('./data/glossary.csv').sort_values(by='acronym', key=lambda x: x.str.len(), ascending=False)
            for _, row in glossary.iterrows():
                acronym = row['acronym']
                meaning = row['meaning']
                pattern = r'\b' + re.escape(acronym) + r'\b'
                chunk_text = re.sub(pattern, meaning, chunk_text, flags=re.IGNORECASE)
            
            # Removing special characters
            chunk_text = re.sub(r'[^A-Za-z0-9À-ÿ\s]', ' ', chunk_text)

            for word in chunk_text.split():
                # Removing Stop Words
                token_lower = word.lower()
                if token_lower in STOP_WORDS:
                    continue 

                # Applying weights
                word = word.strip('\'"')
                has_priority = (
                    word.isupper() or 
                    word.istitle() or 
                    (word.startswith(("'", '"')) and word.endswith(("'", '"')))
                )
                weight = 2 if has_priority else 1

                # Stemming
                token_lower = self.stemmer.stem(token_lower)

                # Storing
                if token_lower not in weighted_chunks: # Avoiding 'fruit' override 'FRUIT'
                    weighted_chunks[token_lower] = weight

        return weighted_chunks
    
    def get_total_weight(self):
        total_weight = 0
        for weight in self.processed.values():
            total_weight += weight
        return total_weight