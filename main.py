import requests

# create basic UI
# (1) the program must fetch user information
# (2) dedicated window to paste content
# (3) dedicated window to fetch content
# the program must store api keys (encrypted)
# and the user keys. It must also store fetched data in secure
# files
# (4) send the fetched data via e-mail

# API user log-in data
api_dev_key = str()
api_user_name = str()
api_user_password = str()
api_user_key = str()

d = {"api_dev_key": api_dev_key, "api_user_name": api_user_name, "api_user_password": api_user_password}


class User():
    def __init__(self):
        pass

    def get_user_key(self, dev_key, user_name, user_pw):
        try:
            d = {'api_dev_key': f"{dev_key}", 'api_user_name': f"{user_name}", 'api_user_password': f"{user_pw}"}
            request = requests.post("https://pastebin.com/api/api_login.php", d)
            print(f"[i] {request.status_code}")
            return request.text
        except Exception as E:
            print(f"[X] {E}\t Try again")


request = requests.post("https://pastebin.com/api/api_login.php", d)
