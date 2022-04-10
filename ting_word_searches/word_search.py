def find_word_occurrence(word, file, include_content):
    occurrences = []

    for line, content in enumerate(file["linhas_do_arquivo"]):
        if word.lower() in content.lower():
            if include_content:
                occurrences.append({
                    "linha": line+1,
                    "conteudo": content})
            else:
                occurrences.append({"linha": line+1})
    return occurrences


def exists_word(word, instance):
    """Aqui irá sua implementação"""


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
