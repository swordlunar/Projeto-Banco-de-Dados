# -*- coding: utf-8 -*-
import psycopg2
import datetime


def create_tables():
    try:
        commands = (
            """
            CREATE TABLE paciente (
                id_pac SERIAL PRIMARY KEY UNIQUE,
                nome_pac VARCHAR(255) NOT NULL,
                sexo_pac CHAR NOT NULL,
                tipo_sag VARCHAR(2) NOT NULL,
                cpf_pac VARCHAR(10) NOT NULL,
                rg_pac VARCHAR(10) NULL,
                end_log_pac VARCHAR(255) NOT NULL,
                end_num_pac INTEGER NOT NULL,
                end_bairro_pac VARCHAR(255) NOT NULL,
                end_cidade_pac VARCHAR(255) NOT NULL,
                end_cep_pac VARCHAR(11) NOT NULL,
                end_uf_pac VARCHAR(2) NOT NULL,
                end_comp_pac VARCHAR,
                tel1_pac VARCHAR(15) NOT NULL,
                tel2_pac VARCHAR(15),
                email_pac VARCHAR(100) NOT NULL,
                boletim VARCHAR NOT NULL,
                presc VARCHAR(255) NOT NULL,
                fixas_ane VARCHAR NOT NULL,
                desc_cir VARCHAR NOT NULL,
                observacao VARCHAR NOT NULL,
                proce VARCHAR NOT NULL,
                pront SERIAL NOT NULL UNIQUE,
                ult_con INTEGER UNIQUE                                                     
            );
            """,
            """
            CREATE TABLE consulta (
                id_con SERIAL PRIMARY KEY UNIQUE,
                id_pac INTEGER UNIQUE,
                id_fun INTEGER UNIQUE,
                data_con TIMESTAMP NOT NULL,                
                sint VARCHAR NOT NULL,
                diag VARCHAR NOT NULL
            );
            """,
            """
            CREATE TABLE internacao (
                id_int SERIAL PRIMARY KEY UNIQUE,
                data_int TIMESTAMP NOT NULL,              
                dias_perm INTEGER NOT NULL,
                num_lei INTEGER NOT NULL,
                id_con INTEGER NOT NULL UNIQUE,
                tratamento VARCHAR NOT NULL,
                diag_ini VARCHAR NOT NULL,
                diag_fin VARCHAR NOT NULL
            );
            """,
            """
            CREATE TABLE agenda (
                id_con INTEGER UNIQUE,
                id_fun INTEGER UNIQUE,
                cpf_fun VARCHAR(10) UNIQUE 
            );
            """,
            """
            CREATE TABLE funcionario (
                id_fun SERIAL PRIMARY KEY UNIQUE,
                cpf_fun VARCHAR(10) NOT NULL UNIQUE,
                rg_fun VARCHAR(10) NOT NULL,
                crm INTEGER,
                cargo VARCHAR(15), 
                cofen INTEGER,
                nome_fun VARCHAR NOT NULL,
                hora_plant INTEGER NOT NULL,
                end_log_fun VARCHAR(255) NOT NULL,
                end_num_fun INTEGER NOT NULL,
                end_bairro_fun VARCHAR(255) NOT NULL,
                end_cidade_fun VARCHAR(255) NOT NULL,
                end_cep_fun VARCHAR(11) NOT NULL,
                end_uf_fun VARCHAR(2) NOT NULL,
                end_comp VARCHAR,
                tel1_fun VARCHAR(15) NOT NULL,
                tel2_fun VARCHAR(15)
            );
            """,
            """
            CREATE TABLE cadastro (
                id_pac INTEGER UNIQUE,
                pront INTEGER UNIQUE,
                cpf_fun VARCHAR(10) UNIQUE,
                id_fun INTEGER UNIQUE
            );
            """,
            """
            ALTER TABLE paciente ADD
            FOREIGN KEY (ult_con) REFERENCES
            consulta (id_con) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE consulta ADD
            FOREIGN KEY (id_fun) REFERENCES
            funcionario (id_fun) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE consulta ADD
            FOREIGN KEY (id_pac) REFERENCES
            paciente (id_pac) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE internacao ADD
            FOREIGN KEY (id_con) REFERENCES
            consulta (id_con) ON DELETE SET NULL ON UPDATE CASCADE
            """
            ,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (pront) REFERENCES
            paciente (pront) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (id_pac) REFERENCES
            paciente (id_pac) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (id_fun) REFERENCES
            funcionario (id_fun) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (cpf_fun) REFERENCES
            funcionario (cpf_fun) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE agenda ADD
            FOREIGN KEY (id_fun) REFERENCES
            funcionario (id_fun) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE agenda ADD
            FOREIGN KEY (cpf_fun) REFERENCES
            funcionario (cpf_fun) ON DELETE SET NULL ON UPDATE CASCADE
            """,
            """
            ALTER TABLE agenda ADD
            FOREIGN KEY (id_con) REFERENCES
            consulta (id_con) ON DELETE SET NULL ON UPDATE CASCADE
            """
        )

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        for c in commands:
            cur.execute(c)
        cur.close()
        con.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def exibir_funcionario(pessoas):
    for pessoa in pessoas:
        print("=================================")
        print("Nome: " +pessoa[6])
        print("Cargo: " + pessoa[4])
        print("CPF: " + str(pessoa[1]))
        print("RG: " + str(pessoa[2]))
        if (pessoa[4] == "médico"):
            print("CRM: " + str(pessoa[3]))
        if (pessoa[4] == "enfermeiro"):
            print("COFEN: " + str(pessoa[5]))
        print("Horas de plantão: " + str(pessoa[7]) + " HR")
        print("Endereço: " + pessoa[8] + ", N " + str(pessoa[9]) + ", bairro " + pessoa[10])
        print("Cidade: " + pessoa[11] + ", UF: " + pessoa[13])
        print("Telefone: " + str(pessoa[15]))
        print("=================================\n")


def exibir_paciente(pessoas):
    for pessoa in pessoas:
        print("=================================")
        print("Nome: " + pessoa[1])
        print("CPF: " + str(pessoa[4]))
        print("RG: " + str(pessoa[5]))
        print("Sexo: " + pessoa[2])
        print("Boletim: " + pessoa[16])
        print("Prescrições: " + pessoa[17])
        print("Fixas anestésicas: " + pessoa[18])
        print("Descriçoẽs cirurgicas: " + pessoa[19])
        print("Observação: " + pessoa[20])
        print("Procedimento: " + pessoa[21])
        print("Prontuaŕio: " + str(pessoa[22]))
        print("Email: " + pessoa[15])
        print("Telefone: " + str(pessoa[13]))
        print("Endereço: " + pessoa[6] + ", N " + str(pessoa[7]) + ", bairro " + pessoa[8])
        print("Cidade: " + pessoa[9] + ", UF: " + pessoa[10])
        print("Telefone: " + str(pessoa[15]))
        print("=================================\n")


def exibir_relatorio(dados):
    for dado in dados:
        print("ID do Funcionário: " +str(dado[0]),"Nome do Funcionário: "+str(dado[1]),"ID do Paciente: " +str(dado[2]),"Nome do Paciente:" +str(dado[3]))


def cadastrar_funcionario():
    print("Escolha o cargo:\n1- Médico\n2- Enfermeiro\n3- Secretário")
    opcao = input()
    if opcao is "1":
        cargo = "médico"
    elif opcao is "2":
        cargo = "enfermeiro"
    else:
        cargo = "secretário"
    crm = cofen = None

    nome = input("Digite o nome: ")
    rg = input("Digite o rg: ")
    cpf = input("Digite o cpf: ")
    tel1 = input("Digite o telefone: ")
    tel2 = input("Digite outro telefone (opcional): ")
    if cargo is "médico":
        crm = input("Digite o CRM (médico): ")
    if cargo is "enfermeiro":
        cofen = input("Digite o COFEN (enfermeiro): ")
    horasplatao = input("Digite tempo de plantão: ")
    logradouro = input("Digite a rua: ")
    bairro = input("Digite o bairro: ")
    numero = input("Digite o numero: ")
    cidade = input("Digite a cidade: ")
    cep = input("Digite o cep: ")
    uf = input("Digite o estado: ")
    complemento = input("Digite o complemento (opcional): ")

    if tel2 is "":
        tel2 = None
    if complemento is "":
        complemento = None

    try:

        comand = """
                INSERT INTO funcionario (cpf_fun, rg_fun, crm, cargo, cofen,
                    nome_fun, hora_plant, end_log_fun, end_num_fun,
                    end_bairro_fun, end_cidade_fun, end_cep_fun, end_uf_fun,
                    end_comp, tel1_fun, tel2_fun) VALUES (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);                
                """

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        cur.execute(comand, (cpf, rg, crm, cargo, cofen, nome, horasplatao, logradouro, numero,
                             bairro, cidade, cep, uf, complemento, tel1, tel2,))
        con.commit()
        print("\n#Funcionário cadastrado com sucesso!\n")
        menu()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def cadastrar_paciente():
    nome = input("Digite o nome: ")
    rg = input("Digite o rg: ")
    cpf = input("Digite o cpf: ")
    sexo = input("Digite o sexo: ")
    tel1 = input("Digite o telefone: ")
    tel2 = input("Digite outro telefone (opcional): ")
    email = input("Digite o email: ")
    tipo_sanquineo = input("Digite o tipo sanquíneo do paciente: ")
    descricoes_cirurgicas = input("Digite as descrições cirurgicas do paciente: ")
    observacoes = input("Digite as observações: ")
    prescricoes_medicas = input("Digite as prescrições médicas: ")
    fichas_anestesicas = input("Digite as fichas anestésicas: ")
    boletim_medico = input("Digite o boletim médico do paciente: ")
    procedimentos = input ("Digite os procedimentos a serem realizados no paciente: ")
    logradouro = input("Digite o logradouro: ")
    bairro = input("Digite o bairro: ")
    numero = input("Digite o numero: ")
    cidade = input("Digite a cidade: ")
    cep = input("Digite o cep: ")
    uf = input("Digite o estado: ")
    complemeto = input("Digite o complemento (opcional): ")

    try:
        comand = """
            INSERT INTO paciente (nome_pac, sexo_pac,tipo_sag, cpf_pac,
                rg_pac, end_log_pac, end_num_pac, end_bairro_pac,
                end_cidade_pac, end_cep_pac, end_uf_pac, end_comp_pac, tel1_pac, tel2_pac, email_pac,
                boletim, presc, fixas_ane, desc_cir, observacao, proce) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        cur.execute(comand, ((nome,), (sexo,), (tipo_sanquineo,), (cpf,), (rg,), (logradouro,), (numero,), (bairro,), (cidade,),
                         (cep,), (uf,),(complemeto,),(tel1,), (tel2,), (email,), (boletim_medico,), (prescricoes_medicas,),(fichas_anestesicas,),(descricoes_cirurgicas,),(observacoes,),(procedimentos,),))
        con.commit()
        print("\n#Paciente cadastrado com sucesso!\n")
        menu()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def exibir_internados(internado):
    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="1234")
    cur = con.cursor()
    comando = """SELECT nome_pac FROM paciente WHERE id_pac = (SELECT id_pac FROM consulta WHERE id_con = (%s))"""
    print("=================================")
    cur.execute(comando, (internado[0][4],))
    print("Internado: " + str(cur.fetchone()[0]))
    print("Data de entrada: " + str(internado[0][1]))
    print("Dias para saída: " + str(internado[0][2]))
    print("Leito: " + str(internado[0][3]))
    print("Tratamento: " + internado[0][5])
    print("Diagnostico inicial: " + internado[0][6])
    print("Diagnostico final: " + internado[0][7])
    print("=================================\n")        


