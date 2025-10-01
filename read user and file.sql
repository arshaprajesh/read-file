CREATE DATABASE read_file;
use read_file;

select *
from file_details;

select *
from user_details;

select *
from user_file_link;


ALTER TABLE file_details 
ADD CONSTRAINT user_id_foreign_key 
FOREIGN KEY(user_id) 
REFERENCES user_details(userID); 

SELECT *
FROM user_details uf
JOIN file_details u 
ON uf.userID = u.fileID
WHERE uf.userID = 1;


INSERT INTO file_details (
    title,
    description,
    created_by,
    created_at,
    updated_by,
    updated_at,
    user_id
) VALUES (
    'mary.txt',
    'Initial draft of the project proposal',
    'maya',
    '2025-09-27',
    'arsha',
    '2025-09-27',
    2  -- This links to userID in user_details
);


SELECT COUNT(user_id) AS user_count
FROM file_details
WHERE fileID = 25;


SELECT user_id
FROM file_details
WHERE fileID = 25;


SELECT *
FROM information_schema.tables
WHERE table_name = 'file_details';


SELECT 
    u.userID,
    u.name,
    u.date,
    u.state,
    f.fileID,
    f.title,
    f.description
FROM 
    user_details u
INNER JOIN 
    file_details f
ON 
    u.userID = f.user_id;


INSERT INTO user_details 
(name, date, state, Created_by, Created_at, updated_by, updated_at)
VALUES 
('arsha', '2025-08-01', 'nc', 'arsha', '2025-08-01', 'praji', '2025-08-01');


ALTER TABLE user_details
ADD COLUMN updated_by VARCHAR(255),
ADD COLUMN updated_at Date;

ALTER TABLE file_details ADD COLUMN user_id INT;


ALTER TABLE file_details ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(userID);


INSERT INTO user_file_link (user_id, file_id) VALUES (2, 20);

