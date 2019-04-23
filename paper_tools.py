import sys
import requests
import json

class paper_tools:
    # constructor
    def __init__(self, access_token):
        self.access_token = access_token

    # get list of files in your dropbox
    def getlist(self):
        url = "https://api.dropboxapi.com/2/paper/docs/list"

        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }

        data = {
        }
        r = requests.post(url, headers=headers, data=json.dumps(data))
        return r

    # create new document file in your dropbox
    def create(self, fname):
        url = "https://api.dropboxapi.com/2/paper/docs/create"

        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": "{\"import_format\":{\".tag\":\"markdown\"}}"
        }

        data = open(fname, "rb").read()

        r = requests.post(url, headers=headers, data=data)
        return r

    # download file specified by fid param formed markdown style
    def download_md(self, fid):
        url = "https://api.dropboxapi.com/2/paper/docs/download"

        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Dropbox-API-Arg": "{\"doc_id\":\"" + fid + "\",\"export_format\":{\".tag\":\"markdown\"}}"
        }

        r = requests.post(url, headers=headers)
        return r

    # get title of "fid"
    def get_title(self, fid):
        r = self.download_md(fid)
        return eval(r.headers['Dropbox-Api-Result'])['title']




if __name__ == "__main__":
    argv = sys.argv
    d = paper_tools(argv[1])
    print(d.getlist().content.decode())