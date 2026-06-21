import pandas as pd  
from sqlalchemy import create_engine
import os

DATABASE_URL= os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
        
df = pd.read_csv("Tamil_movies_dataset.csv")
df.to_sql("Dataset",engine,if_exists="replace", index=False)

print("Dataset Loaded")