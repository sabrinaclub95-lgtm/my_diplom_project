import sender_stand_request
import data



def get_kit_body(name):
    
    current_kit_body = data.kit_body.copy()
    
    current_kit_body["name"] = name
    
    return current_kit_body



def positive_assert(kit_body):
    
    resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    
    assert resp_kit.status_code == 201
    
    assert resp_kit.json()["name"] == kit_body["name"]




def negative_assert_code_400(kit_body):
   resp_kit = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
   assert resp_kit.status_code == 400

def get_new_user_token():
    
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    
    return resp_user.json()["authToken"]


    # Тест 1. 
def test_create_kit_1_letter_in_name_get_success_response():
   kit_body = get_kit_body("a")
   positive_assert(kit_body)
    
    # Тест 2.
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)
    # Тест 3.  Ошибка
def test_create_kit_0_letter_in_name_get_success_response ():
   negative_assert_code_400("")

    # Тест 4.  Ошибка
def test_create_kit_512_letter_in_name_get_success_response ():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


    #Тест 5.  
def test_create_kit_eng_letter_in_name_get_success_response ():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

    #Тест 6.
def test_create_kit_rus_letter_in_name_get_success_response ():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

    #Тест 7.
def test_create_kit_spec_letter_in_name_get_success_response ():
    kit_body = get_kit_body("№%@,")
    positive_assert(kit_body)

    #Тест 8.
def test_create_kit_probel_letter_in_name_get_success_response ():
    kit_body = get_kit_body("Человек и КО")
    positive_assert(kit_body)

    #Тест 9.
def test_create_kit_digit_letter_in_name_get_success_response ():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

     #Тест 10. Ошибка
def test_create_kit_ne_peredan_letter_in_name_get_success_response ():
   negative_assert_code_400

    #Тест 11. Ошибка
def test_create_kit_int_letter_in_name_get_success_response ():
   negative_assert_code_400(123)