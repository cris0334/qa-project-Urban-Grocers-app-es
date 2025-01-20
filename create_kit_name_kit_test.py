import data
import sender_stand_request

# Seccion de usuarios, copiado de proyecto anterior
# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

def get_kit_body(kit_name):
    kit_body = {}
    if ~(kit_name is None):
        data.kit_create_data.copy()
        kit_body['name'] = kit_name

    return kit_body

def create_user_and_get_token(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]

# fin de seccion de usuarios

def get_kit_create_ok_body(kit_name, auth_token):
    kit_create_ok_body = data.kit_create_ok_response

    kit_create_ok_body['name'] = kit_name
    kit_create_ok_body['user']['authToken'] = auth_token

    return kit_create_ok_body


def get_kit_create_error_name_body():
    return data.kit_create_error_name_response.copy()

def get_kit_create_error_parameter_body():
    return data.kit_create_error_parameter_response.copy()

def positive_assert(kit_name, auth_token):
    kit_body = get_kit_body(kit_name)
    kit_create_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    kit_create_response_json = kit_create_response.json()
    assert kit_create_response.status_code == 201
    assert kit_create_response_json["name"] == kit_name
    assert kit_create_response_json["user"]["authToken"] == auth_token

def negative_assert_name(kit_name, auth_token):
    kit_body = get_kit_body(kit_name)
    kit_create_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    kit_create_error_name_body = get_kit_create_error_name_body()
    kit_create_response_json = kit_create_response.json()

    assert kit_create_response.status_code == 400
    assert kit_create_response_json["message"] == kit_create_error_name_body['message']

def negative_assert_params(kit_name, auth_token):
    kit_body = get_kit_body(kit_name)
    kit_create_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    kit_create_error_parameter_body = get_kit_create_error_parameter_body()
    kit_create_response_json = kit_create_response.json()

    assert kit_create_response.status_code == 400
    assert kit_create_response_json["code"] == kit_create_error_parameter_body['code']
    assert kit_create_response_json["message"] == kit_create_error_parameter_body['message']


def test_create_kit_1_letter_in_kit_name_get_success_response():
    auth_token = create_user_and_get_token("Andrea")
    positive_assert("a",
                    auth_token)

def test_create_kit_15_letter_in_kit_name_get_success_response():
    auth_token = create_user_and_get_token("Andrea")
    positive_assert("Aaaaaaaaaaaaaaa",
                    auth_token)

def test_create_user_0_letter_in_kit_name_get_error_response():
    auth_token = create_user_and_get_token("Andrea")
    negative_assert_name("",
                         auth_token)

def test_create_user_16_letter_in_kit_name_get_error_response():
    auth_token = create_user_and_get_token("Andrea")
    negative_assert_name("Aaaaaaaaaaaaaaaa",
                         auth_token)

def test_create_kit_special_letter_in_kit_name_get_success_response():
    auth_token = create_user_and_get_token("Andrea")
    positive_assert('"№%@",',
                    auth_token)

def test_create_kit_empty_space_letter_in_kit_name_get_success_response():
    auth_token = create_user_and_get_token("Andrea")
    positive_assert("A Aaa",
                    auth_token)

def test_create_user_number_string_in_kit_name_get_error_response():
    auth_token = create_user_and_get_token("Andrea")
    positive_assert("123",
                    auth_token)

def test_create_user_empty_body_get_error_response():
    auth_token = create_user_and_get_token("Andrea")
    negative_assert_params(None,
                           auth_token)

def test_create_user_2_letter_in_kit_name_get_error_response():
    auth_token = create_user_and_get_token("Andrea")
    negative_assert_name(123,
                         auth_token)