SELECT albumid, COUNT(Trackid) AS cnt FROM tracks
GROUP BY albumid
ORDER BY cnt DESC;