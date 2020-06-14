import phonenumbers
from phonenumbers import NumberParseException


def number_phone_is_not_valid(number_phone_raw):
    if number_phone_raw[:3] == '+52':
        try:
            phonenumbers.parse(number_phone_raw)
        except NumberParseException as e:
            print(e.error_type)
            return "El numero ingresado debe terner el siguiente formato: <codigo_pais><area><numero_telefonico> " \
                   "Eje: +52553787852"
    else:
        return "El numero tiene que ser con lada internacional +52"
    return None