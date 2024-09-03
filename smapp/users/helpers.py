#helper functions
from django.db.transaction import commit

from .models import User
from profilepics.models import ProfilePic


def add_to_diff_dict(differences, key_value_tuple):
    key, value = key_value_tuple[0], key_value_tuple[1]
    if key == "profilepic":
        piccie = key_value_tuple[1]
        new_pfp = ProfilePic(image=piccie)
        new_pfp.save()
        value = new_pfp.id

    differences[key] = value
    return differences


def apply_changes(differences, user):
    print(differences)
    print("user_id: ", user.id)
    User.objects.filter(id=user.id).update(**differences)


def detect_difference(dict_of_original_user, dict_of_new_user):
    cntr = 0
    differences = {}

    for key, value in dict_of_original_user.items():
        if key in dict_of_new_user: #checking they both have this key
            print("key: ", key)
            val1 = dict_of_original_user[key]
            val2 = dict_of_new_user[key]
            print("val1: ", val1,"val2: ", val2) #profile pic is None

            if val1 != val2:
                print("difference detected", val1, val2)
                differences = add_to_diff_dict(differences, (key, val2)) #add the key and the changed value to

    return differences

