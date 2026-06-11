 -- SELECT * FROM users
-- -- SELECT * FROM profiles
-- -- SELECT * FROM games
-- -- SELECT * FROM user_games
-- -- SELECT * FROM publishers
-- -- SELECT * FROM reviews

-- 1.
-- Display all games that cost more than the average game price.
-- SELECT * 
-- FROM games
-- WHERE price > (
-- 	SELECT AVG(price) 
-- 	FROM games
-- 	)

-- 2.
-- Display all users who played more hours than the average hours played.
-- SELECT u.username, SUM(ug.hours_played) as somme FROM users u
-- LEFT JOIN user_games ug ON ug.user_id = u.id
-- GROUP BY u.username
-- HAVING SUM(ug.hours_played) > (
-- 	SELECT AVG(somme)
-- 	FROM (
-- 		SELECT SUM(hours_played) as somme
-- 		FROM user_games
-- 		GROUP BY user_id
-- 		)
-- )
-- ORDER BY somme

-- SELECT AVG(somme)
-- FROM (
-- 	SELECT SUM(hours_played) as somme
-- 	FROM user_games
-- 	GROUP BY user_id
-- 	)
	
-- SELECT SUM(hours_played) as somme
-- 	FROM user_games
-- 	GROUP BY user_id
	
-- 3.
-- Display all games that have at least one review.

-- SELECT * 
-- FROM games g
-- WHERE g.id IN (
-- 	SELECT r.game_id FROM reviews r
-- 	GROUP BY r.game_id
-- 	HAVING COUNT(*) >= 1
-- )

-- SOLUTION_ Maxim
-- SELECT g.*
-- FROM games g
-- WHERE EXISTS (SELECT 1 
-- 			  FROM reviews r
-- 			  WHERE r.game_id = g.id
-- 			 )

-- SELECT r.game_id FROM reviews r
-- GROUP BY r.game_id
-- HAVING COUNT(*) >= 1

-- 4.
-- Display all games that were never reviewed.
-- SELECT * 
-- FROM games g
-- WHERE g.id NOT IN (
-- 	SELECT r.game_id FROM reviews r
-- 	GROUP BY r.game_id
-- 	HAVING COUNT(*) >= 1
-- )

-- 5.
-- Display all users who bought at least one game.
-- SELECT * FROM users
-- WHERE id IN(
-- 	SELECT user_id FROM user_games
-- 	GROUP BY user_id
-- )
-- 6.
-- Display all users who never bought a game.
-- SELECT * FROM users
-- WHERE id NOT IN(
-- 	SELECT user_id FROM user_games
-- 	GROUP BY user_id
-- )

-- 7.
-- Display all games whose price is equal to the maximum game price.
-- SELECT * FROM games
-- WHERE price =(
-- 	SELECT MAX(g.price) 
-- 	FROM games g
-- )

-- 8.
-- Display all publishers that published at least one free game.
-- SELECT * FROM publishers
-- WHERE id IN(
-- 	SELECT g.publisher_id FROM games g
-- 	WHERE g.price = 0
-- 	GROUP BY g.publisher_id
-- )

-- 9.
-- Display all users who own at least one game from Rockstar Games.
-- SELECT u.* FROM users u
-- LEFT JOIN user_games ug ON u.id = ug.user_id
-- WHERE ug.game_id IN (
-- 	SELECT g.id 
-- 	FROM games g
-- 	WHERE g.publisher_id = ( 
-- 		SELECT p.id 
-- 		FROM publishers p 
-- 		WHERE p.name = 'Rockstar Games')
-- 	)
-- GROUP BY u.id
--Solution avec exis
-- SELECT u.*
-- FROM users u
-- WHERE EXISTS (SELECT 1
-- 				FROM user_games ug
-- 				JOIN games g ON g.id = ug.game_id
-- 				JOIN publishers p ON p.id = g.publisher_id
-- 				WHERE ug.user_id = u.id AND p.name = 'Rockstar Games'
-- 				)


-- 10.
-- Display all users who reviewed a game they do NOT own.
-- SELECT u.* FROM users u
-- LEFT JOIN reviews r ON r.user_id = u.id
-- WHERE u.id NOT IN (
-- 	SELECT ug.user_id FROM user_games ug
-- 	WHERE r.game_id = ug.game_id
-- ) AND r.user_id IS NOT NULL

-- SELECT u.*
-- FROM users u
-- JOIN reviews r ON r.user_id = u.id
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM user_games ug
--     WHERE ug.user_id = r.user_id
--       AND ug.game_id = r.game_id
-- );


-- SELECT * FROM users u
-- WHERE u.id IN (SELECT r.user_id FROM reviews r
-- 	WHERE r.game_id NOT IN (SELECT ug.game_id FROM user_games ug
-- 		WHERE ug.user_id = u.id))
		
 -- SELECT * FROM reviews

-- 11. Tention pas sûr
-- Using a CTE, display the top 3 users with the most total hours played.
-- SELECT u.username, SUM(u_g.hours_played) FROM users u
-- LEFT JOIN user_games u_g ON u.id = u_g.user_id
-- WHERE u.id IN (
-- 	SELECT ug.user_id FROM user_games ug
-- 	GROUP BY ug.user_id
-- 	ORDER BY SUM(ug.hours_played) DESC
-- 	LIMIT 3
-- 	)
-- GROUP BY u.username
-- ORDER BY SUM(u_g.hours_played) DESC

