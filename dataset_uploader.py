import pandas as pd  
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Gokul%400508@localhost:5432/Kollywood_Movies_2011-19')
        
df = pd.read_csv("Tamil_movies_dataset.csv")
df.to_sql("Dataset",engine,if_exists="replace", index=False)

print("Dataset Loaded")