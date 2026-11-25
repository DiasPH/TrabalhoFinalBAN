#include <iostream>
#include <string>
#include <libpq-fe.h>

using namespace std;

static const char* CONN_INFO =
    "host=localhost port=5432 dbname=tottenham_stats user=tottenham_user password=tottenham_password";

bool verificarStatus(PGconn* conn, PGresult* res, const string& acao) {
    ExecStatusType st = PQresultStatus(res);
    if (st != PGRES_COMMAND_OK && st != PGRES_TUPLES_OK) {
        cerr << "Erro ao " << acao << ": " << PQresultErrorMessage(res) << "\n";
        PQclear(res);
        return false;
    }
    return true;
}

void inserirJogador(PGconn* conn){
    string nome, cidade, estadio;
}
