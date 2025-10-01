CREATE DATABASE read_file;
use read_file;

CREATE TABLE file_details (
    fileID INT auto_increment,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(400) NOT NULL,
    PRIMARY KEY (fileID)  
);

ALTER TABLE file_details
MODIFY fileID INT AUTO_INCREMENT PRIMARY KEY;

ALTER TABLE file_details DROP PRIMARY KEY;

select *
from file_details;

INSERT INTO file_details (title, description)  
VALUES ('file3.txt', 'home insurance details'); 

 