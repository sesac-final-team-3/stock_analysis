CREATE TABLE IF NOT EXISTS tb_news (
    ID int auto_increment NOT NULL PRIMARY KEY , 
    DomainID tinyint NOT NULL , 
    MainCategory varchar(16) , 
    SubCategory varchar(16) ,
    WritedAt DATETIME  ,
    Title varchar(128) , 
    Content text NOT NULL, 
    URL varchar(255) , 
    PhotoURL text NULL, 
    Writer varchar(16) , 
    Stickers TEXT ,
    FOREIGN KEY (DomainID) REFERENCES tb_domain(ID) ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS tb_comment (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NewsID int NOT NULL,
    UserID int NOT NULL,
    WritedAt DATETIME NULL,
    Content text NULL,

    FOREIGN KEY (NewsID) REFERENCES tb_news(ID) ON UPDATE CASCADE,
    FOREIGN KEY (UserID) REFERENCES tb_user(ID) ON UPDATE CASCADE
);

CREATE TABLE tb_user (
    ID int auto_increment NOT NULL PRIMARY KEY,
    DomainID tinyint,
    UserID VARCHAR(16),
    UserName VARCHAR (32),
    FOREIGN KEY (DomainID) REFERENCES tb_domain(ID) ON UPDATE CASCADE
);

CREATE TABLE tb_domain (
    ID tinyint auto_increment NOT NULL PRIMARY KEY,
    name VARCHAR(10)
);