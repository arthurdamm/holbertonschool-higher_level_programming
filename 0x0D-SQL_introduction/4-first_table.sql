-- Creates first table
-- Create first_table with id, name
CREATE TABLE IF NOT EXISTS first_table (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=INNODB;
