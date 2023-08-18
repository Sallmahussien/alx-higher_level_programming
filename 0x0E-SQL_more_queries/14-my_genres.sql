-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tg.name
FROM tv_show_genres AS tsg
  INNER JOIN tv_genres AS tg
  ON tsg.genre_id = tg.id
  INNER JOIN tv_shows AS ts
  ON tsg.show_id = ts.id WHERE ts.title = "Dexter"
  ORDER BY tg.name ASC;