-- 12.
-- Using a CTE, display:
-- publisher name
-- total games
-- average price for publishers having more than 1 game.
-- SELECT * FROM publishers
-- WHERE id IN(
-- 	SELECT g.publisher_id FROM games g
-- 	GROUP BY g.publisher_id
-- 	HAVING COUNT(g.publisher_id) > 1	
-- )

-- SELECT p.name, ttemp."Total" as "Total" , ttemp."Price" as "Price" 
-- FROM 
-- 	(SELECT g.publisher_id, COUNT(g.publisher_id) as "Total" , AVG(g.price) as "Price" 
-- 	FROM games g
-- 	GROUP BY g.publisher_id
-- 	HAVING COUNT(g.publisher_id) > 1) AS ttemp
-- LEFT JOIN publishers p ON p.id = ttemp.publisher_id



-- 13.
-- Using CTEs, correctly display:

-- game title
-- publisher name
-- total players
-- total hours played
-- average rating
-- SELECT g.title, p.name FROM games g
-- LEFT JOIN publishers p ON p.id = g.publisher_id

-- SELECT g.title, p.name, 
-- COUNT(DISTINCT ug.user_id) AS "Total player", 
-- SUM(ug.hours_played) AS "Hours Played", 
-- ttemp."Rating"
-- FROM
-- (
-- 	SELECT AVG(r.rating) as "Rating", r.game_id
-- 	FROM reviews r
-- 	GROUP BY r.game_id
-- ) AS ttemp
-- LEFT JOIN user_games ug ON ug.game_id = ttemp.game_id
-- RIGHT JOIN games g ON g.id = ttemp.game_id
-- LEFT JOIN publishers p ON p.id = g.publisher_id
-- GROUP BY g.title, ttemp."Rating", p.name

-- WITH player_stats AS (
--     SELECT
--         game_id,
--         COUNT(user_id) AS total_players,
--         SUM(hours_played) AS total_hours_played
--     FROM user_games
--     GROUP BY game_id
-- ),
-- rating_stats AS (
--     SELECT
--         game_id,
--         AVG(rating) AS average_rating
--     FROM reviews
--     GROUP BY game_id
-- )
-- SELECT
--     g.title AS game_title,
--     p.name AS publisher_name,
--     COALESCE(ps.total_players, 0) AS total_players,
--     COALESCE(ps.total_hours_played, 0) AS total_hours_played,
--     rs.average_rating
-- FROM games g
-- JOIN publishers p ON p.id = g.publisher_id
-- LEFT JOIN player_stats ps ON ps.game_id = g.id
-- LEFT JOIN rating_stats rs ON rs.game_id = g.id;

-- 14.
-- Using CTEs, correctly display:

-- publisher name
-- total games
-- average game price
-- total hours played on their games

-- SELECT p.name FROM publishers p
-- SELECT * FROM games g
-- SELECT p.name, ttemp."Total", ttemp."Average"--, ttemp."Somme"
-- FROM(
-- 	SELECT COUNT(g.publisher_id) AS "Total", 
-- 	g.publisher_id, 
-- 	AVG(g.price)::decimal(10,2) AS "Average"--,
-- 	--SUM(ug.hours_played) AS "Somme"
-- 	FROM games g 
-- 	--LEFT JOIN user_games ug ON ug.game_id = g.id
-- 	GROUP BY g.publisher_id
-- ) as ttemp
-- LEFT JOIN publishers p ON p.id = ttemp.publisher_id
-- SELECT SUM(ug.hours_played) FROM user_games ug
-- GROUP BY ug.game_id

WITH publishers_stats
AS (SELECT p.id, p.name, COUNT(g.id) AS total_games, COALESCE(AVG(g.price)::numeric(10,2), 0) AS average_game_price
  FROM publishers p
  LEFT JOIN games g ON g.publisher_id = p.id
  GROUP BY p.id, p.name
    ),
games_stats AS (
  SELECT g.publisher_id, SUM(ug.hours_played) AS total_hours_per_publisher
  FROM games g
  LEFT JOIN user_games ug ON ug.game_id = g.id
  GROUP BY g.publisher_id
  )
SELECT ps.name,
     ps.total_games,
     ps.average_game_price,
     COALESCE(gs.total_hours_per_publisher, 0)
FROM publishers_stats ps
LEFT JOIN games_stats gs ON gs.publisher_id = ps.id

-- 15.
-- Display all games that are more expensive than the average price of their publisher.
-- SELECT g.* FROM games g
-- WHERE g.price > (
-- 	SELECT AVG(g2.price) FROM games g2
-- 	LEFT JOIN publishers p ON p.id = g.publisher_id
-- )
-- SELECT g.*, ttemp.name FROM (
-- 	SELECT AVG(g2.price) as "Average", g2.publisher_id, p.name FROM games g2
-- 	LEFT JOIN publishers p ON p.id = g2.publisher_id
-- 	GROUP BY g2.publisher_id, p.name
-- 	) 
-- AS ttemp
-- LEFT JOIN games g ON g.publisher_id = ttemp.publisher_id
-- WHERE g.price > ttemp."Average"




