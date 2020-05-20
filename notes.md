# M11 - Text Mining, by Sergey Khoroshenkikh



## Day 01

### Python refresher

- `pprint()` : pretty print, needs to be imported: `from pprint import pprint`
- `defaultdict()` provides default value to a key and doesn't raise `KeyError`.

```py
from collections import defaultdict
dict = defaultdict(int)  # default value 0. defaultdict(<type>)
```
- `Counter()` powerful container to count things.

```py
from collections import Counter
c = Counter()
print(c.most_common()[:3]) # top 3
```

- `re` find things, regex
file:///home/dobi/ahsu/2020/11-txt_mining/notebooks/01-text_analysis_tools_nishit_shah.ipynb
```py
import re
# find all words in hamlet and convert to lowercase
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
```

- `plt`

```py
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.hist(len_tokens, bins=0)
plt.show()
```

### spaCy

- `nlp = English()`: loads vanilla english text analyser
- `nlp = spaacy.load("en")`: loads lemmatization english analyser. Pipeline has `tagger, parser, ner` which can be disabled. When all disabled `tokenizer` remains by default.
- `tokenizer`: tokenizes/splits words.
- `tagger`: predict part of speech, POS-tagging.
- `parser`: extracts dependencies between words.
- `ner`: recognizes named entities, "Named Entity Recognition".

```py
tweets = []
nlp = spacy.load("en")
for tw in tweets:
  doc = nlp(tw)
  # lemmas & tags
  for token in doc:
    lemma = token.lemma_
    lemma_hash = token.lemma
    tag = token.tag_
    tag_description = spacy.explain(tag)
  # parser
  html = spacy.displacy.render(doc, style="dep") # display relations
  display(HTML(html))
  # ner
  for ent in doc.ents:
    entity_text = ent.text
    entity_label = ent.label_
    entity_decription = spacy.explain(entity_label)

nlp_all = spacy.load("en")
nlp_tokenizer = spacy.load("en", disable=["parser", "tagger", "ner"]) # none
nlp_tagger = spacy.load("en", disable=["parser", "ner"])
nlp_parser = spacy.load("en", disable=["tagger", "ner"])
nlp_ner = spacy.load("en", disable=["parser", "tagger"])
```

## Day 02 - TF-IDF

### Python

```py
u = set()
a = [1, 2, 3, 1]
u |= set(a)  # u.update(a)
```

You can have: `defaultdict(Counter)`

```py
# populate a dictionary using comprehension
term_idf = {
    term: log(num_documents / term_count)
    for term, term_count in term_counter.items()
}
```

### spacy

- spacy data objects, illustration from 01 notebook, Ex 01:
```py
for tw in tqdm(tweets[:2]):
  doc = nlp_none(tw['text'])
  print(type(doc))  #>>> <class 'spacy.tokens.doc.Doc'>
  print(type(doc[0]), doc[0])  #>>> <class 'spacy.tokens.token.Token'> RT
  print(type(doc[0].text), doc[0].text)  #>>> <class 'str'> RT
  tokens = [token.text for token in doc]
  print(tokens[:2])  #>>> <class 'list'> ['RT', '@FLOTUS']
  tweet_len.append(len(tokens))
  uniq_tokens |= set(tokens)

'''
`doc` is an annotated document with a lot of information.
You want to be specific in getting info you need and have methods for the same. Use them like here you extract `token.text` from token that's in the doc.
'''
```

### sklearn TF-IDF

```py

vectorizer = TfidfVectorizer(smooth_idf=False)  # sklearn TF-IDF vecotrizer without `+ 1` added to the formula.

# the order of terms stored always remains constant for the trained vectorizer.
# non-zero vectors are always normalized - values between 0-1 - so that we can compute distances.

print(tabulate(vectorizer_internals, headers=["word", "idf", "count"]))
'''
>>> vectorizer.vocabulary_: {'one': 0, 'two': 2, 'three': 1} # by default sorted in ascending
>>> vectorizer.idf_: [2.09861229 1.         1.40546511] # by default sorted in ascending
>>> word        idf    count
>>> ------  -------  -------
>>> one     2.09861        1
>>> two     1.40547        2
>>> three   1              3
'''
```