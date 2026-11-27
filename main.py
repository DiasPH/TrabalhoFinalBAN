import psycopg2

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 5433,
    "dbname": "tottenham_stats",
    "user": "tottenham_user",
    "password": "tottenham_password",
}

def lerInt(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def listaJogadores(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id_jogador, nome, numero_camisa FROM jogador ORDER BY id_jogador;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    


def insereStats(conn, posicao: int, id_jogador: int) -> bool:
    try:
        with conn.cursor() as cur:
            if posicao == 1:
                gols = lerInt("Gols: ")
                fin = lerInt("Finalizações: ")
                fin_certas = lerInt("Finalizações certas: ")
                cur.execute(
                    """
                    INSERT INTO atacante (id_jogador, gols, finalizacoes, finalizacoes_certas)
                    VALUES (%s, %s, %s, %s);
                    """,
                    (id_jogador, gols, fin, fin_certas),
                )
                return True

            elif posicao == 2:
                assistencias = lerInt("Assistências: ")
                passes = lerInt("Passes: ")
                passes_certos = lerInt("Passes Certos: ")
                cur.execute(
                    """
                    INSERT INTO meio_campista (id_jogador, assistencias, passes, passes_certos)
                    VALUES(%s, %s, %s, %s);
                    """,
                    (id_jogador, assistencias, passes, passes_certos),
                )
                return True

            elif posicao == 3:
                desarmes = lerInt("Desarmes: ")
                interceptacoes = lerInt("Interceptações: ")
                faltas = lerInt("Faltas cometidas: ")
                cur.execute(
                    """
                    INSERT INTO zagueiro (id_jogador, desarmes, interceptacoes, faltas)
                    VALUES(%s, %s, %s, %s);
                    """,
                    (id_jogador, desarmes, interceptacoes, faltas),
                )
                return True

            elif posicao == 4:
                defesas = lerInt("Defesas: ")
                gols_sofridos = lerInt("Gols Sofridos: ")
                clean_sheets = lerInt("Clean Sheets: ")
                cur.execute(
                    """
                    INSERT INTO goleiro (id_jogador, defesas, gols_sofridos, clean_sheets)
                    VALUES(%s, %s, %s, %s);
                    """,
                    (id_jogador, defesas, gols_sofridos, clean_sheets),
                )
                return True

            else:
                print("Posição Inválida")
                return False
    except psycopg2.Error as e:
        print(f"[ERRO POSIÇÃO] {e}")
        return False

def inserir_opt(conn) -> None:
    print("1 - Novo Jogador")
    print("2 - Inserir na tabela Atacante")
    print("3 - Inserir na tabela Meio-Campista")
    print("4 - Inseir na tabela zagueiro")
    print("5 - Inserir na tabela goleiro")
    print("6 - Inseir jogador sem posição")
    opt = lerInt("Escolha: ")

    if opt == 1:
        nome = input("Nome: ").strip()
        idade = lerInt("Idade (>=16): ")
        nac = input("Nacionalidade: ").strip()
        camisa = lerInt("Numero da Camisa (1..99): ")
        jogos = lerInt("Jogos Disputados: ")
        print("Escolha posição: ")
        print("1 - Atacante")
        print("2 - Meio-Campista")
        print("3 - Zagueiro")
        print("4 - Goleiro")
        pos = lerInt("Escolha: ")

        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO jogador (nome, idade, nacionalidade, numero_camisa, jogos_disputados)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id_jogador
                    """,
                    (nome, idade, nac, camisa, jogos),
                )
                id_jogador = cur.fetchone()[0]

            if not insereStats(conn, pos, id_jogador):
                conn.rollback()
                return

            conn.commit()
            print(f"Inserido com sucesso! id_jogador = {id_jogador}")
        except psycopg2.Error as e:
            conn.rollback()
            print(f"[ERRO JOGADOR] {e}")

    elif 2 <= opt <= 5:
        listaJogadores(conn)
        id_jogador = lerInt("Id jogador existente: ")
        if(insereStats(conn, opt-1, id_jogador)):
            conn.commit()
            print("Registro inserido na tabela.")
        else:
            print("Opção inválida.")

    elif opt == 6:
        nome = input("Nome: ").strip()
        idade = lerInt("Idade (>=16): ")
        nac = input("Nacionalidade: ").strip()
        camisa = lerInt("Numero da Camisa (1..99): ")
        jogos = lerInt("Jogos Disputados: ")

        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO jogador (nome, idade, nacionalidade, numero_camisa, jogos_disputados)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id_jogador
                    """,
                    (nome, idade, nac, camisa, jogos),
                )
                conn.commit()
                print(f"Inserido com sucesso! id_jogador = {id_jogador}")

        except:
            conn.rollback()
            print(f"[ERRO JOGADOR] {e}")
        
def remover_opt(conn) -> None:
    print("MENU: ")
    print("1 - Remover da tabela jogador")
    print("2 - Remover da tabela atacante")
    print("3 - Remover da tabela meio-campista")
    print("4 - Remover da tabela zagueiro")
    print("5 - Remover da tabela goleiro")



def main() -> None:
    conn = None

    try:
        conn = psycopg2.connect(**DB_CONFIG)
    except psycopg2.Error as e:
        print(f"Falha ao conectar no PostgreSQL: {e}")
        return

    try:    
        if conn is not None:
            while True:
                print("Menu Principal")
                print("==================")
                print("1 - Inserir novas tuplas")
                opt = lerInt("Escolha: ")

                if opt == 1:
                    inserir_opt(conn)

                else:
                    print("Opção inválida")

    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    main()
