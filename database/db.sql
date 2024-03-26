--DROP TABLE Passwords;

CREATE TABLE Passwords (
	pass_id INT AUTO_INCREMENT,
	website_title VARCHAR(50),
	url VARCHAR(50),
	username VARCHAR(20),
	encrypted_pass VARCHAR(16) NOT NULL,
	date_created DATE NOT NULL,
	PRIMARY KEY (pass_id)
) AUTO_INCREMENT = 1000;
