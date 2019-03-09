class Tokenizer:
    DELIMITER = ' '

    def __init__(self, inp: str):
        self.tokens = inp.split(self.DELIMITER)
        self.last_tmpl = ''

    def match(self, tmpl: str) -> bool:
        self.last_tmpl = tmpl
        items = tmpl.split(self.DELIMITER)
        if len(self.tokens) < len(items):
            return False
        items = self._non_variables(tmpl)
        return items == self.tokens[:len(items)]

    def _non_variables(self, items_str: str) -> list:
        """
        Gets target string without variables attached.
        Example:
        '!test start <name>' becomes '[!test, start]'
        """
        items = items_str.split(self.DELIMITER)
        items = [i for i in items if len(i) > 0]
        items = ['' if i.startswith('<') else i for i in items]
        items = self._remove_last_blanks(items)
        return items

    def _remove_last_blanks(self, items: list) -> str:
        """
        Not going to lie, I don't know why this is here
        """
        for i, item in enumerate(items[::-1]):
            if item != '':
                return items[::-1][i:][::-1]

    def items(self) -> dict:
        template = self.last_tmpl.split(self.DELIMITER)
        non_vars = self._non_variables(self.last_tmpl)

        var = template[len(non_vars):]
        var = [i[1:len(i) - 1] for i in var]
        args = self.tokens[len(non_vars):]
        # Case when last argument should be combined
        if len(args) > len(var):
            n = len(args) - len(var)
            last_msg = args[len(args) - n - 1:]
            last_msg = [' '.join(last_msg)]
            args = args[:len(args) - n - 1] + last_msg
        return {n: a for n, a in zip(var, args)}
