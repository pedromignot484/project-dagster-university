import duckdb
conn = duckdb.connect(database="data/staging/data.duckdb") # assumes you're writing to the same destination as specified in .env.example
conn.execute("select count(*) from trips").fetchall()