SELECT tracks.albumid, albums.title, COUNT(tracks.Trackid) AS cnt FROM tracks
JOIN albums ON albums.albumid=tracks.albumid
GROUP BY tracks.albumid
ORDER BY tracks.albumid;