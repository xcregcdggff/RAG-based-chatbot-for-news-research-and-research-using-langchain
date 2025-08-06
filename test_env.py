import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

print("🟢 NEWS_API_KEY:", os.getenv("NEWS_API_KEY"))
print("🟢 OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
