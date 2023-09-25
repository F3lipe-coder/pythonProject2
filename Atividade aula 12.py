def produto(descricao, tipo, quantidade):
    descricao = descricao.strip()
    tipo=tipo.strip()
    quantidade = quantidade.strip()
    if quantidade.isdigit():
        return {"descricao":descricao,"tipo":tipo,"quantidade":int(quantidade)}
    else:
        print("O valor da quantidade não é valido")


produtos = list()

while True:
    descricao = input("Digite a descrição do produto: ")
    tipo = input("Digite o tipo do produto: ")
    quantidade = input("Digite a quantidade do produto: ")
    if isinstance(produto(descricao=descricao,tipo=tipo,quantidade=quantidade),dict):
        produtos.append(produto(descricao=descricao,tipo=tipo,quantidade=quantidade))
    else:
        print("Não foi possivel cadastrar")

    resp=input("Deseja sair sim ou não").strip()[0].upper()

    if resp == "S":
        break

print(produtos)
