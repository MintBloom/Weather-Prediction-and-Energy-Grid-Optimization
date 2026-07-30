import pandas as pd
from sqlalchemy import create_engine 
from DataGatherandExport import convert_to_csv

def QueryToPostgresql(username, password, host, port, database_name, ):

    # username =   your username 
    # password =    password created during installation
    # host =       host name/address
    # port =       port number
    # database_name = "Weather and Energy Database" database name
    # df = dataframe to be exported

    
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database_name}") 
    
    df = pd.read_sql(f"""SELECT d.datetime, d."ND", d."TSD", d."EMBEDDED_SOLAR_GENERATION", d."EMBEDDED_WIND_GENERATION",
                        w.temperature_2m, w.cloudcover, w.shortwave_radiation
                        FROM energy_demand_data d
                        INNER JOIN history_weather_data w ON d.datetime = w.datetime; """, 
                        con=engine)

    convert_to_csv(df, 'energy-demand-data\\' + "datetime_join.csv")

    print("Data exported to PostgreSQL database successfully.")

if __name__ == "__main__":
    QueryToPostgresql("postgres", "#76h25T", "localhost", "5432", "Weather and Energy Database", )