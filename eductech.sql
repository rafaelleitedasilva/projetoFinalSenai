create database eductech;

use eductech;

CREATE TABLE `eductech`.`cadastro_aluno` (
  `RA` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `RG` INT NOT NULL,
  `CPF` INT NOT NULL,
  `Data_Nascimento` DATE NOT NULL,
  `Sexo` VARCHAR(1) NOT NULL,
  `Nome_pai` VARCHAR(45) NOT NULL,
  `Nome_mae` VARCHAR(45) NOT NULL,
  `Endereco` VARCHAR(150) NOT NULL,
  `Telefone` INT NOT NULL,
  `Escola` VARCHAR(100) NOT NULL,
  `Bloqueado` TINYINT NOT NULL,
  /*FK*/
  `Sigla` VARCHAR(10) NOT NULL,
  `ID_Calendario` INT,
  PRIMARY KEY (`RA`));

CREATE TABLE `eductech`.`cadastro_professor` (
  `NIF` VARCHAR(9) NOT NULL,
  `Nome` VARCHAR(70) NULL,
  `Formacao` VARCHAR(200) NULL,
  `Data_Nascimento` DATE NULL,
  `CPF` INT NULL,
  `RG` INT NULL,
  `Endereco` VARCHAR(150) NULL,
  `Sexo` VARCHAR(1) NULL,
  `Telefone` INT NULL,
  `Email` VARCHAR(100) NULL,
  `Senha` VARCHAR(100) NULL,
  /*FK*/ 
  `ID_Calendario` INT,
  `Sigla` VARCHAR(10) NOT NULL,
  `Nome_Disciplina`	VARCHAR(50),
  PRIMARY KEY (`NIF`));

CREATE TABLE `eductech`.`calendario` (
  `ID_Calendario` INT,
  `Data_Emissao` DATE NOT NULL,
  `Data_Entrega` DATE,
  `Anotacao` VARCHAR(1000) NULL,
  /*FK*/ 
  `RA` INT NOT NULL,
  `NIF` VARCHAR(9) NOT NUll,
  `Sigla` VARCHAR(50),
  PRIMARY KEY (`ID_Calendario`));
  
CREATE TABLE `eductech`.`disciplinas` (
  `Nome_Disciplina` VARCHAR(50) NOT NULL,
  /*FK*/ 
  `Sigla` VARCHAR(9) NOT NULL,
  `Nome_Curso` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Nome_Disciplina`));
  
CREATE TABLE `eductech`.`curso`(
	`Nome_Curso` VARCHAR(100) NOT NULL,
    /*FK*/ 
    `Nome_Disciplina` VARCHAR(50) NOT NULL,
	`Sigla` VARCHAR(10) NOT NULL,
    PRIMARY KEY (`Nome_Curso`));
    
CREATE TABLE `eductech`.`turmas` (
	`Sigla` VARCHAR(10) NOT NULL,    
    `Qtde_Alunos` INT,
    `Data_Inicio` DATE,
    `Data_Fim` DATE,
    `Horario_Entrada` TIME,
    `Horario_Saida` TIME,
    /*FK*/ 
    `NIF` VARCHAR(9) NOT NULL,
    `Nome_Curso` VARCHAR(100) NOT NULL);
  


/*Add cadastro_aluno FKs*/

alter table cadastro_aluno
add foreign key (Sigla) references turmas(Sigla);
alter table cadastro_aluno
add foreign key (ID_Calendario) references calendario(ID_Calendario);

/*Add cadastro_professor FKs*/

alter table cadastro_professor
add foreign key (ID_Calendario) references calendario(ID_Calendario);
alter table cadastro_professor
add foreign key (Sigla) references turmas(Sigla);
alter table cadastro_professor
add foreign key (Nome_Disciplina) references disciplinas(Nome_Disciplina);

/*Add calendario FKs*/

alter table calendario
add foreign key (NIF) references cadastro_professor(NIF);
alter table calendario
add foreign key (RA) references cadastro_aluno(RA);
alter table calendario
add foreign key (Sigla) references turmas(Sigla);

/*Add disciplinas FKs*/

alter table disciplinas
add foreign key (Sigla) references turmas(Sigla);
alter table disciplinas
add foreign key (Nome_Curso) references curso(Nome_Curso);

/*Add curso FKs*/

alter table curso
add foreign key (Nome_Disciplina) references disciplinas(Nome_Disciplina);
alter table curso
add foreign key (Sigla) references turmas(Sigla);

/*Add turmas FKs*/

alter table turmas
add foreign key (Nome_Curso) references curso(Nome_Curso);
alter table turmas
add foreign key (NIF) references cadastro_professor(NIF);
  
insert into turmas 
values ('M2DSI', 40, '2022-01-27' , '2023-06-23', '07:45:00', '11:45:00', 0, "Técnico em Desenvolvimento de Sistemas");

insert into cadastro_aluno
values (0123456, 'Manuel Gomi', 0123456, 0123456, '1980-12-25' , 'M', 'José Gomi', 'Josefina Gomi', 'Rua da Caneta Azul, Bairro do Ai Ai Ai', 646554, 'Escola Estadual Profº Francisco Lourenço De Melo', 1, 'M2DSI', 0);
insert into cadastro_aluno
values (01234567, 'Manuel Gomi', 0123456, 0123456, '1980-12-25' , 'M', 'José Gomi', 'Josefina Gomi', 'Rua da Caneta Azul, Bairro do Ai Ai Ai', 646554, 'Escola Estadual Profº Francisco Lourenço De Melo', 1, 'M2DSI', 0);
select *from turmas;

drop database eductech;
drop table cadastro_aluno;

