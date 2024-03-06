-- First round of scripts
-- DROP TABLE Websites
-- DROP TABLE Passwords

CREATE TABLE Passwords (
    password_id VARCHAR(20),
    encrypted_password VARCHAR(50) NOT NULL,
    PRIMARY KEY (password_id)
)

CREATE TABLE Websites (
    website VARCHAR(100) NOT NULL,
    username VARCHAR(80), -- could also force
    password_id VARCHAR(20) NOT NULL REFERENCES Passwords,
    encrypted_password VARCHAR(50) NOT NULL REFERENCES Passwords,
    PRIMARY KEY (website, username)
)