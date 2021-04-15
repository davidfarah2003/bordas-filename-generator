import itertools

def k(value):
    url = "https://biblio.editions-bordas.fr/epubs/BORDAS/bibliomanuels/ressources/"
    num_complet = "9782047337646"
    num_abbr = "733764"
    nom_livre = "INDICE_Tle_spe"
    additional_ldp = ["livre-du-professeur", "livre-prof"]
    mots_cles = ['integral', 'int', 'INT', 'Integral', 'complet', 'COMPLET']

    if value == "nom_livre":
        return nom_livre
    elif value == "url":
        return url
    elif value == "num":
        return num_complet
    elif value == "num_":
        return num_abbr
    elif value == "ldp+":
        return additional_ldp
    elif value == "mots":
        return mots_cles

def full_iter(word):
    result = list(map(''.join, itertools.product(*zip(word.upper(), word.lower()))))
    return result

def rephrase(possibilities):
    phrase_list = []
    for index, tuplez in enumerate(possibilities):
        element_one = tuplez[0]
        element_two = tuplez[1]
        element_three = tuplez[2]
        phrase = f"{element_one}_{element_two}_{element_three}"
        phrase_list.append(phrase)
    return phrase_list


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l


if __name__ == '__main__':
    ldp_list = full_iter("ldp")
    if k("ldp+"):
        for term in k("ldp+"):
            if term != "":
                ldp_list.append(term)
    print(ldp_list)

    params = [ldp_list, [k("nom_livre")], k("mots")]
    params = permutation(params)
    list_of_l = []
    for param in params:
        possibilities = list(itertools.product(*param))  # finds all combinations of lists
        list_of_names = rephrase(possibilities)
        list_of_l.append(list_of_names)

    final_list = list(itertools.chain.from_iterable(list_of_l))
    print(len(final_list))

    with open("filenames.txt", mode="w") as outfile:
        for phrase in final_list:
            outfile.write("%s\n" % phrase)