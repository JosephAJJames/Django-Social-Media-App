#helper functions
from .models import User


def add_to_diff_dict(differences, key_value_tuple):
    key, value = key_value_tuple[0], key_value_tuple[1]
    differences[key] = value
    return differences

def apply_changes(differences, user):
    for key, value in differences:
        User.objects.filter(id=user.id).update(**differences)


def detect_difference(dict_of_original_user, dict_of_new_user):
    cntr = 0
    differences = {}

    for key, value in dict_of_original_user:
        if key in dict_of_new_user: #checking they both have this key
            val1 = dict_of_original_user[key]
            val2 = dict_of_new_user[key]

            if val1 != val2:
                differences = add_to_diff_dict(differences, (key, val2)) #add the key and the changed value to

    return differences