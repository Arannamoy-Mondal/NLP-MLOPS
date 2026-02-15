import os
import dotenv

dotenv.load_dotenv()


print(os.getenv('LANGCHAIN_PROJECT'))
print(os.getenv('LANGCHAIN_API_KEY'))