import pandas as pd
from sqlalchemy import create_engine


conn = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/webscap')
df = pd.read_csv("dbs.csv")

df.to_sql(
    "Vacancy",
    conn,
    if_exists="append",
    index=False
)
