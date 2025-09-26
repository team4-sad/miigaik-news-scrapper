import abc


class BaseInput(abc.ABC):
    def fetch(self):
        pass

    def fetch_page(self):
        pass

    def next_page(self):
        pass

    def set_page_id(self, page_id):
        pass

    @property
    def page(self):
        raise NotImplementedError()
