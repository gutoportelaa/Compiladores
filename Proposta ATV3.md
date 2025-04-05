# Linguagem Natural Controlada (LNC): Segurança Pública

ocorrências: <um ou mais registro>
registro: ‘tipo:’ natureza ‘data:’ data_hora ‘local:’ local ‘relato:’ descrição ‘envolvidos:’
envolvidos ‘objetos:’ objetos
natureza: furto | roubo | perda | ameaça | acidente | estelionato
data_hora: <data qualquer no formato: dd/mm/aa, incluindo ou não o horário no formato:
hh:mm>
local: <breve descrição do local, formada por uma sequência de palavras>
descrição: <breve descrição da ocorrência, formada por uma sequência de palavras>
envolvidos: <um ou mais envolvidos, incluindo vítimas e suspeitos>
objetos: <descrição de um ou mais objetos envolvidos na ocorrência, por exemplo,
celular, computador, veículo, tv, mochila, ou outros objetos>

# 1) Criar um parser descendente recursivo (feito manualmente) para a LNC descrita. Mais
# de um registro de ocorrência pode ser descrito no mesmo arquivo. Porém, o formato dos
# registros deve ser devidamente reconhecido pelo parser.

# 2) Criar manualmente o analisador léxico para reconhecer os tokens usados nas
# descrições, incluindo palavras acentuadas.
