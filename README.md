# NLP US Search in HTML files
This repo makes a search over all HTML files in a root folder based on a US, or Acceptance Criteria, ranking all files based on Weighted Recall method.

## How to run
```bash
pip install -r requirements.txt
python src/main.py
```

## How is it done?
On the User Story:
- Glossary application (for acronyms resolution)
- Special characters removal
- Stop Words removal
- Noun chunks selection using spaCy
- Stemming
- Weight application over important words (i.e. upper case words, capitalized and quote-surrounded)

On the HTML files:
- Text between selected tags extraction (declared on the code itself)
- Stemming

On the Comparison and ranking:
- Score = (matches / us total weight)

> This is useful to understand (human or AI) the context and visual aspects that the provided User Story is reffering to. Make a run to see how it works!
