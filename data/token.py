import requests
import json

def token(akun):
	try:
		return requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(akun.split("|")[-0],akun.split("|")[-1])).json()["access_token"]
	except:
		return False
		
def basetoken(url=None):
	token=json.loads(open("config/config.json").read())
	try:
		return requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(token["email"],token["pass"])).json()["access_token"]
	except:return False
