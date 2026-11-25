CREATE TABLE jogador (
    id_jogador SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL CHECK (idade >= 16),
    nacionalidade VARCHAR(60) NOT NULL,
    numero_camisa INT NOT NULL CHECK (numero_camisa BETWEEN 1 AND 99),
    jogos_disputados INT NOT NULL DEFAULT 0 CHECK (jogos_disputados >= 0)
);

CREATE TABLE atacante (
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	gols INT NOT NULL DEFAULT 0 CHECK (gols >= 0),
	finalizacoes INT NOT NULL DEFAULT 0 CHECK (finalizacoes >= 0),
	finalizacoes_certas INT NOT NULL DEFAULT 0 CHECK (finalizacoes_certas >= 0)
);

CREATE TABLE meio_campista(
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	assistencias INT NOT NULL DEFAULT 0 CHECK (assistencias >= 0),
	passes INT NOT NULL DEFAULT 0 CHECK (assistencias >= 0),
	passes_certos INT NOT NULL DEFAULT 0 CHECK (passes_certos >= 0)
);

CREATE TABLE zagueiro (
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	desarmes INT NOT NULL DEFAULT 0 CHECK (desarmes >=0),
	interceptacoes INT NOT NULL DEFAULT 0 CHECK (interceptacoes >= 0),
	faltas INT NOT NULL DEFAULT 0 CHECK (faltas >= 0)
);


CREATE TABLE goleiro (
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	defesas INT NOT NULL DEFAULT 0 CHECK (defesas >= 0),
	gols_sofridos INT NOT NULL DEFAULT 0 CHECK (gols_sofridos >= 0),
	clean_sheets INT NOT NULL DEFAULT 0 CHECK (clean_sheets >= 0)
);


