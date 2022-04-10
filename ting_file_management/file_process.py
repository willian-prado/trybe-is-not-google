from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)

    processed_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }

    if not instance.search_by_filename(path_file):
        instance.enqueue(processed_file)
        print(processed_file, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
