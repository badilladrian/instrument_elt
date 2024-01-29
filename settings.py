import os

# Define default values
DATE_FORMAT = "%d-%b-%Y"
MAX_DATE = "19-12-2014"
INPUT_CSV_FILE_PATH = "sample_data.csv"
OUTPUT_CSV_RESULT_FILE = "output.csv"

# Environment variables to customize the pipeline
DATE_FORMAT = os.environ.get("DATE_FORMAT", DATE_FORMAT)
INPUT_CSV_FILE_PATH = os.environ.get("INPUT_CSV_FILE_PATH", INPUT_CSV_FILE_PATH)
OUTPUT_CSV_RESULT_FILE = os.environ.get(
    "OUTPUT_CSV_RESULT_FILE", OUTPUT_CSV_RESULT_FILE
)
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 1000))
POOL_SIZE = int(os.environ.get("POOL_SIZE", 5))
LOGGER_LEVEL = os.environ.get("LOGGER_LEVEL", "INFO")


# Database configuration
DATABASE_USER = os.environ.get("DATABASE_USER", "your_username")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "your_password")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "your_database")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PORT = int(os.environ.get("DATABASE_PORT", 5432))

DATABASE_CONFIG = {
    "user": DATABASE_USER,
    "password": DATABASE_PASSWORD,
    "database": DATABASE_NAME,
    "host": DATABASE_HOST,
    "port": DATABASE_PORT,
}
