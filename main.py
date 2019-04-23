import sys
import paper_tools as paper
import _token
import json

class tools:

    def __init__(self, access_token):
        self.p = paper.paper_tools(access_token)

    def get_doc_ids(self):
        items = self.p.getlist().json()
        return items["doc_ids"]

    def make_correspond_table(self):
        l = {}
        for c in self.get_doc_ids():
            l[self.p.get_title(c)] = c
        return l


if __name__ == "__main__":
    argv = sys.argv
    t = tools(_token.access_token)
    print(t.make_correspond_table().keys())
