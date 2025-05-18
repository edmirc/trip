USE trip1;
CREATE TABLE IF NOT exists citys (
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (100) NOT NULL,
    state VARCHAR (2) NOT NULL,
    description VARCHAR(300) NULL,
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS type (
	id INT AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    description VARCHAR(300) NULL,
    
    PRIMARY KEY (id),
    UNIQUE KEY (name)
);

CREATE TABLE IF NOT EXISTS cars (
	id INT AUTO_INCREMENT,
    plate VARCHAR(7) not null,
    model varchar(50) not null,
    km int not null,
    description VARCHAR(200) null,
    
    primary key (id),
    unique key(plate)
);

create table if not exists fuel(
	id int auto_increment,
    km_init int not null,
    km_end int not null,
    km_total int,
    fuel enum('Gasolina', 'Etanol', 'Diesel'),
    average decimal(10,2),
    description varchar(300),
    
    primary key (id)
);

create table if not exists notes(
	id bigint auto_increment,
    number bigint not null,
    path varchar(500) not null,
    description varchar(200) null,
    
    primary key(id)
);
 

 create table if not exists exes(
	id bigint auto_increment,
    date date not null,
    type int not null,
    note bigint not null,
    car int not null,
    fuel int not null,
    city bigint not null,
    date_criate date default(current_date()),
     
     primary key(id),
    foreign key(type) references type(id),
    foreign key(note) references notes(id),
    foreign key(car) references cars(id),
    foreign key(fuel) references fuel(id),
    unique(fuel),
    foreign key(city) references citys(id)
 );
 
 delimiter 
	 create procedure if not exists insert_fuel(
		in kminit int,
		in kmend int,
		in infuel enum('Gasolina', 'Etanol', 'Diesel'),
		in qnt decimal(10,2),
		in indescription varchar(300) null,
		out id_insert int
		)
		begin
			declare kmtotal decimal(10,2);
			declare inaverage decimal(10,2);
			set kmtotal = kmend - kminit;
			set inaverage = kmtotal / qnt;
			
			insert into fuel (km_init, km_end, km_total, fuel, average, description)
			values (kminit, kmend, kmtotal, infuel, inaverage, description); 
	 
			set id_insert = last_insert_id();
		end 
 delimiter ;