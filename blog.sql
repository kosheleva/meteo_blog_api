CREATE DATABASE IF NOT EXISTS blog;
USE blog;


CREATE TABLE IF NOT EXISTS blog.Categories (
	id INTEGER AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS blog.Tags (
	id INTEGER AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS blog.Authors (
	id INTEGER AUTO_INCREMENT,
    nickname VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    status ENUM('active', 'blocked', 'deleted') NOT NULL,
    created_at DATETIME NOT NULL, 
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS blog.Posts (
	id INTEGER AUTO_INCREMENT,
    title VARCHAR(300) NOT NULL,
    content TEXT NOT NULL,
    is_visible BOOLEAN NOT NULL,
    created_at DATETIME NOT NULL, 
    updated_at DATETIME NOT NULL, 
    author_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (author_id) REFERENCES Authors(id),
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);


CREATE TABLE IF NOT EXISTS blog.PostsTags (
	id INTEGER AUTO_INCREMENT,
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (post_id) REFERENCES Posts(id),
    FOREIGN KEY (tag_id) REFERENCES Tags(id)
);


INSERT INTO blog.Categories
    (title)
VALUES
    ('Cars'),
    ('Nature');


INSERT INTO blog.Tags
    (title)
VALUES
    ('kids'),
    ('memes');

