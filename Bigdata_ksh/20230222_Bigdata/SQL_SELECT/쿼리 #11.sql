SELECT Country, COUNT(Country) AS cnt FROM customers
GROUP BY Country
ORDER BY cnt DESC
LIMIT 5;