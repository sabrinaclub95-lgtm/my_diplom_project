import sender_stand_request
import data


def test_create_and_get_order():
      
  order_response = sender_stand_request.post_new_order(data.body)

    
  assert order_response.status_code == 201

    
  track_number = order_response.json()["track"]
  
   
  get_order_response = sender_stand_request.get_order_by_track(track_number)

    
    
  assert get_order_response.status_code == 200 
