import json
import pytest
import inventory5




my_path = "../ACI_Inventory/json/"
my_file = "lc_lab.json"
r_content = my_path + my_file
#inventory5.my_url = content


@pytest.fixture(scope='module')
def db():
    print('-------- Setup --------')
    r_data = inventory5.OpenFile()
    db = r_data.open_file(r_content)
    yield db
    print('-------- Teardown -----')
    del db


def test_list(db):
    print("BOO")
    assert type(db) == dict

