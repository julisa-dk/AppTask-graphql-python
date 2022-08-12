create database Todo;
use Todo;
create table Task(
    id int auto_increment,
    title varchar(255) not null,
    description varchar(255) not null,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID)
);