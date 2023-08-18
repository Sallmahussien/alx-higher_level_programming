-- Lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT ts.title
FROM
  tv_show_genres AS tsg
  INNER JOIN tv_shows AS ts
  ON tsg.show_id = ts.id
  INNER JOIN tv_genres AS tg
  ON tsg.genre_id = tg.id WHERE tg.name = "Comedy"
  ORDER BY ts.title ASC;
