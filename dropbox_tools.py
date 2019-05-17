import sys
import paper_tools as paper
import _token
import json

class dropbox_tools:
    def __init__(self, access_token):
        self.p = paper.paper_tools(access_token)

    def __get_doc_ids(self):
        items = self.p.getlist().json()
        return items["doc_ids"]

    def make_correspond_table(self):
        l = {}
        for c in self.__get_doc_ids():
            l[self.p.get_title(c)] = c
        return l

    def upload_file(self, path):
        self.p.create(path)

    def download(self, fid, mode="md"):
        if mode == "md":
            return self.p.download_md(fid)
        else:
            # TODO
            print("in preparation")


if __name__ == "__main__":
    argv = sys.argv
    t = dropbox_tools(_token.access_token)
    print(t.make_correspond_table().keys())
