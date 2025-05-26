def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(filepath):

    palavras = get_book_text(filepath)
    qnt_letras_unicas = {}
    for letra in palavras:
        if letra.lower() in qnt_letras_unicas:
            qnt_letras_unicas[letra.lower()] += 1
        else:
            qnt_letras_unicas[letra.lower()] = 1

    return qnt_letras_unicas


def lista_sortida(filepath):

    dicionario = get_num_chars(filepath)
    dicionario_sortido = []

    for letra in dicionario:

        if letra.isalpha() == True:
            dicionario_sortido.append( {"Letra": letra, "Quantidade": dicionario[letra]} )

    def sort_key(item):
        return item["Quantidade"]

    dicionario_sortido.sort(key=sort_key, reverse=True)

    return dicionario_sortido
    


def main(book_path):

   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {book_path}...")

   print("----------- Word Count ----------")
   print(f"Found {get_num_words(get_book_text(book_path))} total words")


   print("--------- Character Count -------")
   A = lista_sortida(book_path)
   for x in range(len(A)):
       print(f" {A[x]["Letra"]}: {A[x]["Quantidade"]}")

   print("============= END ===============")

   return True