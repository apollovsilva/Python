preco_livro = 24.95

desconto = 0.6

envio_primeiro_livro = 3.00

envio_livros_adicionais = 0.75

total_livro = 60 * preco_livro * desconto

livro_mais_frete = total_livro + envio_primeiro_livro + 59*envio_livros_adicionais

print(livro_mais_frete)