def exibir_consultas(consultas):
    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="1234")
    cur = con.cursor()
    comando_pac = """SELECT nome_pac FROM paciente WHERE id_pac = (%s)"""
    comando_fun = """SELECT nome_fuc FROM funcionario WHERE id_fun = (%s)"""

    for consulta in consultas:
        print("=================================")
        print("Código da consulta: " + str(consulta[0]))
        cur.execute(comando_pac, (consulta[1],))
        print("Nome do paciênte: " + str(cur.fetchone()[0]))
        cur.execute(comando_fun, (consulta[2],))
        print("Médico: " + str(cur.fetchone()[0]))
        print("Data: " + str(consulta[3]))
        print("Sintomas: " + consulta[4])
        print("Diagnostico: " + consulta[5])
        print("=================================\n")


def encontrar_funcionario():
    try:
        print("Você deseja buscar por:\n1- Nome\n2- CPF\n3- Cargo\n")
        opcao = input()
        if opcao is "1":
            valor = input("Digite o nome: ")
            comand = """SELECT * FROM funcionario WHERE nome_fun = (%s)"""
        elif opcao is "2":
            valor = input("Digite o cpf: ")
            comand = """SELECT * FROM funcionario WHERE cpf_fun = (%s)"""
        else:
            print("1- Médico\n2- Enfermeiro\n3- Secretário")
            opcao_cargo = input()
            if opcao_cargo is "1":
                comand = """SELECT * FROM funcionario WHERE cargo = 'médico'"""
            elif opcao_cargo is "2":
                comand = """SELECT * FROM funcionario WHERE cargo = 'enfermeiro'"""
            else:
                comand = """SELECT * FROM funcionario WHERE cargo = 'secretário'"""

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        cur.execute(comand, (valor,))
        r = cur.fetchall()
        cur.close()
        if len(r)==0:
            print("\n#Funcionário não encontrado!\n")
            menu()
        else:
            exibir_funcionario(r)
            menu()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def encontrar_paciente():
    try:
        print("Você deseja buscar por:\n1- Nome\n2- CPF\n")
        opcao = input()
        if opcao is "1":
            valor = input("Digite o nome: ")
            comand = """SELECT * FROM paciente WHERE nome_pac = (%s)"""
        else:
            valor = input("Digite o cpf: ")
            comand = """SELECT * FROM paciente WHERE cpf_pac = (%s)"""

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        cur.execute(comand, (valor,))
        r = cur.fetchall()
        cur.close()
        if len(r)==0:
            print("\n#Paciente não encontrado!\n")
            menu()
        else:
            exibir_paciente(r)
            menu()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def encontrar_consulta():
    try:
        valor = input("Digite o CPF do paciênte: ")
        comand = """SELECT * FROM consulta WHERE id_pac = (SELECT id_pac FROM paciente WHERE cpf_pac = (%s))"""
        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="1234")
        cur = con.cursor()
        cur.execute(comand, (valor,))
        r = cur.fetchall()
        cur.close()
        exibir_consultas(r)
        menu()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def encontrar_internacao():
    try:
        valor = input("Digite o CPF do paciênte: ")
        comand = """SELECT * FROM internacao WHERE id_con = (SELECT id_con FROM consulta WHERE 
                    id_pac = (SELECT id_pac FROM paciente WHERE cpf_pac = (%s)))"""
        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="1234")
        cur = con.cursor()
        cur.execute(comand, (valor,))
        r = cur.fetchall()
        cur.close()
        exibir_internados(r)
        menu()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def cadastrar_consulta():
    id_paciente = input("Digite o ID do paciente: ")
    id_funcionario = input("Digite o seu ID: ")
    sintomas = input("Digite os sintomas do paciente: ")
    diagnostico = input("Digite o diagnostico do paciente: ")

    comand = """
            INSERT INTO consulta (id_pac, id_fun, data_con, sint, diag) VALUES
            (%s, %s, %s, %s, %s)

            """

    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
    cur = con.cursor()
    cur.execute(comand,
                ((id_paciente,), (id_funcionario,), (datetime.datetime.now()), (sintomas,), (diagnostico,),))
    con.commit()
	menu()


