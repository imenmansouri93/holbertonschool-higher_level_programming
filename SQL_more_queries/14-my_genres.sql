-- lists all shows contained in hbtn_0d_tvshows 
SELECT tv_genres.name
FROM tv_shows
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE  tv_shows.title = "Dexter"
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_genres.name DESC;