# class docs
Dropbox API version : 2

## init

set your Dropbox API access token to "access_token" param.

``` python
import dropbox_tools as dbox
access_token = 'your_access_token'
l = dbox.docs(access_token).getlist()
print(l.content)
```
