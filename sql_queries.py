# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
    user_ID        VARCHAR(50)     NOT NULL                       PRIMARY KEY,
    first_name     VARCHAR(80)                                               ,
    last_name      VARCHAR(80)                                               ,
    gender         VARCHAR(1)                                                ,
    level          VARCHAR(10)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
    song_ID     VARCHAR(50)        NOT NULL                       PRIMARY KEY,
    title       VARCHAR(255)                                                 ,
    artist_ID   VARCHAR(50)        NOT NULL                                  ,
    year        INTEGER                                                      ,
    duration    FLOAT
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
    artist_ID   VARCHAR(50)        NOT NULL                       PRIMARY KEY ,
    name        VARCHAR(255)                                                  ,
    location    VARCHAR(255)                                                  ,
    latitude    FLOAT                                                         ,
    longitude   FLOAT
    );
""")


time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
    start_time  TIMESTAMP          NOT NULL                       PRIMARY KEY ,
    hour        SMALLINT,
    day         SMALLINT,
    week        SMALLINT,
    month       SMALLINT,
    year        SMALLINT,
    weekday     SMALLINT
    );
""")

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
    songplay_ID    SERIAL                NOT NULL                 PRIMARY KEY  ,
    start_time     TIMESTAMP             REFERENCES time(start_time)           ,
    user_ID        VARCHAR(50)           REFERENCES users(user_ID)             ,
    level          VARCHAR(10)                                                 ,
    song_ID        VARCHAR(50)           REFERENCES songs(song_ID)             ,
    artist_ID      VARCHAR(50)           REFERENCES artists(artist_ID)         ,
    session_ID     INTEGER                                                     ,
    location       VARCHAR(255)                                                ,
    user_agent     VARCHAR(255)
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
    start_time
    ,user_ID
    ,level
    ,song_ID
    ,artist_ID
    ,session_ID
    ,location
    ,user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO users (
    user_ID
    ,first_name
    ,last_name
    ,gender
    ,level
) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_ID) DO UPDATE SET level=excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs (
    song_ID
    ,title
    ,artist_ID
    ,year
    ,duration
) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_ID) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (
    artist_ID
    ,name
    ,location
    ,latitude
    ,longitude
) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_ID) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (
    start_time
    ,hour
    ,day
    ,week
    ,month
    ,year
    ,weekday
) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT 
    s.song_ID
    ,a.artist_ID
FROM
    songs s 
    JOIN artists a ON s.artist_ID = a.artist_ID
WHERE
    s.title = %s
    AND a.name = %s
    AND s.duration = %s
GROUP BY
    s.song_ID
    ,a.artist_ID
;
""")
# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]