def cadastrar_internacao():
    num_leito = input("Digite o número do leito: ")
    id_consulta = input("Digite o ID da cosulta: ")
    dias_perm = input("Digite os dias que ele permanecerá: ")
    diagnostico_ini = input("Digite o diagnostico inicial do paciente: ")
    diagnostico_fin = input("Digite o diagnostico final do paciente: ")
    tratamento = input("Digite o tratamento no qual o paciente será submetido: ")


    comand = """
            INSERT INTO internacao (data_int,num_lei, id_con, dias_perm, diag_ini, diag_fin, tratamento) VALUES
            (%s, %s, %s, %s, %s, %s , %s)

            """

    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
    cur = con.cursor()
    cur.execute(comand,
                ((datetime.datetime.now(),),(num_leito,),(id_consulta,),(dias_perm,),(diagnostico_ini,),(diagnostico_fin,),(tratamento,),))
    con.commit()

def consultar_funcionarioXpaciente():
    comand = """ 
            SELECT f.id_fun ,nome_fun, p.id_pac,nome_pac
            FROM funcionario f ,paciente p ,consulta c
            WHERE f.id_fun = c.id_fun and p.id_pac = c.id_pac
    """
    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
    cur = con.cursor()
    cur.execute(comand)
    r = cur.fetchall()
    cur.close()
    exibir_relatorio(r)

    con.commit()


