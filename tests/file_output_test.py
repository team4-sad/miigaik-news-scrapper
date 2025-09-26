import dataclasses
import json
import os
import unittest

from src.file_output import FileOutput
from src.news_model import NewsModel
from tests.mock.mock_news_model import MockNewsModel


class FileOutputTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.test_output_path = "./tests/output.json"
        self.news_model: NewsModel = MockNewsModel()
        self.output = FileOutput(self.test_output_path)

    def tearDown(self):
        if self.output.is_opened:
            self.output.close()
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def read_path(self):
        with open(self.test_output_path, "r", encoding="utf-8") as file:
            return file.read()

    def assertContent(self, count: int = 1):
        saved_content = self.read_path()
        eq_lst = [dataclasses.asdict(self.news_model) for _ in range(count)]
        json_str = json.dumps(eq_lst)
        self.assertEqual(saved_content, json_str)

    def test_fail_save_one(self):
        with self.assertRaises(OSError):
            self.output.save_one(self.news_model)
    
    def test_fail_save_many(self):
        with self.assertRaises(OSError):
            self.output.save_many([self.news_model])

    def test_save_one(self):
        self.output.open()
        self.output.save_one(self.news_model)
        self.output.close()
        self.assertContent()

    def test_save_one_append(self):
        self.output.open()
        self.output.save_one(self.news_model)
        self.output.save_one(self.news_model)
        self.output.close()
        self.assertContent(count=2)

    def test_save_many(self):
        self.output.open()
        self.output.save_many([self.news_model, self.news_model])
        self.output.close()
        self.assertContent(count=2)

    def test_save_many_append(self):
        self.output.open()
        self.output.save_many([self.news_model, self.news_model])
        self.output.save_many([self.news_model, self.news_model])
        self.output.close()
        self.assertContent(count=4)

    def test_save_one_context_manager(self):
        with self.output:
            self.output.save_one(self.news_model)
        self.assertContent()

    def test_fail_double_open(self):
        with self.assertRaises(OSError):
            self.output.open()
            self.output.open()

    def test_fail_close(self):
        with self.assertRaises(OSError):
            self.output.close()

    def test_check_file_opened(self):
        self.assertFalse(self.output.is_opened)
        self.output.open()
        self.assertTrue(self.output.is_opened)
        self.output.close()
        self.assertFalse(self.output.is_opened)

    def test_check_file_opened_context_manager(self):
        self.assertFalse(self.output.is_opened)
        with self.output:
            self.assertTrue(self.output.is_opened)
        self.assertFalse(self.output.is_opened)
