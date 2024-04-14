import os
import sys
from dotenv import load_dotenv

is_load_env = load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

if not is_load_env:
    print("[ERROR] .env file does not exist. Please create .env file at root of backend in order to use MYSQL. .env cannot be empty either")
    sys.exit(1)

config_env = {
    "MYSQL_USERNAME": os.getenv('MYSQL_USERNAME'),
    "MYSQL_PASSWORD":  os.getenv('MYSQL_PASSWORD'),
    "MYSQL_HOST": os.getenv('MYSQL_HOST'),
    "MYSQL_DATABASE": os.getenv('MYSQL_DATABASE')
}