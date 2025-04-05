import re

token_rules = [             #tupla de expressões regulares e seus nomes
    ('TIPO', r'tipo:'),
    ('DATA', r'data:'),
    ('LOCAL', r'local:'),
    ('RELATO', r'relato:'),
    ('ENVOLVIDOS', r'envolvidos:'),
    ('OBJETOS', r'objetos:'),
    ('NATUREZA', r'furto|roubo|perda|ameaça|acidente|estelionato'),
    ('DATA_HORA', r'\d{2}/\d{2}/\d{2}( \d{2}:\d{2})?'),
    ('TEXTO', r'[^\n]+'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
]                                   #reparem que não tem OCORRENCIA, REGISTRO ou ENVOLVIDOS. Isso é pq são símbolos não terminais
                                       #logo, não se encaixam como tokens. Eles são gerados na hora de criar a árvore sintática

def tokenizar(texto):
    tokens = []
    pos = 0
    while pos < len(texto):
        match = None
        for token_tipo, pattern in token_rules:
            regulexpress = re.compile(pattern)
            match = regulexpress.match(texto, pos)
            if match:
                if token_tipo != 'SKIP' and token_tipo != 'NEWLINE':
                    tokens.append((token_tipo, match.group(0).strip()))
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Erro léxico próximo de: {texto[pos:]}")
    return tokens 
                    