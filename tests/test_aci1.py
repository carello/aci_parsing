import json
import pytest
import inventory4b




my_path = "../ACI_Inventory/json/"
my_file = "lc_lab.json"
content = my_path + my_file
#inventory5.my_url = content


@pytest.fixture(scope='module')
def db():
    print('-------- Setup --------')
    db = inventory4b.open_file(content)
    yield db
    print('-------- Teardown -----')
    del db


def test_list(db):
    print("BOO")
    assert type(db) == dict

