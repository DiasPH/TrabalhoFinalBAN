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


def insereStats(conn, posicao: int, id_jogador: int) -> bool:
    try:
        with conn.cursor() as cur:
            if posicao == 1:
                gols = lerInt("Gols: ")
                fin = lerInt("Finalizações: ")
                fin_certas = ler_int("Finalizações certas: ")
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
                    (id_jogaddor, assistencias, passes, passes_certos),
                )
                return True

            elif posicao == 3
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

            elif posicao == 4
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

            else
                print("Posição Inválida")
                return False
    except psycopg2.Error as e:
    print(f"[ERRO POSIÇÃO] {e}")
    return False

def inserir_opt(conn) -> None:
    