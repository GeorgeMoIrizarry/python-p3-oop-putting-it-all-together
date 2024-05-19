#!/usr/bin/env python3
import ipdb
class Book:
    def __init__(self, title="A Book!", page_count=1):
        self.title = title
        self.page_count = page_count
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count): 
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
# ipdb.set_trace()