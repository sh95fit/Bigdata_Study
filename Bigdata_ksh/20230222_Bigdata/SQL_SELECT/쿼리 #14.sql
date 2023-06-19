SELECT tracks.genreid, genres.Name, count(tracks.genreid) AS track_num FROM tracks 
JOIN genres ON genres.GenreId=tracks.genreid
GROUP BY tracks.genreid
ORDER BY track_num DESC
LIMIT 10;