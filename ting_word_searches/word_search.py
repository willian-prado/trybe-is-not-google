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


def check_word(word, instance, include_content):
    matches = []

    for index in range(len(instance)):
        file = instance.search(index)
        match = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": find_word_occurrence(word, file, include_content),
        }

        if len(match["ocorrencias"]) > 0:
            matches.append(match)

    return matches


def exists_word(word, instance):
    return check_word(word, instance, False)


def search_by_word(word, instance):
    return check_word(word, instance, True)
