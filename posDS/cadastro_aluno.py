resp = input("Deseja cadastrar algum estudante? (S)(N): ")

while resp == "S" or resp == "s":

    nome = input("Digite o nome do estudante: ")
    alunoEmail = input("Digite o email do estudante: ")
    alunoCPF = input("Digite o CPF do estudante: ")
    alunoMatricula = input("Digite a mátricula do estudante: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media < 6:
        nota4 = float(input("Nota ainda não alcançada. Insira uma 4ª nota: "))

        media = (nota1 + nota2 + nota3 + nota4) / 4

        if media < 6:
            print("Média insuficiente! Estudante reprovado.")

    else:
        print(f"Estudante {nome}, parabéns pela aprovação!")
        print(
            f"""Em seu diploma constarão os seguintes dados:\n Nome: {nome}\n Email: {alunoEmail}\n CPF: {alunoCPF}\n Matrícula: {alunoMatricula}."""
        )

    resp = input("Deseja cadastrar mais algum estudante? (S)(N): ")
