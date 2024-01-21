import logging

from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

@pytest.fixture
def create_pet_test_data():
    endpoint = "/pets/"
    response = api_helpers.get_api_data(endpoint)
    id_list = [entry["id"] for entry in response.json()]
    json = {"id": max(id_list)+1, "name": "mastan", "type": "cat", "status": "available"}
    return json

@pytest.fixture
def create_order_test_data(create_pet_test_data):
    json = {"pet_id": create_pet_test_data.get("id")}
    return json

@pytest.fixture
def update_order_status_test_data():
    json = {"status": "sold"}
    return json


def test_patch_order_by_id(create_pet_test_data, create_order_test_data, update_order_status_test_data):
    logging.info('Post request for creating a new pet')
    endpoint_create_pet = "/pets/"
    response_from_pet_creation = api_helpers.post_api_data(endpoint_create_pet, create_pet_test_data)
    assert response_from_pet_creation.status_code == 201, 'Status code validation failed.'
    assert (response_from_pet_creation.json())["status"] == "available", 'Pet status validation failed.'

    logging.info('Post request to create a new order based on pet id')
    endpoint_create_order = "/store/order"
    response_from_order = api_helpers.post_api_data(endpoint_create_order, create_order_test_data)
    order_id = (response_from_order.json())["id"]
    print('order_id: '+order_id)
    assert response_from_order.status_code == 201, 'Status code validation failed.'
    validate(instance=response_from_order.json(), schema=schemas.order)

    logging.info('Get request to verify status of order.')
    endpoint_get_by_pet_id = f"/pets/{create_pet_test_data.get('id')}"
    response_from_get_by_pet_id = api_helpers.get_api_data(endpoint_get_by_pet_id)
    assert response_from_get_by_pet_id.status_code == 200, 'Status code validation failed.'
    assert (response_from_get_by_pet_id.json())["status"] == "pending", 'Status of order does not match'

    logging.info('Verify message, status code and current pet status which is "sold"')
    endpoint_update_order_status = '/store/order/'+order_id
    response_from_order_status_update = api_helpers.patch_api_data(endpoint_update_order_status,
                                                                   update_order_status_test_data)
    assert response_from_order_status_update.status_code == 200, 'Status code validation failed.'
    response_from_get_by_pet_id = api_helpers.get_api_data(endpoint_get_by_pet_id)
    assert (response_from_get_by_pet_id.json())['status'] == 'sold', 'Current pet status does not match'
    assert (response_from_order_status_update.json())["message"] == "Order and pet status updated successfully", \
        'Message does not match with the expected one'


    # --BUG# 1--
    # USER IS NOT ABLE TO UPDATE "PENDING" STATUS TO "AVAILABLE". USER ONLY ALLOW TO UPDATE THAT TO "SOLD" STATUS

    # --BUG# 2--
    # PET ID ALLOWS 2 DATA TYPES: STRING AND INTEGER
