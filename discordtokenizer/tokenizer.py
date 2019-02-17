class Tokenizer:
    def __init__(self, inp: str):
        self.tokens = inp.split(' ')
        self.last = ''

    def match(self, tmpl: str) -> bool:
        self.last = tmpl
        items = tmpl.split(' ')
        if len(self.tokens) < len(items):
            return False
        items = self._get_const(tmpl)
        return items == self.tokens[:len(items)]

    def _get_const(self, items_str: str) -> list:
        items = items_str.split(' ')
        items = [item for item in items if len(item) > 0]
        items = ['' if i.startswith('<') else i for i in items]
        items = self._last_blank(items)
        return items

    def _last_blank(self, items: list) -> str:
        for i, item in enumerate(items[::-1]):
            if item != '':
                return items[::-1][i:][::-1]

    def items(self) -> dict:
        template = self.last.split(' ')
        const_template = self._get_const(self.last)

        names = template[len(const_template):]
        names = [i[1:len(i) - 1] for i in names]
        args = self.tokens[len(const_template):]
        return {n: a for n, a in zip(names, args)}
