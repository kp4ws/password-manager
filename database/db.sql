CREATE TABLE Websites (
	title VARCHAR(50),
	hashed_pass VARCHAR(16) NOT NULL
);

-- pass_id will start at 1000 and go up with each entry
CREATE TABLE Passwords (
	pass_id INT AUTO_INCREMENT,
	encrypted_pass VARCHAR(16) NOT NULL,
	PRIMARY KEY (pass_id)
) AUTO_INCREMENT = 1000;
