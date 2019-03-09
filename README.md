# Tokenizer for text messages

## Setup

`pip3 install -U chatbottokenizer`

## Usage

```py
from chatbottokenizer import Tokenizer

INPUT_STRING = '!bot create george'
tokens = Tokenizer('!bot', INPUT_STRING)
if tokens.match('create <name>'):
  items = tokens.items()
  print('Name is: {}'.format(items['name']))
```

Note: `.items()` must be called after a `.match()`