def deletar_funcionario():
    cpf = input ("Digite o CPF do funcionário que você deseja deletar: ")

    comand = """
            DELETE  FROM funcionario WHERE cpf_fun = (%s)
        """

    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
    cur = con.cursor()
    cur.execute(comand,
                ((cpf),))
    con.commit()
    print("O funcionário de cpf "+str(cpf)+"foi deletado com sucesso!\n")
    menu()

def atualizar_funcionario():
    cpf = input("Digite o cpf do funcionário: ")
    comand = """
            SELECT * FROM funcionario WHERE cpf_fun = (%s)
        """
    con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
    cur = con.cursor()
    cur.execute(comand,
                ((cpf),))
    r=cur.fetchone()
    cur.close()
    exibir_funcionario(r)

    valor = input("Deseja atualizar este funcionário (S/N)? ")
    if valor is "S":
        nome = input ("Digite um novo nome para o funcionário: ")
        comand = """
                    UPDATE funcionario
                    SET nome_fun = (%s)
                    WHERE nome_fun = (%s)
                    """
        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        cur.execute(comand,
                    ((nome),(r[6]),))
        con.commit()
    else:
        menu()


def menu():
    print("Você deseja:\n1 - Cadastrar paciênte\n2 - Cadastrar funcionário\n3 - Buscar funcionário\n"
          "4 - Buscar paciênte\n5 - Deletar Funcionário\n6- Sair")
    opcao = input()
    if opcao is "1":
        cadastrar_paciente()
    elif opcao is "2":
        cadastrar_funcionario()
    elif opcao is "3":
        encontrar_funcionario()
    elif opcao is "4":
        encontrar_paciente()
    elif opcao is "5":
        deletar_funcionario()
    else:
        print("============================")


if __name__ == "__main__":
    #create_tables()
    #cadastrar_funcionario()
    # encontrar_funcionario()
    #menu()
    #cadastrar_consulta()
    #consultar_funcionarioXpaciente()
    atualizar_funcionario()
