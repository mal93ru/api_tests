# Тестирование API
Тестирование API сервиса jsonplaceholder.typicode.com с помощью Python используя библиотеки pytest, requests, jsonschema
Тесты для todos - https://jsonplaceholder.typicode.com/todos:

test_api_hw3.py::
test_getting_positive - Позитивный тест для Getting a resource
test_getting_negative - Негативный тест для Getting a resource
test_listing_all - Позитивный тест для Listing all resources
test_creating - Позитивный тест для Creating a resource
test_updating_with_put_positive - Позитивный тест для Updating a resource with PUT
test_updating_with_put_negative - Негативный тест для Updating a resource with PUT
test_updating_with_patch - Позитивный тест для Updating a resource with PATCH
test_deleting - Позитивный тест для Deleting a resource
test_filtering_positive - Позитивный тест для Filtering resources
test_filtering_negative - Негативный тест для Filtering resources


Тестирование json sсhema сервиса jsonplaceholder.typicode.com
Тесты для проверки структуры json (schema) todos - https://jsonplaceholder.typicode.com/todos

test_schema_hw3.py::
test_schema_getting - Тест схемы одного todo
test_schema_listing_all - Тест схемы массива todos

schemas/* - Схемы, использующиеся тестами
