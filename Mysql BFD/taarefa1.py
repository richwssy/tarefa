import mysql.connector


class SistemaProdutoria:
    def __init__(self):
        self.config_db = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'admin',
            'database': 'Produtoria'
        }

    def conectar(self):
        try:
            return mysql.connector.connect(**self.config_db)
        except mysql.connector.Error as err:
            print(f"Erro ao conectar: {err}")
            return None

    def cadastrar(self):
        print("\nCADASTRO DE PROFESSOR")
        try:
            id_prof = int(input("Digite o ID (número inteiro): "))
            matricula = input("Digite a Matrícula: ")
            nome = input("Digite o Nome: ")
            disciplina = input("Digite a Disciplina: ")

            conexao = self.conectar()
            if conexao:
                cursor = conexao.cursor()
                sql = "INSERT INTO professores (id, Matricula, Nome, Disciplina) VALUES (%s, %s, %s, %s)"
                valores = (id_prof, matricula, nome, disciplina)

                cursor.execute(sql, valores)
                conexao.commit()
                print("Professor cadastrado com sucesso!")

                cursor.close()
                conexao.close()
        except ValueError:
            print("O ID deve ser um número inteiro.")
        except mysql.connector.Error as err:
            print(f"Erro ao cadastrar no banco: {err}")

    def deletar(self):
        print("\nDELETAR PROFESSOR")
        matricula = input(
            "Digite a MATRÍCULA do professor que deseja deletar: ")

        conexao = self.conectar()
        if conexao:
            cursor = conexao.cursor()
            sql = "DELETE FROM professores WHERE Matricula = %s"
            cursor.execute(sql, (matricula,))
            conexao.commit()

            if cursor.rowcount > 0:
                print(f"Professor com matrícula {matricula} deletado.")
            else:
                print("Nenhum professor encontrado com essa matrícula.")

            cursor.close()
            conexao.close()

    def listar_tudo(self):
        print("\nLISTA DE TODOS OS PROFESSORES")
        conexao = self.conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM professores")
            resultados = cursor.fetchall()

            if resultados:
                print(
                    f"{'ID':<5} | {'Matrícula':<15} | {'Nome':<20} | {'Disciplina'}")
                print("-" * 60)
                for linha in resultados:
                    print(
                        f"{linha[0]:<5} | {linha[1]:<15} | {linha[2]:<20} | {linha[3]}")
            else:
                print("Nenhum registro encontrado.")

            cursor.close()
            conexao.close()

    def listar_especifico(self):
        print("\nBUSCAR PROFESSOR ESPECÍFICO")
        matricula = input("Digite a MATRÍCULA para busca: ")

        conexao = self.conectar()
        if conexao:
            cursor = conexao.cursor()
            sql = "SELECT * FROM professores WHERE Matricula = %s"
            cursor.execute(sql, (matricula,))
            resultado = cursor.fetchone()

            if resultado:
                print("\nProfessor Encontrado:")
                print(f"ID: {resultado[0]}")
                print(f"Matrícula: {resultado[1]}")
                print(f"Nome: {resultado[2]}")
                print(f"Disciplina: {resultado[3]}")
            else:
                print("Professor não encontrado.")

            cursor.close()
            conexao.close()


if __name__ == "__main__":
    sistema = SistemaProdutoria()

    while True:
        print("\n1. Cadastrar Professor")
        print("2. Listar Tudo")
        print("3. Listar Específico (por Matrícula)")
        print("4. Deletar (por Matrícula)")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sistema.cadastrar()
        elif opcao == '2':
            sistema.listar_tudo()
        elif opcao == '3':
            sistema.listar_especifico()
        elif opcao == '4':
            sistema.deletar()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")
