import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
        json=body,
        headers=data.headers
    )


response = get_docs()
print(response.status_code)


response = post_new_order(data.body)
print(response.status_code)


track_number = response.json().get("track")

def get_order_by_track(track):
    params = {"t": track}  
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
        params=params,
        headers=data.headers
    )


if track_number:
    response = get_order_by_track(track_number)
    print(response.status_code)
else:
    print("Трек-номер не получен.")
 
