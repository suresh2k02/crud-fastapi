from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://camilo0119:6604107@localhost:3306/fastapi")
connection = engine.connect()
meta = MetaData()