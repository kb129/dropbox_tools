# class docs
Dropbox API version : 2

## init

set your Dropbox API access token to "access_token" param.

``` python
import dropbox_tools as dbox
import json

access_token = 'your_access_token'
j = dbox.docs(access_token).getlist().json()
print(j)
```
