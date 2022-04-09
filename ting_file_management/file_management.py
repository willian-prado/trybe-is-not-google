from os.path import exists
import sys


def txt_importer(path_file):
    if exists(path_file):
        if not path_file.endswith('txt'):
            print("Formato inválido", file=sys.stderr)

        with open(path_file) as file:
            content = file.read()
            return content.split('\n')
    else:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
