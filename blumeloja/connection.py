from psycopg2 import connect
import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING_NEON = os.getenv('NEON_DB_STRING')

conn = connect(CONNECTION_STRING_NEON)