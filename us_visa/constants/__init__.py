# This File defines all the conatants 

# defining data base constansts

DATABASE_NAME = "US_VISA"     # Data base name in mongo db 

COLLECTION_NAME = "visa_data"     #    Collection name is data base 

MONGODB_URL_KEY = "MONGODB_URL"       # Mongo db URL




"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"   # Feature store folder inside artifacts folder   to hold raw data before train test split 
DATA_INGESTION_INGESTED_DIR: str = "ingested"      # ingested folder inside artifact folder responsible to hold train and test data 
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2    # Train test ratio 
