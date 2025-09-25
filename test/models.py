from src.models import LLM
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    llm = LLM(model=r'models/gemini-2.5-flash-lite-preview-06-17')
    res = llm.singleChat("Hello")
    print(res)