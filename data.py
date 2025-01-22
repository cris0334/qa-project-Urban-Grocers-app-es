headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_create_data = {
    "name": ""
}

kit_create_ok_response = {
       "name": "",
       "user": {
        "id": 0,
        "firstName": "",
        "phone": "",
        "address": "",
        "email": "",
        "comment": "",
        "authToken": ""
    },
       "productsList": None,
       "id": 0,
       "productsCount": 0
   }

kit_create_error_parameter_response = {
       "code": 400,
       "message": "No se han aprobado todos los parámetros requeridos"
   }

kit_create_error_name_response = {
       "code": 400,
       "message": "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
   }