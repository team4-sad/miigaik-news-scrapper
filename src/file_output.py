import dataclasses
import json
import os
from io import TextIOWrapper

from src.base_output import BaseOutput
from src.news_model import NewsModel


class FileOutput(BaseOutput):
    def __init__(self, path: str):
        self._file: TextIOWrapper | None = None
        self._path = path

    @property
    def is_opened(self):
        return self._file is not None

    def open(self):
        if self._file is not None:
            raise OSError("File already opened")
        if not os.path.exists(self._path):
            open(self._path, "w").close()
        self._file = open(self._path, "w+", encoding="utf-8")

    def close(self):
        if self._file is None:
            raise OSError("File not opened")
        self._file.close()
        self._file = None

    def save_one(self, news: NewsModel):
        if self._file is None:
            raise OSError("File not opened")
        lst = self._read()
        obj_dict = dataclasses.asdict(news)
        lst.append(obj_dict)
        self._save(lst)

    def save_many(self, news: list[NewsModel]):
        if self._file is None:
            raise OSError("File not opened")
        lst = self._read()
        objects_dict = [dataclasses.asdict(item) for item in news]
        lst.extend(objects_dict)
        self._save(lst)

    def _read(self):
        row_json = self._file.read()
        if row_json != "":
            lst = json.loads(row_json)
        else:
            lst = []
        return lst

    def _save(self, obj):
        self._file.seek(0)
        self._file.truncate(0)
        json.dump(obj, self._file, ensure_ascii=False)
        self._file.flush()
        self._file.seek(0)

    def __enter__(self):
        self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
