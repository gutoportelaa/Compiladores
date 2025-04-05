


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consumir(self, tipo_esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == tipo_esperado:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Esperado {tipo_esperado}, mas veio {self.tokens[self.pos]}")

    def parse_ocorrencias(self):
        ocorrencias = []
        while self.pos < len(self.tokens):
            try:
                ocorrencias.append(self.parse_registro())
            except SyntaxError as e:
                print(f"Erro de sintaxe: {e}")
                break
        return ocorrencias

    def parse_registro(self):
        self.consumir('TIPO')
        natureza = self.consumir('NATUREZA')[1]

        self.consumir('DATA')
        data_hora = self.consumir('DATA_HORA')[1]

        self.consumir('LOCAL')
        local = self.parse_texto_livre()

        self.consumir('RELATO')
        relato = self.parse_texto_livre()

        self.consumir('ENVOLVIDOS')
        envolvidos = self.parse_texto_livre()

        self.consumir('OBJETOS')
        objetos = self.parse_texto_livre()

        return {
            'natureza': natureza,
            'data_hora': data_hora,
            'local': local,
            'relato': relato,
            'envolvidos': envolvidos,
            'objetos': objetos
        }

    def parse_texto_livre(self):
        palavras = []
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'TEXTO':
            palavras.append(self.tokens[self.pos][1])
            self.pos += 1
        return ' '.join(palavras)


