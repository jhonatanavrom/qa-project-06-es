import sender_stand_request
import data
import pytest

# esta función cambia los valores en el parámetro "name"
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def positive_assert(kit_name_value):
    kit_body = get_kit_body(kit_name_value)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    # El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    response = kit_response.json()
    assert response['name'] == kit_name_value

def negative_assert_code_400(kit_name_value_2):
    kit_body2 = get_kit_body(kit_name_value_2)
    kit_response = sender_stand_request.post_new_client_kit(kit_body2)
    assert kit_response.status_code == 400

#El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_success_response():
    positive_assert("a")

#El número permitido de caracteres (511)
def test_create_kit_511_letters_in_name_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#El número de caracteres es menor que la cantidad permitida (0):
def test_create_kit_0_letters_in_name_negative_response():
    negative_assert_code_400("")

#El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letters_in_name_negative_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Se permiten caracteres especiales:
def test_create_kit_special_characters_in_name_success_response():
    positive_assert("№%@,")

#Se permiten espacios
def test_create_kit_blank_spaces_in_name_success_response():
    positive_assert(" A Aaa ")

#Se permiten números
def test_create_kit_with_numbers_in_name_success_response():
    positive_assert("1234")

def negative_assert_no_kit_name(kit_body_3):
    response = sender_stand_request.post_new_client_kit(kit_body_3)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400

#El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_kit_name(kit_body)

#Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400
