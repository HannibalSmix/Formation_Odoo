-- DROP TABLE IF EXISTS users CASCADE;
-- DROP TABLE IF EXISTS profiles CASCADE;
-- DROP TABLE IF EXISTS publishers CASCADE;
-- DROP TABLE IF EXISTS games CASCADE;
-- DROP TABLE IF EXISTS user_games CASCADE;
-- DROP TABLE IF EXISTS reviews CASCADE;

-- CREATE TABLE users (
-- 	id int primary key GENERATED ALWAYS AS IDENTITY,
-- 	user_name varchar(64) NOT NULL UNIQUE CHECK(LENGTH(user_name) >= 2),
-- 	email varchar(128) UNIQUE NOT NULL CHECK (email LIKE '%@%.%'),
-- 	--dob date NOT NULL CHECK (DATE_PART('YEAR',dob) >= 1900 AND EXTRACT(YEAR FROM AGE(NOW(), dob)) > 13),
-- 	dob date NOT NULL CHECK(dob >= '1900-01-01' and dob <= current_date - INTERVAL '13 YEARS'),
-- 	country varchar(64),
-- 	created_at timestamptz DEFAULT NOW()
-- );

-- CREATE TABLE profiles(
-- 	id int primary key GENERATED ALWAYS AS IDENTITY,
-- 	bio text,
-- 	avatar varchar(256),
-- 	user_id int NOT NULL UNIQUE,
-- 	CONSTRAINT FK_profiles_users FOREIGN KEY(user_id) REFERENCES users(id)
-- 	ON DELETE CASCADE
-- );

-- CREATE TABLE publishers(
-- 	id int primary key GENERATED ALWAYS AS IDENTITY,
-- 	name varchar(64) NOT NULL UNIQUE
-- );

-- CREATE TABLE games(
-- 	id int primary key GENERATED ALWAYS AS IDENTITY,
-- 	title varchar(64) NOT NULL CHECK (CHAR_LENGTH(title) >= 2),
-- 	price decimal(10,2),
-- 	release_date Date,
-- 	publisher_id int,
-- 	CONSTRAINT FK_games_publishers FOREIGN KEY(publisher_id) REFERENCES publishers(id)
-- 	ON DELETE SET NULL
-- );

-- CREATE TABLE user_games(
-- 	user_id int NOT NULL,
-- 	game_id int NOT NULL,
-- 	played_time int DEFAULT 0,
-- 	purchased_date timestamptz, --tz pour timezone
-- 	CONSTRAINT FK_user_games_users FOREIGN KEY(user_id) 
-- 	REFERENCES users(id) ON DELETE SET NULL,
-- 	CONSTRAINT FK_user_games_games FOREIGN KEY(game_id) 
-- 	REFERENCES games(id) ON DELETE CASCADE,
-- 	PRIMARY KEY (user_id, game_id)
-- );

-- CREATE TABLE reviews(
-- 	id int primary key GENERATED ALWAYS AS IDENTITY,
-- 	user_id int,
-- 	game_id int,
-- 	rating int NOT NULL CHECK (rating BETWEEN 0 AND 5),
-- 	comment text CHECK (CHAR_LENGTH(comment) >= 2),
-- 	created_at timestamptz DEFAULT now(),
-- 	CONSTRAINT FK_reviews_users FOREIGN KEY(user_id) 
-- 	REFERENCES users(id) ON DELETE SET NULL,
-- 	CONSTRAINT FK_reviews_games FOREIGN KEY(game_id) 
-- 	REFERENCES games(id) ON DELETE CASCADE
-- );

-- -- commentaires 
-- -- ALTER ...
-- -- TRUNCATE TABLE --> vide table du contenu --> plus rapide que delete

-- SELECT (10/3.0) as "Haha @ hoho"

