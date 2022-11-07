--  creates the database hbtn_0d_usa and the table states (in the database cities) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    state_id INT NOT NULL FOREIGN KEY REFERENCES states(id),
    name VARCHAR(256) NOT NULL
)