import unittest

from bs4 import BeautifulSoup

from src.web_input import WebInput


class WebInputTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.base_url = 'https://www.miigaik.ru/about/news'
        self.test_id_page = 6583
        self.input = WebInput(self.base_url)

    def test_get_init_first_page(self):
        curr_page = self.input.page
        self.assertEqual(curr_page, 1)

    def test_get_next_page(self):
        self.input.next_page()
        curr_page = self.input.page
        self.assertEqual(curr_page, 2)

    def test_generate_correct_url(self):
        curr_url = self.input.url
        self.assertEqual(curr_url, f'{self.base_url}?PAGEN_2=1')
        self.input.next_page()
        curr_url = self.input.url
        self.assertEqual(curr_url, f'{self.base_url}?PAGEN_2=2')

    def test_fetch(self):
        html = self.input.fetch()
        self.assertIsInstance(html, str)
        is_html = bool(BeautifulSoup(html, "html.parser").find())
        self.assertTrue(is_html)

    def test_fail_fetch_page(self):
        with self.assertRaises(ValueError):
            _ = self.input.fetch_page()

    def test_fail_get_url_item_news(self):
        with self.assertRaises(ValueError):
            _ = self.input.url_item_news

    def test_get_url_item_news(self):
        self.input.set_page_id(self.test_id_page)
        self.assertEqual(self.input.url_item_news, f"{self.base_url}/{self.test_id_page}")

    def test_fetch_page(self):
        self.input.set_page_id(self.test_id_page)
        html = self.input.fetch_page()
        self.assertIsInstance(html, str)
        is_html = bool(BeautifulSoup(html, "html.parser").find())
        self.assertTrue(is_html)
