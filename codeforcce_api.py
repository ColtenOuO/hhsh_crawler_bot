import requests

def get_user_data(handle):
    url = "https://codeforces.com/api/user.info"
    data = { # 參數
        "handles": handle,
    }
    
    access_token = requests.post(url, data = data)

    if( access_token.json()['status'] != 'OK' ):
        return 'No User'

    return access_token.json()['result'][0]
def get_user_rank(handle):
    url = "https://codeforces.com/api/user.info"
    data = { # 參數
        "handles": handle,
    }
    
    access_token = requests.post(url, data = data)

    return access_token.json()['result'][0]['rank']