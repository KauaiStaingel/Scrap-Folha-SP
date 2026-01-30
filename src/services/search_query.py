import urllib.parse


class SearchQueryBuilder:
    def ask(self):
        query = input("Digite o assunto da busca: ").strip()

        if not query:
            raise ValueError("Assunto não pode ser vazio")

        return urllib.parse.quote(query)
