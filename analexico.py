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
]
