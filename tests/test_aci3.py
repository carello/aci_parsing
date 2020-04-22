import json
import pytest
import inventory6




my_path = "../ACI_Inventory/json/"
my_file = "lc_lab.json"
h_content = my_path + my_file
#inventory5.my_url = content


@pytest.fixture(scope='module')
def db():
    print('-------- Setup --------')
    r_data = inventory6.OpenFile(h_content)
    db = r_data.open_file()
    yield db
    print('-------- Teardown -----')
    del db


def test_list(db):
    print("BOO")
    print(db)
    assert type(db) == dict
