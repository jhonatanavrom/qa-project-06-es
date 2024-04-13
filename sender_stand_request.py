import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def get_user_token():
    response = post_new_user(data.user_body)
    response_data = response.json()
    return response_data['authToken']

def post_new_client_kit(kit_body):
    auth_token = get_user_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json=kit_body.copy(),  # inserta el cuerpo de solicitud
                         headers=headers)  # inserta los encabezados