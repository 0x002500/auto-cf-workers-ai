import request

def req(model, prompt, account_id, api_token):
    headers = {'Authorization': Bearer {api_token}}
    prompt = {"prompt": {prompt}}
    res = requests.get('https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}', headers=headers, data=prompt)
    data = res.json()
    if data['success'] == false:
        return "false"
    else:
        return data['result']['response']
