class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consumir(self, tipo_esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == tipo_esperado:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        raise SyntaxError(f"Esperado {tipo_esperado}, mas veio {self.tokens[self.pos]}")

    def parse_ocorrencias(self):
        ocorrencias = []
        while self.pos < len(self.tokens):
            ocorrencias.append(self.parse_registro())
        return ocorrencias

    def parse_registro(self):
        self.consumir('TIPO')
        natureza = self.consumir('NATUREZA')[1]

        self.consumir('DATA')
        data_hora = self.consumir('DATA_HORA')[1]

        self.consumir('LOCAL')
        local = self.consumir('TEXTO')[1]

        self.consumir('RELATO')
        relato = self.consumir('TEXTO')[1]

        self.consumir('ENVOLVIDOS')
        envolvidos = self.consumir('TEXTO')[1].split(',')

        self.consumir('OBJETOS')
        objetos = self.consumir('TEXTO')[1].split(',')

        return {
            "natureza": natureza,
            "data_hora": data_hora,
            "local": local,
            "relato": relato,
            "envolvidos": [e.strip() for e in envolvidos],
            "objetos": [o.strip() for o in objetos]
        }
