drop table college;
drop table news;
drop table notice;
drop table newsComment;
drop table studentInfo;

create table college (
	id serial,
	name varchar(255) not null,
	address varchar(255) not null,
	primary key(id)
);

create table news (
	id serial,
	collegeId int not null,
	title varchar(255) not null,
	time date not null,
	sourceURL varchar(255) not null,
	picURL varchar(255),
	originURL varchar(255) not null,
	accessNum int default 0,
	primary key(id),
	foreign key(collegeId) references college(id)
);

create table notice (
	id serial,
	collegeId int not null,
	title varchar(255) not null,
	time date not null,
	sourceURL varchar(255) not null,
	originURL varchar(255) not null,
	accessNum int default 0,
	primary key(id),
	foreign key(collegeId) references college(id)
);

create table newsComment (
	id serial,
	newsId int not null,
	collegeId int not null,
	studentId varchar(255) not null,
	sourceURL varchar(255) not null,
	time date not null,
	ip varchar(255),
	enjoy int default 0,
	dislike int default 0,
	primary key(id),
	foreign key(newsId) references news(id),
	foreign key(studentId) references studentInfo(id),
	foreign key(collegeId) references college(id)
);

create table studentInfo(
	id varchar(255),
	name varchar(255) not null,
	secondName varchar(255),
	lastModified date not null,
	primary key(id)
);
