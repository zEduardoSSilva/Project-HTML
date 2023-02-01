import webbrowser

"""Faz a Leitura do Arquivo"""

with open("Formulario.html", "r") as arquivo:
    conteudo = arquivo.read()

"""Abre o Arquivo HTML na Web em Outra Aba atravez no 'New=2' !!!"""

arquivo = "Formulario.html"
webbrowser.open(arquivo, new=2)
