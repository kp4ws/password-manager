--DROP TABLE Websites;
--DROP TABLE Passwords;

CREATE TABLE Websites (
	title VARCHAR(50) PRIMARY KEY,
	url VARCHAR(100),
	username VARCHAR(16),
	hashed_pass VARCHAR(16) NOT NULL,
	date_created DATE NOT NULL
);

-- pass_id will start at 1000 and go up with each entry
CREATE TABLE Passwords (
	pass_id INT AUTO_INCREMENT,
	website VARCHAR(50) NOT NULL,
	encrypted_pass VARCHAR(16) NOT NULL,
	FOREIGN KEY (website) REFERENCES Websites(title),
	PRIMARY KEY (pass_id)
) AUTO_INCREMENT = 1000;
