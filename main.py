from analexico import tokenizar
from parser import Parser
from pprint import pprint

def main():
    nome_arquivo_txt = "ocorrencias.txt"
    with open(nome_arquivo_txt, "r", encoding="utf-8") as f:
        entrada = f.read()


    tokens = tokenizar(entrada)
    parser = Parser(tokens)
    try:
        ocorrencias = parser.parse_ocorrencias()
        print(" Análise sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f" Erro de sintaxe: {e}")

    pprint(ocorrencias)

if __name__ == "__main__":
    main()