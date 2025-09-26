import requests
from django.conf import settings

def moodle_api_call(ws_function, params: dict):
    """
    Generic function to call Moodle REST API.
    """
    url = f"{settings.MOODLE_BASE_URL}/webservice/rest/server.php"
    data = {
        "wstoken": settings.MOODLE_WS_TOKEN,
        "wsfunction": ws_function,
        "moodlewsrestformat": "json",
    }
    print(url)
    data.update(params)
    print(data)
    response = requests.post(url, data=data)
    response.raise_for_status()
    print(response.json()  )
    return response.json()

def get_all_users():
    
    payload = {
        "criteria[0][key]": "username",   # empty key means no filtering
        "criteria[0][value]": "%"
    }
    return moodle_api_call("core_user_get_users", payload)    


def create_user(username, password, firstname, lastname, email):
    payload = {
        "users[0][username]": username,
        "users[0][password]": password,
        "users[0][firstname]": firstname,
        "users[0][lastname]": lastname,
        "users[0][email]": email,
        "users[0][auth]": "manual",
    }
    return moodle_api_call("core_user_create_users", payload)


def get_user_by_id(userid):
    return moodle_api_call("core_user_get_users_by_field", {
        "field": "id",
        "values[0]": userid,
    })


def update_user(userid, **kwargs):
    payload = {f"users[0][{k}]": v for k, v in kwargs.items()}
    payload["users[0][id]"] = userid
    return moodle_api_call("core_user_update_users", payload)


def delete_user(userid):
    return moodle_api_call("core_user_delete_users", {"userids[0]": userid})
