import dropbox_tools
import _token

tools = dropbox_tools.dropbox_tools(_token.access_token)
t = tools.make_correspond_table()
i_to_name = []
i = 0
for item in t:
    i_to_name.append(item)
    i = i + 1

while True:
    print("----- 0: show, 1:upload, 2:download -----")
    print("input num:")
    sel = input()
    if int(sel) == 0:
        i = 0
        for item in t:
            print(i, item, t[item])
            i = i + 1
    elif int(sel) == 1:
        print("file name ? : ")
        path = input()
        tools.upload_file(path)
    elif int(sel) == 2:
        print("file number ? : ")
        n = input()
        with open(i_to_name[int(n)]+".md", mode="w", encoding="UTF-8") as f:
            f.write(tools.download(t[i_to_name[int(n)]]).content.decode())

    else:
        break