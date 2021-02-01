drop database financaspessoais;
create database financaspessoais;
use financaspessoais;

create table ano(
	idano int not null auto_increment,
    numeroano int not null,
    primary key (idano));
    
create table mes (
	id int not null auto_increment,
    nome varchar(10) not null,
    numero int not null,
    idano int not null,
    primary key(id),
	CONSTRAINT fk_mes_ano FOREIGN KEY (idano) REFERENCES ano (idano));

create table contabanco(
	id int not null auto_increment,
    nomebanco varchar(64) not null,
    primary key(id));   

create table cartaofatura(
	id int not null auto_increment,
    idbanco int not null,
	produtoservico varchar(64) not null,
    data date not null,
    valor decimal(6,2) not null,
    nparcelas int not null,
    idmes int not null,
    primary key (id),
    CONSTRAINT fk_cartaofatura_mes foreign key (idmes) references mes(id),
    CONSTRAINT fk_cartaofatura_contabanco foreign key (idbanco) references contabanco(id));
    
 
    
create table dividafixa(
	id int not null auto_increment,
    nome varchar(64) not null,
    data date not null,
    valor decimal(6,2) not null,
    primary key(id),
    idmes int not null,
    idconta int null,
    constraint fk_dividafixa_contabanco foreign key(idconta) references contabanco(id),
    constraint fk_dividafixa_mes foreign key(idmes) references mes(id));
    

    

 alter table contabanco add column credito boolean not null default 0;
 alter table contabanco add column debito boolean not null default 0;
 alter table contabanco add column limitecredito decimal(6,2) null;

insert into ano (numeroano) values ('2025');
insert into cartaofatura(banco, produtoservico, data, valor, idmes) values('bradesco', 'chinelo', '2021/01/12', '20.90','3');
insert into mes(nome, numero, idano) values ('janeiro', '1', '1'),('fevereiro', '2','1'),('março', '3','1'),('abril', '4','1'),('maio', '5','1'),('junho', '6','1'),('julho', '7','1'),('agosto', '8','1'),('setembro', '9','1'),('outubro', '10','1'),('novembro', '11','1'),('dezembro', '12','1');
insert into mes(nome, numero, idano) values ('janeiro', '1', '2'),('fevereiro', '2','2'),('março', '3','2'),('abril', '4','2'),('maio', '5','2'),('junho', '6','2'),('julho', '7','2'),('agosto', '8','2'),('setembro', '9','2'),('outubro', '10','2'),('novembro', '11','2'),('dezembro', '12','2');
insert into mes(nome, numero, idano) values ('janeiro', '1', '3'),('fevereiro', '2','3'),('março', '3','3'),('abril', '4','3'),('maio', '5','3'),('junho', '6','3'),('julho', '7','3'),('agosto', '8','3'),('setembro', '9','3'),('outubro', '10','3'),('novembro', '11','3'),('dezembro', '12','3');
insert into mes(nome, numero, idano) values ('janeiro', '1', '4'),('fevereiro', '2','4'),('março', '3','4'),('abril', '4','4'),('maio', '5','4'),('junho', '6','4'),('julho', '7','4'),('agosto', '8','4'),('setembro', '9','4'),('outubro', '10','4'),('novembro', '11','4'),('dezembro', '12','4');
insert into mes(nome, numero, idano) values ('janeiro', '1', '5'),('fevereiro', '2','5'),('março', '3','5'),('abril', '4','5'),('maio', '5','5'),('junho', '6','5'),('julho', '7','5'),('agosto', '8','5'),('setembro', '9','5'),('outubro', '10','5'),('novembro', '11','5'),('dezembro', '12','5');

insert into dividafixa(nome,data, valor, idmes, idconta) values ('contatelefone', '2020/01/21', '59.90','3', 2);
insert into contabanco(nomebanco) values('NuBank');
insert into contabanco (nomebanco, debito, credito, limitecredito) values ('inter','1','1',null);

truncate contabanco;