# M11 - Text Mining, by Sergey Khoroshenkikh

## Day 01

### Python refresher

- `pprint()` : pretty print, needs to be imported: `from pprint import pprint`
- `defaultdict()` provides default value to a key and doesn't raise `KeyError`.

```py
from collections import defaultdict
dict = defaultdict(int)  # default value 0
```
- `Counter()` powerful container to count things.

```py
from collections import Counter
c = Counter()
print(c.most_common()[:3]) # top 3
```

- `re` find things, regex

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
