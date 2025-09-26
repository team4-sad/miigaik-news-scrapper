import uuid

from src.file_output import FileOutput
from src.parser import Parser
from src.web_input import WebInput

inp = WebInput(base_url="https://www.miigaik.ru/about/news")
out = FileOutput(f"../output/{uuid.uuid4().hex}.json")
parser = Parser(inp=inp, out=out)
with out:
    parser.parse_news()
print("Завершение...")
