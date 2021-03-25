CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 주석

INSERT INTO classmates
(name, age, address)
VALUES 
('john', 20, 'seoul'),
('john', 20, 'seoul'),
('john', 20, 'seoul'),
('john', 20, 'seoul'),
('john', 20, 'seoul'),
('john', 20, 'seoul'),
('john', 20, 'seoul');

-- 이거는 안되네...


SELECT name, age FROM classmates;

-- 제한 수
SELECT * FROM classmates LIMIT 3;

-- 오프셋
SELECT rowid, * FROM classmates LIMIT 1 OFFSET 2;

-- 조건으로 불러오기
SELECT * FROM classmates WHERE name='tony';

-- 필드값 중복 없이 불러오기
SELECT DISTINCT age FROM classmates;

-- 삭제
DELETE FROM classmates WHERE rowid=4;


CREATE TABLE tests (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);

INSERT INTO tests (name) VALUES ('최철순');

-- WHERE 조건
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;


SELECT * FROM users WHERE age>=30;

SELECT first_name, last_name FROM users WHERE age>=30;

SELECT last_name, age FROM users WHERE age>=30 AND last_name='김';

SELECT COUNT(*) FROM users;

SELECT AVG(age) FROM users WHERE age>=30;

SELECT first_name, MAX(balance) FROM users;

SELECT AVG(balance) FROM users WHERE age>=30;

SELECT * FROM users WHERE age LIKE '2_';

-- tests 예시
CREATE TABLE tests (
age INTEGER,
name TEXT
);

INSERT INTO tests VALUES (20, 'tony'), (30, 'eric'), (40, 'juan');

-- 숫자형 패턴으로 찾기!
SELECT * FROM tests WHERE age LIKE '3_';

-- 글자형 정렬 주의!
SELECT * FROM users ORDER BY balance DESC;



SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%-5114-%';


-- default
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age LIMIT 10;

SELECT * FROM users ORDER BY age, last_name LIMIT 10;

SELECT last_name, first_name 
FROM users ORDER BY balance 
DESC LIMIT 10;


SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name;


CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('제목', '내용'), ('제목2', '내용2');


ALTER TABLE articles RENAME TO news;

-- nullable
ALTER TABLE news ADD COLUMN created_at TEXT;

-- 디폴트
ALTER TABLE news ADD COLUMN updated_at TEXT NOT NULL DEFAULT '2021-03-25';