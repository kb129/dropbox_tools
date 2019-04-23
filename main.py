import sys
import dropbox_tools as dbox
import _token
import json

def get_doc_ids(access_token):
    items = dbox.docs(access_token).getlist().json()
    return items["doc_ids"]


print(get_doc_ids(_token.access_token))