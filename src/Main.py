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
                cpf_pac INTEGER NOT NULL,
                rg_pac INTEGER NOT NULL,
                end_log_pac VARCHAR(255) NOT NULL,
                end_num_pac INTEGER NOT NULL,
                end_bairro_pac VARCHAR(255) NOT NULL,
                end_cidade_pac VARCHAR(255) NOT NULL,
                end_cep_pac VARCHAR(11) NOT NULL,
                end_uf_pac VARCHAR(2) NOT NULL,
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
                cpf_fun INTEGER UNIQUE 
            );
            """,
            """
            CREATE TABLE funcionario (
                id_fun SERIAL PRIMARY KEY UNIQUE,
                cpf_fun INTEGER NOT NULL UNIQUE,
                rg_fun INTEGER NOT NULL,
                crm INTEGER,
                cargo VARCHAR(15), 
                cofen INTEGER,
                nome_fuc VARCHAR NOT NULL,
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
                cpf_fun INTEGER UNIQUE,
                id_fun INTEGER UNIQUE
            );
            """,
            """
            ALTER TABLE paciente ADD
            FOREIGN KEY (ult_con) REFERENCES
            consulta (id_con)
            """,
            """
            ALTER TABLE consulta ADD
            FOREIGN KEY (id_fun) REFERENCES
            funcionario (id_fun)
            """,
            """
            ALTER TABLE consulta ADD
            FOREIGN KEY (id_pac) REFERENCES
            paciente (id_pac)
            """,
            """
            ALTER TABLE internacao ADD
            FOREIGN KEY (id_con) REFERENCES
            consulta (id_con)
            """
            ,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (pront) REFERENCES
            paciente (pront)
            """,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (id_pac) REFERENCES
            paciente (id_pac)
            """,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (id_fun) REFERENCES
            funcionario (id_fun)
            """,
            """
            ALTER TABLE cadastro ADD
            FOREIGN KEY (cpf_fun) REFERENCES
            funcionario (cpf_fun)
            """,
            """
            ALTER TABLE agenda ADD
            FOREIGN KEY (id_fun) REFERENCES
            funcionario (id_fun)
            """,
            """
            ALTER TABLE agenda ADD
            FOREIGN KEY (cpf_fun) REFERENCES
            funcionario (cpf_fun)
            """,
            """
            ALTER TABLE agenda ADD
            FOREIGN KEY (id_con) REFERENCES
            consulta (id_con)
            """
        )

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="1234")
        cur = con.cursor()
        for c in commands:
            cur.execute(c)
        cur.close()
        con.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def cadastrar_funcionario():
    nome = input("Digite o nome: ")
    rg = input("Digite o rg: ")
    cpf = input("Digite o cpf: ")
    cargo = input("Digite o cargo: ")
    tel1 = input("Digite o telefone: ")
    tel2 = input("Digite outro telefone (opcional): ")
    crm = input("Digite o CRM (médico): ")
    cofen = input("Digite o COFEN (enfermeiro): ")
    horasplatao = input("Digite tempo de plantão: ")
    logradouro = input("Digite a rua: ")
    bairro = input("Digite o bairro: ")
    numero = input("Digite o numero: ")
    cidade = input("Digite a cidade: ")
    cep = input("Digite o cep: ")
    uf = input("Digite o estado: ")
    complemeto = input("Digite o complemento (opcional): ")

    try:

        comand = """
                INSERT INTO funcionario (cpf_fun, rg_fun, crm, cargo, cofen,
                    nome_fuc, hora_plant, end_log_fun, end_num_fun,
                    end_bairro_fun, end_cidade_fun, end_cep_fun, end_uf_fun,
                    end_comp, tel1_fun, tel2_fun) VALUES (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

        con = psycopg2.connect(host="localhost", database="sgh", user="postgres", password="postgres")
        cur = con.cursor()
        cur.execute(comand, ((cpf,), (rg,), (crm,), (cargo,), (cofen,), (nome,), (datetime.datetime.now(),), (logradouro,), (numero,),
                             (bairro,), (cidade,), (cep,), (uf,), (complemeto,), (tel1,), (tel2,),))
        con = commit()

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
    lagradouro = input("Digite a rua: ")
    bairro = input("Digite o bairro: ")
    numero = input("Digite o numero: ")
    cidade = input("Digite a cidade: ")
    cep = input("Digite o cep: ")
    uf = input("Digite o estado: ")
    complemeto = input("Digite o complemento (opcional): ")

    comand = """
            INSERT INTO paciente (id_pac, nome_pac, sexo_pac,tipo_sag, cofen,
                nome_fuc, hora_plant, end_log_fun, end_num_fun,
                end_bairro_fun, end_cidade_fun, end_cep_fun, end_uf_fun,
                end_comp, tel1_fun, tel2_fun) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s )
            )
        """


if __name__ == "__main__":
    create_tables()
    cadastrar_funcionario()






