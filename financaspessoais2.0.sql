create database financaspessoais;
use financaspessoais;

create table usuario(
    id int not null auto_increment,
    nome varchar(64) not null,
    email varchar(254) not null,
    senha varchar(64) not null,
    primary key(id),
    unique(email)
);

create table ano(
    idano int not null auto_increment,
    numeroano int not null,
    primary key (idano)
);

create table mes(
    id int not null auto_increment,
    nome varchar(10) not null,
    numero int not null,
    idano int not null,
    primary key(id),
    CONSTRAINT fk_mes_ano FOREIGN KEY (idano) REFERENCES ano (idano)
);

create table contabanco(
    id int not null auto_increment,
    nomebanco varchar(64) not null,
    idusuario int not null,
    credito boolean not null default 0,
    debito boolean not null default 0,
    limitecredito decimal(6,2) null,
    primary key(id),
    CONSTRAINT fk_contabanco_usuario FOREIGN KEY (idusuario) REFERENCES usuario (id)
);

create table categoria (
    id int not null auto_increment,
    nome ENUM('Alimentação', 'Transporte', 'Moradia', 'Educação', 'Saúde', 'Lazer', 'vestuário','comunicação', 'impostos', 'Outros') NOT NULL,
    primary key(id)
);

create table movimentacao(
    id int not null auto_increment,
    idbanco int not null,
	idcategoria int not null,
    descricao varchar(64) not null,
    data date not null,
    valor decimal(6,2) not null,
    nparcelas int not null,
    idmes int not null,
    primary key (id),
    CONSTRAINT fk_movimentacao_mes FOREIGN KEY (idmes) REFERENCES mes(id),
	CONSTRAINT fk_movimentacao_categoria FOREIGN KEY (idcategoria) REFERENCES categoria (id),
    CONSTRAINT fk_movimentacao_contabanco FOREIGN KEY (idbanco) REFERENCES contabanco(id)
);

create table dividafixa(
    id int not null auto_increment,
    nome varchar(64) not null,
    data date not null,
    valor decimal(6,2) not null,
    idmes int not null,
    idbanco int null,
	idcategoria int not null,
    primary key(id),
    CONSTRAINT fk_dividafixa_contabanco FOREIGN KEY(idbanco) REFERENCES contabanco(id),
	CONSTRAINT fk_dividafixa_categoria FOREIGN KEY (idcategoria) REFERENCES categoria (id),
    CONSTRAINT fk_dividafixa_mes FOREIGN KEY(idmes) REFERENCES mes(id)
);
