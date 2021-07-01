import secrets
import string
import requests
from lxml import html, cssselect
from collections import Counter, OrderedDict


class PhonesCodes:
    def __init__(self):
        self.phones_n_codes = [{'phone': None,
                                'code': None}]
        self.request = None

    def generate_code(self, length=6):
        phone = self.request.args.get('phone')
        try:
            int(phone)
        except TypeError:
            return {"incrorect phone": True}

        if len(phone) < 6:
            return {"incrorect phone": True}

        letters_and_digits = string.ascii_uppercase + string.digits
        code = ''.join(secrets.choice(
            letters_and_digits) for _ in range(length))

        # Проверка существующего телефона запись/перезапись
        for each in range(len(self.phones_n_codes)):
            if phone == self.phones_n_codes[each]['phone']:
                self.phones_n_codes[each] = {'phone': phone,
                                             'code': code}
                return code
            else:
                self.phones_n_codes.append({"phone": phone,  # TODO проверка на корректность телефона
                                            "code": code})
        return code

    def check_phone(self):
        password = self.request.get_json()
        if password in self.phones_n_codes:
            return {"status": "OK"}
        else:
            return {"status": "Fail"}


def check_tags(required_tags, having_tags):
    checked_tags = {}
    for tag in required_tags:
        if tag in having_tags:
            checked_tags[tag] = having_tags[tag]
    return checked_tags


def structure_scan(url, required_tags=None):
    tags = {}
    page = requests.get(url)
    tree = html.fromstring(page.content)
    all_elms = tree.cssselect('*')
    all_tags = Counter([x.tag for x in all_elms])

    for tag in all_tags:
        tags[tag] = all_tags[tag]

    if required_tags:
        return check_tags(required_tags=required_tags, having_tags=tags)
    else:
        return tags


def find_difference(url, structure):
    link_structure = structure_scan(url)
    difference = {}

    for key, value in link_structure.items():
        if key in structure:
            if value != structure[key]:
                difference[key] = abs(link_structure[key] - structure[key])
        else:
            difference[key] = link_structure[key]

    if bool(difference):
        return {"is_correct": "False", "difference": difference}
    else:
        return {"is_correct": "True"}