-- DROP TABLE IF EXISTS reviews;
-- DROP TABLE IF EXISTS user_games;
-- DROP TABLE IF EXISTS profiles;
-- DROP TABLE IF EXISTS games;
-- DROP TABLE IF EXISTS publishers;
-- DROP TABLE IF EXISTS users;
 
-- CREATE TABLE users (
--     id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     username VARCHAR(50) NOT NULL UNIQUE CHECK (LENGTH(username) >= 3),
--     email VARCHAR(100) NOT NULL UNIQUE CHECK (email LIKE '%@%'),
--     country VARCHAR(50) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- CREATE TABLE profiles (
--     id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     user_id INT NOT NULL UNIQUE,
--     bio TEXT,
--     avatar_url TEXT,
--     birth_date DATE,
--     CONSTRAINT fk_profiles_users
--         FOREIGN KEY (user_id)
--         REFERENCES users(id)
--         ON DELETE CASCADE
-- );
-- CREATE TABLE publishers (
--     id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     name VARCHAR(100) NOT NULL UNIQUE,
--     country VARCHAR(50) NOT NULL
-- );
-- CREATE TABLE games (
--     id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     title VARCHAR(100) NOT NULL UNIQUE,
--     price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
--     release_date DATE,
--     publisher_id INT NOT NULL,
--     CONSTRAINT fk_games_publishers
--         FOREIGN KEY (publisher_id)
--         REFERENCES publishers(id)
-- );
-- CREATE TABLE user_games (
--     user_id INT NOT NULL,
--     game_id INT NOT NULL,
--     hours_played INT DEFAULT 0 CHECK (hours_played >= 0),
--     purchase_date DATE NOT NULL,
--     PRIMARY KEY (user_id, game_id),
--     CONSTRAINT fk_user_games_users
--         FOREIGN KEY (user_id)
--         REFERENCES users(id)
--         ON DELETE CASCADE,
--     CONSTRAINT fk_user_games_games
--         FOREIGN KEY (game_id)
--         REFERENCES games(id)
--         ON DELETE CASCADE
-- );
-- CREATE TABLE reviews (
--     id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     user_id INT NOT NULL,
--     game_id INT NOT NULL,
--     rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
--     comment TEXT CHECK (LENGTH(comment) >= 5),
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     CONSTRAINT fk_reviews_users
--         FOREIGN KEY (user_id)
--         REFERENCES users(id)
--         ON DELETE CASCADE,
--     CONSTRAINT fk_reviews_games
--         FOREIGN KEY (game_id)
--         REFERENCES games(id)
--         ON DELETE CASCADE,
--     CONSTRAINT unique_user_game_review
--         UNIQUE (user_id, game_id)
-- );
-- INSERT INTO users (username, email, country) VALUES
-- ('Davit', 'davit@test.com', 'Belgium'),
-- ('Sarah', 'sarah@test.com', 'France'),
-- ('Lucas', 'lucas@test.com', 'Belgium'),
-- ('Emma', 'emma@test.com', 'Canada'),
-- ('Noah', 'noah@test.com', 'Germany'),
-- ('Lina', 'lina@test.com', 'Belgium'),
-- ('Tom', 'tom@test.com', 'USA'),
-- ('Julie', 'julie@test.com', 'France'),
-- ('Alex', 'alex@test.com', 'USA'),
-- ('Mike', 'mike@test.com', 'UK');
-- INSERT INTO profiles (user_id, bio, avatar_url, birth_date) VALUES
-- (1, 'Metalhead and Souls fan', 'avatar1.png', '2002-03-02'),
-- (2, 'Competitive FPS player', 'avatar2.png', '1998-07-10'),
-- (3, 'Indie games lover', 'avatar3.png', '2001-11-15'),
-- (4, 'Streamer and content creator', 'avatar4.png', '1999-01-20'),
-- (5, 'Hardcore RPG gamer', 'avatar5.png', '1995-05-05');
-- INSERT INTO publishers (name, country) VALUES
-- ('FromSoftware', 'Japan'),
-- ('CD Projekt', 'Poland'),
-- ('Valve', 'USA'),
-- ('Rockstar Games', 'USA'),
-- ('Riot Games', 'USA'),
-- ('Activision', 'USA'),
-- ('Naughty Dog', 'USA'),
-- ('Mojang', 'Sweden'),
-- ('Epic Games', 'USA');
-- INSERT INTO games (title, price, release_date, publisher_id) VALUES
-- ('Elden Ring', 59.99, '2022-02-25', 1),
-- ('Dark Souls 3', 39.99, '2016-04-12', 1),
-- ('Cyberpunk 2077', 49.99, '2020-12-10', 2),
-- ('Counter Strike 2', 0.00, '2023-09-27', 3),
-- ('GTA V', 29.99, '2013-09-17', 4),
-- ('League of Legends', 0.00, '2009-10-27', 5),
-- ('Call of Duty MW3', 79.99, '2023-11-10', 6),
-- ('The Last of Us', 69.99, '2022-09-02', 7),
-- ('Minecraft', 26.95, '2011-11-18', 8),
-- ('Fortnite', 0.00, '2017-07-21', 9),
-- ('Red Dead Redemption 2', 59.99, '2018-10-26', 4);
-- INSERT INTO user_games (user_id, game_id, hours_played, purchase_date) VALUES
-- (1, 1, 220, '2024-01-10'),
-- (1, 4, 450, '2023-11-01'),
-- (1, 5, 180, '2022-08-20'),
-- (2, 3, 95, '2024-03-15'),
-- (2, 6, 800, '2020-06-01'),
-- (2, 7, 120, '2024-01-20'),
-- (3, 2, 140, '2023-07-22'),
-- (3, 9, 300, '2022-12-05'),
-- (4, 8, 40, '2024-04-18'),
-- (4, 11, 110, '2024-01-03'),
-- (5, 1, 350, '2024-02-11'),
-- (5, 8, 70, '2024-03-10'),
-- (6, 10, 500, '2021-07-14'),
-- (6, 6, 1000, '2019-09-09'),
-- (7, 4, 1300, '2021-06-01'),
-- (8, 3, 35, '2024-05-02'),
-- (9, 5, 220, '2022-10-10'),
-- (10, 9, 600, '2020-05-05');
-- INSERT INTO reviews (user_id, game_id, rating, comment) VALUES
-- (1, 1, 5, 'Absolute masterpiece'),
-- (2, 6, 4, 'Still addictive after years'),
-- (3, 2, 5, 'Amazing boss fights'),
-- (4, 11, 5, 'Best story ever'),
-- (5, 1, 5, 'Fantastic exploration'),
-- (6, 10, 4, 'Very fun with friends'),
-- (7, 4, 5, 'Competitive and intense'),
-- (8, 3, 3, 'Good but buggy'),
-- (9, 5, 5, 'Classic game'),
-- (10, 9, 5, 'Infinite creativity');
 
-- INSERT INTO users (username, email, country) VALUES
-- ('Nina', 'nina@test.com', 'Belgium'),
-- ('Oscar', 'oscar@test.com', 'Spain'),
-- ('Yuki', 'yuki@test.com', 'Japan'),
-- ('Maya', 'maya@test.com', 'USA'),
-- ('Chris', 'chris@test.com', 'UK');
 
-- INSERT INTO profiles (user_id, bio, avatar_url, birth_date) VALUES
-- (11, NULL, NULL, '2000-06-12'),
-- (12, 'Casual gamer', NULL, '1997-09-30'),
-- (13, 'JRPG and Souls enjoyer', 'avatar13.png', '1996-02-14');
 
-- INSERT INTO publishers (name, country) VALUES
-- ('Ubisoft', 'France');
 
-- INSERT INTO games (title, price, release_date, publisher_id) VALUES
-- ('Bloodborne', 19.99, '2015-03-24', 1),
-- ('Sekiro', 59.99, '2019-03-22', 1),
-- ('Bully', 14.99, '2006-10-17', 4),
-- ('Valorant', 0.00, '2020-06-02', 5),
-- ('Warzone', 0.00, '2020-03-10', 6),
-- ('Uncharted 4', 39.99, '2016-05-10', 7),
-- ('Hades', 24.99, '2020-09-17', 3),
-- ('Portal 2', 9.99, '2011-04-19', 3);
 
-- INSERT INTO user_games (user_id, game_id, hours_played, purchase_date) VALUES
 
-- (1, 6, 120, '2020-01-12'),
-- (1, 7, 240, '2024-02-01'),
-- (1, 9, 90, '2021-04-10'),
-- (1, 12, 160, '2022-02-02'),
-- (1, 15, 80, '2023-04-04'),
 
-- (2, 4, 300, '2023-09-28'),
-- (2, 10, 900, '2018-08-08'),
-- (2, 15, 450, '2022-07-07'),
-- (2, 16, 700, '2021-02-02'),
 
-- (3, 4, 150, '2023-10-01'),
-- (3, 6, 500, '2020-03-03'),
-- (3, 10, 250, '2018-01-01'),
-- (3, 15, 200, '2021-01-01'),
-- (3, 16, 100, '2022-05-05'),
 
-- (4, 18, 60, '2020-11-11'),
 
-- (5, 12, 400, '2022-06-06'),
-- (5, 13, 180, '2023-03-03'),
 
-- (6, 4, 700, '2023-11-11'),
-- (6, 16, 350, '2022-10-10'),
-- (6, 17, 40, '2024-04-04'),
 
-- (7, 6, 1200, '2019-09-09'),
-- (7, 16, 850, '2020-04-04'),
 
-- (8, 11, 100, '2023-08-08'),
-- (8, 14, 40, '2023-01-01'),
 
-- (9, 1, 150, '2024-01-01'),
-- (9, 3, 90, '2024-02-02'),
-- (9, 4, 300, '2024-03-03'),
-- (9, 6, 600, '2024-04-04'),
-- (9, 7, 80, '2024-05-05'),
 
-- (12, 17, 25, '2024-06-06'),
 
-- (13, 1, 500, '2024-01-01'),
-- (13, 2, 350, '2024-01-02'),
-- (13, 12, 250, '2024-01-03'),
-- (13, 13, 300, '2024-01-04'),
 
-- (14, 5, 70, '2024-02-02'),
-- (14, 8, 30, '2024-03-03'),
 
-- (15, 18, 10, '2024-05-05');
 
-- INSERT INTO reviews (user_id, game_id, rating, comment) VALUES
-- (1, 7, 4, 'Fun but sweaty'),
-- (1, 9, 5, 'Blocky perfection'),
-- (2, 4, 5, 'Best competitive FPS'),
-- (2, 10, 4, 'Chaotic but fun'),
-- (3, 6, 4, 'Still toxic but addictive'),
-- (4, 18, 5, 'Beautiful adventure'),
-- (5, 12, 5, 'Gothic masterpiece'),
-- (5, 13, 5, 'Parry god simulator'),
-- (6, 17, 5, 'Insane roguelike'),
-- (7, 16, 4, 'Battle royale classic'),
-- (8, 14, 4, 'Old but gold'),
-- (9, 3, 4, 'Much better now'),
-- (9, 7, 2, 'Too expensive for what it is'),
-- (12, 17, 5, 'Perfect indie game'),
-- (13, 1, 5, 'Peak fantasy RPG'),
-- (14, 5, 5, 'Still iconic'),
-- (15, 6, 1, 'Not my thing');

-- SELECT * from users;

-- SELECT username, country FROM users

-- SELECT * from games

-- SELECT title, price from games

-- SELECT * from games WHERE price > 40

-- SELECT * from games WHERE price < 50

-- SELECT * from games WHERE price = 0

-- SELECT * from users WHERE country = 'Belgium'
-- SELECT * from users WHERE country <> 'Belgium'

-- SELECT * FROM publishers WHERE country = 'USA'

-- SELECT * FROM games WHERE release_date > '2020-12-31'
-- SELECT * FROM games WHERE release_date < '2021-01-01'

-- SELECT * FROM games ORDER BY price DESC
-- SELECT * FROM games ORDER BY release_date DESC

-- SELECT * FROM users ORDER BY username

-- SELECT * FROM games WHERE title LIKE '%Dark%'
-- SELECT * FROM games WHERE title LIKE 'C%'

-- SELECT * FROM games WHERE title LIKE '%Dark%'

-- SELECT * FROM users WHERE username LIKE '%a%'

-- SELECT * FROM reviews WHERE rating = 5

-- SELECT * FROM reviews WHERE created_at > '2024-01-01'

-- SELECT * FROM games WHERE price BETWEEN 20 AND 60

-- SELECT * FROM users WHERE country = 'Belgium' or country = 'France'

-- SELECT * FROM games WHERE price != 0

-- SELECT * FROM games ORDER BY title

-- SELECT * FROM publishers ORDER BY name

-- SELECT * FROM games WHERE title LIKE '%2'

-- SELECT * FROM users WHERE created_at > '2022-01-01'

-- SELECT * FROM games WHERE release_date BETWEEN '2014-12-31' AND '2022-01-01'

-- SELECT * FROM reviews WHERE comment ILIKE '%best%'

-- SELECT * FROM games WHERE price = 59.99
--########################################################

-- SELECT UPPER(username), LENGTH(username) FROM users

-- SELECT title, TO_CHAR(release_date, 'YYYY') FROM games

-- SELECT COALESCE(bio, 'No bio yet') as bio FROM profiles

-- SELECT title,
-- CASE 
-- 	WHEN price > 0 THEN 'Paid'
-- 	ELSE 'Free'
-- END as price_label
-- FROM games

-- SELECT count(*) FROM users
-- SELECT count(*) FROM games
-- SELECT AVG(price)::decimal(10, 2) FROM games

-- SELECT SUM(hours_played) from user_games

-- SELECT MIN(rating), MAX(rating) FROM reviews

-- SELECT COUNT(*), country FROM users
-- GROUP BY country

-- SELECT COUNT(*), publisher_id FROM games
-- GROUP BY publisher_id

-- SELECT AVG(price)::decimal(10,2), publisher_id FROM games
-- GROUP BY publisher_id;

-- SELECT SUM(hours_played), user_id FROM user_games
-- GROUP BY user_id

SELECT AVG(hours_played)::decimal(10,2), user_id FROM user_games
GROUP BY user_id


-- SELECT SUM(hours_played), game_id FROM user_games
-- GROUP BY game_id

-- SELECT COUNT(*), TO_CHAR(purchase_date, 'YYYY') FROM user_games
-- GROUP BY TO_CHAR(purchase_date, 'YYYY')

-- SELECT COUNT(*), TO_CHAR(release_date, 'YYYY') FROM games
-- GROUP BY TO_CHAR(release_date, 'YYYY')
-- ORDER BY TO_CHAR(release_date, 'YYYY')

-- SELECT COUNT(*),  
-- CASE 
-- 	WHEN price = 0 THEN 'Free'
-- 	WHEN price < 30 THEN 'Cheap'
-- 	WHEN price BETWEEN 30 AND 60 THEN 'Standard'
-- 	WHEN price > 60 THEN 'Expensive' -->aurait pu mettre else pour la fin
-- END AS "Price category"
-- FROM games
-- GROUP BY "Price category"

-- SELECT COUNT(*), publisher_id FROM games
-- WHERE price > 0
-- GROUP BY publisher_id


-- SELECT AVG(price)::decimal(10,2), publisher_id FROM games
-- WHERE release_date > '2015-01-01'
-- GROUP BY publisher_id

-- SELECT country, count(*) FROM users
-- GROUP BY country
-- HAVING count(*) > 1

-- SELECT user_id, SUM(hours_played) FROM user_games
-- GROUP BY user_id
-- HAVING SUM(hours_played) > 300

-- SELECT game_id, AVG(rating)::decimal(10,2) FROM reviews
-- GROUP BY game_id
-- HAVING AVG(rating) >= 4.5
--###################################################---
--1
-- SELECT g.title, p.name FROM games g
-- JOIN publishers p 
-- ON g.publisher_id = p.id

-- SELECT u.username, p.bio FROM users u
-- JOIN profiles p
-- ON u.id = p.user_id
--3
-- SELECT u.username, g.title, ug.hours_played FROM user_games ug
-- JOIN users u ON u.id = ug.user_id
-- JOIN games g ON g.id = ug.game_id

-- SELECT u.username, g.title, r.rating, r.comment FROM reviews r
-- JOIN users u ON u.id = r.user_id
-- JOIN games g ON g.id = r.game_id
--5
-- SELECT u.username, g.title, ug.purchase_date FROM user_games ug
-- JOIN users u ON u.id = ug.user_id
-- JOIN games g ON g.id = ug.game_id

-- SELECT u.username, p.bio FROM users u
-- LEFT JOIN profiles p
-- ON u.id = p.user_id
--7
-- SELECT g.title, r.comment, r.rating FROM games g
-- LEFT JOIN reviews r 
-- ON g.id = r.game_id


-- SELECT p.name, g.title FROM publishers p
-- LEFT JOIN games g 
-- ON g.publisher_id = p.id

-- SELECT u.username, ug.purchase_date FROM users u
-- LEFT JOIN user_games ug ON u.id = ug.game_id
-- WHERE u.id NOT IN (ug.game_id)
--9
-- SELECT u.username, ug.purchase_date FROM users u
-- LEFT JOIN user_games ug ON u.id = ug.user_id
-- WHERE ug.user_id IS NULL
-- 10
-- SELECT * FROM games g 
-- LEFT JOIN user_games ug ON g.id = ug.game_id
-- WHERE ug.game_id IS NULL
--###########################################################################
--11
-- SELECT g.id, g.title, COUNT(u.id) as total_player FROM user_games ug
-- LEFT JOIN users u ON ug.user_id = u.id
-- LEFT JOIN games g ON g.id = ug.game_id
-- GROUP BY g.title, g.id

-- SELECT g.title, AVG(r.rating)::decimal(10, 1) FROM games g
-- LEFT JOIN reviews r ON r.game_id = g.id
-- GROUP BY g.title
--13
-- SELECT g.title, SUM(ug.hours_played) FROM games g
-- LEFT JOIN user_games ug ON ug.game_id = g.id
-- GROUP BY g.title

-- SELECT u.id, u.username, COUNT(*) FROM users u
-- LEFT JOIN user_games ug ON ug.user_id = u.id
-- GROUP BY u.username, u.id
--15
-- SELECT p.name, AVG(g.price)::decimal(10,2) FROM publishers p
-- LEFT JOIN games g ON g.publisher_id = p.id
-- GROUP BY p.name


-- SELECT u.username, COUNT(ug.user_id) AS "number of owned games", SUM(ug.hours_played) as "total hours played" FROM users u
-- LEFT JOIN user_games ug ON ug.user_id = u.id
-- GROUP BY u.username
--########################""----
--17
-- SELECT u.username, COUNT(ug.user_id) AS "number of owned games" 
-- FROM users u
-- LEFT JOIN user_games ug ON ug.user_id = u.id
-- GROUP BY u.username
-- HAVING COUNT(ug.user_id) > 2

-- SELECT p.name, COUNT(g.title) FROM publishers p
-- LEFT JOIN games g 
-- ON g.publisher_id = p.id
-- GROUP BY p.name
-- HAVING COUNT(g.title) > 1
--19
-- SELECT g.title, AVG(r.rating)::decimal(10, 1) FROM games g
-- LEFT JOIN reviews r ON r.game_id = g.id
-- GROUP BY g.title
-- HAVING AVG(r.rating) > 4

-- 19

-- SELECT g.title, AVG(r.rating) FROM reviews r
-- JOIN games g ON g.id = r.game_id
-- GROUP BY g.title
-- HAVING AVG(r.rating) > 4


-- SELECT u.username, COUNT(r.comment) FROM reviews r
-- JOIN users u ON u.id = r.user_id
-- GROUP BY u.username
-- HAVING COUNT(r.comment) > 1

-- SELECT g.title, SUM(ug.hours_played) FROM user_games ug
-- JOIN games g ON g.id = ug.game_id
-- GROUP BY g.title
-- HAVING SUM(ug.hours_played) > 500
--###########################################"-----"
-- SELECT u.username, SUM(ug.hours_played) FROM users u
-- JOIN user_games ug ON ug.user_id = u.id
-- GROUP BY u.username
-- ORDER BY SUM(ug.hours_played) DESC
-- LIMIT 3

-- SELECT g.title, SUM(ug.hours_played) FROM games g
-- JOIN user_games ug ON g.id = ug.game_id
-- GROUP BY g.title
-- ORDER BY SUM(ug.hours_played) DESC

-- SELECT g.title, SUM(ug.hours_played) FROM games g
-- JOIN user_games ug ON g.id = ug.game_id
-- GROUP BY g.title
-- ORDER BY SUM(ug.hours_played) DESC
-- LIMIT 5

----############################################""""""""""""
-- 26 ---> piège pas moyen -> faudrait 2 requetes
-- SELECT g.title, p.name, COUNT(ug.user_id), SUM(ug.hours_played), AVG(r.rating)::decimal(10,2) 
-- FROM games g
-- LEFT JOIN user_games ug ON ug.game_id = g.id
-- LEFT JOIN reviews r ON r.game_id = g.id
-- LEFT JOIN publishers p ON p.id = g.publisher_id
-- GROUP BY g.title, p.name
-- 27
-- SELECT u.username, COUNT(DISTINCT ug.game_id), COUNT(DISTINCT r.id) FROM users u
-- LEFT JOIN user_games ug ON ug.user_id = u.id
-- LEFT JOIN reviews r ON r.user_id = u.id
-- GROUP BY u.username

-- 28
-- SELECT p.name, COUNT(DISTINCT g.id), AVG(g.price)::decimal(10,2), SUM(ug.hours_played) FROM publishers p
-- LEFT JOIN games g ON g.publisher_id = p.id
-- LEFT JOIN user_games ug ON ug.game_id = g.id
-- GROUP BY p.name

-- SELECT g.title, g.publisher_id, p.name FROM games g
-- JOIN publishers p ON p.id = g.publisher_id 
--29
-- SELECT g.title, p.name, COUNT(DISTINCT r.id), AVG(r.rating)::decimal(5,1) FROM games g
-- LEFT JOIN publishers p ON g.publisher_id = p.id
-- LEFT JOIN reviews r ON r.game_id = g.id
-- GROUP BY g.title, p.name
-- ORDER BY AVG(r.rating) DESC;
-- 30
-- SELECT p.name, SUM(ug.hours_played) FROM publishers p
-- LEFT JOIN games g ON g.publisher_id = p.id
-- JOIN user_games ug ON g.id = ug.game_id
-- GROUP BY p.name
-- ORDER BY SUM(ug.hours_played) DESC

-- SELECT g.title, r.rating FROM games g
-- LEFT JOIN reviews r ON r.game_id = g.id


