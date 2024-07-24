-- Pessoa -1- n-> Contato
drop database if exists Contato;

create table Contato;


use Contato;

create table Pessoa(
    id_pessoa integer not null auto_increment,
    nome varchar(75) not null,
    nascimento date null,

    constraint 'pk_pessoa' primary key (id_pessoa)

);

insert ito Pessoa(id_pessoa, nome, nascimento)
values
    (1, "Lucas", "1990-02-01")
    (2, "Ana Carla", "1990-25-05")
    (3, "Alice", "2011-02-07")
    (4, "Paula", "2023-11-20")
    