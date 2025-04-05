from analexico import tokenize
from pprint import pprint

def main():
    with open("exemplos/exemplo1.txt", "r", encoding="utf-8") as f:
        entrada = f.read()

    tokens = tokenize(entrada)
    pprint(ocorrencias)

if __name__ == "__main__":
    main()