import pandas as pd  
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE = os.getenv("DATABASE_CONN")
engine = create_engine(DATABASE)
        
df = pd.read_csv("Tamil_movies_dataset.csv")
df.to_sql("Dataset",engine,if_exists="replace", index=False)

print("Dataset Loaded")