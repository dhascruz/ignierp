
import requests


MOODLE_BASE_URL = "https://staging.igniteict.com"
MOODLE_WS_TOKEN = "f7b2275d40d76bc3478eae17a791026f"   
MOODLE_URL = "https://your-moodle.com"
LOGIN_URL = f"{MOODLE_BASE_URL}/login/token.php"
REST_URL = f"{MOODLE_BASE_URL}/webservice/rest/server.php"

def get_moodle_token(username, password, service="moodle_mobile_app"):
    params = {"username": username, "password": password, "service": service}
    res = requests.get(LOGIN_URL, params=params).json()
    if "error" in res:
        raise Exception(res["error"])
    return res.get("token")

def get_moodle_user_info(token):
    params = {"wstoken": token, "wsfunction": "core_webservice_get_site_info", "moodlewsrestformat": "json"}
    res = requests.get(REST_URL, params=params).json()
    if "exception" in res:
        raise Exception(res["message"])
    return res

def get_moodle_courses(token, userid):
    params = {"wstoken": token, "wsfunction": "core_enrol_get_users_courses", "userid": userid, "moodlewsrestformat": "json"}
    res = requests.get(REST_URL, params=params).json()
    if isinstance(res, dict) and "exception" in res:
        raise Exception(res["message"])
    return res

