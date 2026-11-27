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
	finalizacoes_certas INT NOT NULL DEFAULT 0 CHECK (finalizacoes_certas >= 0 AND finalizacoes_certas <= finalizacoes)
);

CREATE TABLE meio_campista(
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	assistencias INT NOT NULL DEFAULT 0 CHECK (assistencias >= 0),
	passes INT NOT NULL DEFAULT 0 CHECK (passes >= 0),
	passes_certos INT NOT NULL DEFAULT 0 CHECK (passes_certos >= 0 AND passes_certos <= passes)
);

CREATE TABLE zagueiro (
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	desarmes INT NOT NULL DEFAULT 0 CHECK (desarmes >= 0),
	interceptacoes INT NOT NULL DEFAULT 0 CHECK (interceptacoes >= 0),
	faltas INT NOT NULL DEFAULT 0 CHECK (faltas >= 0)
);


CREATE TABLE goleiro (
	id_jogador INT PRIMARY KEY REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	defesas INT NOT NULL DEFAULT 0 CHECK (defesas >= 0),
	gols_sofridos INT NOT NULL DEFAULT 0 CHECK (gols_sofridos >= 0),
	clean_sheets INT NOT NULL DEFAULT 0 CHECK (clean_sheets >= 0)
);

CREATE TABLE adversario (
	nome_adversario VARCHAR(100) PRIMARY KEY CHECK (btrim(nome_adversario) <> ''),
	pais VARCHAR(100) NOT NULL,
	estadio VARCHAR(100) NOT NULL
);

CREATE TABLE partida (
	id_partida SERIAL PRIMARY KEY,
	data DATE NOT NULL,
	local VARCHAR(100) NOT NULL,
	nome_adversario VARCHAR(100) NOT NULL REFERENCES adversario(nome_adversario) ON UPDATE CASCADE ON DELETE RESTRICT,
	gols_tottenham INT NOT NULL CHECK (gols_tottenham >= 0),
	gols_adversario INT NOT NULL CHECK (gols_adversario >= 0)
);

CREATE TABLE participacao (
	id_partida INT REFERENCES partida(id_partida) ON DELETE CASCADE,
	id_jogador INT REFERENCES jogador(id_jogador) ON DELETE CASCADE,
	tempo_jogado INT NOT NULL CHECK (tempo_jogado >= 0 AND tempo_jogado <= 90),
	titular BOOLEAN NOT NULL DEFAULT FALSE,
	gols_partida INT NOT NULL DEFAULT 0 CHECK (gols_partida >= 0),
	assistencias_partida INT NOT NULL DEFAULT 0 CHECK (assistencias_partida >= 0),
	PRIMARY KEY (id_partida, id_jogador)
); 


