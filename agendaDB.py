# Você consegue!

import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    try:
        conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            db='agenda',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            yield conexao
        finally:
            conexao.close()
    except TypeError as err:
        print(f"Error: {err}")



def inserir_contato():
    try:
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'INSERT INTO agenda (nome, email, telefone, logradouro, cidade, estado)VALUES (%s, %s, %s, %s, %s, %s)'
                nome = input('Nome: ')
                email = input('Email: ')
                telefone = input('Telefone: ')
                logradouro = input('Logradouro: ')
                cidade = input('Cidade: ')
                estado = input('Estado: ')

                cursor.execute(sql, (nome, email, telefone, logradouro, cidade, estado))
                conexao.commit()
    except TypeError as err:
        print(f"Error: {err}")


def listar_contatos():
    try:
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'SELECT * FROM agenda'
                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    print(linha)
    except TypeError as err:
            print(f"Error: {err}")


def pesquisar_por_id():
    try:
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'SELECT * FROM agenda WHERE id=%s'
                identificador = input('Id: ')
                cursor.execute(sql, (identificador,))
                resultado = cursor.fetchall()

                for linha in resultado:
                    print(linha)
    except TypeError as err:
        print(f"Error: {err}")


def pesquisar_por_nome():
    try:
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'SELECT * FROM agenda WHERE nome=%s'
                nome = input('Nome: ')
                cursor.execute(sql, (nome,))
                resultado = cursor.fetchall()

                for linha in resultado:
                    print(linha)
    except TypeError as err:
        print(f"Error: {err}")


def deletar_contato():
    try:
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'DELETE FROM agenda WHERE id=%s'
                identificador = input('Id: ')
                cursor.execute(sql, (identificador,))
                conexao.commit()
    except TypeError as err:
        print(f"Error: {err}")



def atualizar_contato():
    try:
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE agenda SET (%s) WHERE id=%s'
                coluna = input('coluna: ')
                identificador = input('id: ')
                cursor.execute(sql, (coluna, identificador))
                conexao.commit()
    except TypeError as err:
        print(f"Error: {err}")



def menu():
    try:
        print('\n------ Agenda de contatos ------\n')
        print('1. Novo contato')
        print('2. Listar contatos')
        print('3. Pesquisar contato por nome')
        print('4. Pesquisar contato por id')
        print('5. Excluir contato')
        print('6. Atualizar contato')
        print('7. Sair')

        opcao = input('Sua opção: ')
        if opcao == '1':
            inserir_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            pesquisar_por_nome()
        elif opcao == '4':
            pesquisar_por_id()
        elif opcao == '5':
            deletar_contato()
        elif opcao == '6':
            atualizar_contato()
        elif opcao == '7':
            exit()
    except TypeError as err:
        print(f"Error: {err}")


if __name__ == '__main__':
    menu()