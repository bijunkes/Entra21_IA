from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING_NEON = os.getenv('NEON_DB_STRING')

engine = create_engine(CONNECTION_STRING_NEON)