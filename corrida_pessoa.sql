BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "corrida_pessoa" (
	"user_id"	integer NOT NULL,
	"nome"	varchar(100) NOT NULL,
	"sobrenome"	varchar(100) NOT NULL,
	"genero"	varchar(9) NOT NULL,
	"dtNasc"	date NOT NULL,
	"idade"	integer unsigned CHECK("idade" >= 0),
	"email"	varchar(254) NOT NULL,
	"distancia"	varchar(20) NOT NULL,
	PRIMARY KEY("user_id"),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "corrida_pessoa" VALUES (1,'Louis','POTTIER','M','2001-01-04',23,'louispottier44@gmail.com','21km');
INSERT INTO "corrida_pessoa" VALUES (2,'Paul','POTTIER','M','2006-10-20',18,'louispottier44@gmail.com','5km');
INSERT INTO "corrida_pessoa" VALUES (3,'Jean-Christophe','POTTIER','M','1961-10-21',63,'louispottier44@gmail.com','21km');
INSERT INTO "corrida_pessoa" VALUES (4,'Mélanie','APERT','F','1975-12-08',48,'louispottier44@gmail.com','10km');
COMMIT;
