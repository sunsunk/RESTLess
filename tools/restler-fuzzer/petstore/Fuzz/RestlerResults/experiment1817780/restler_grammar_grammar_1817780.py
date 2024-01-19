""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_pet_post_id = dependencies.DynamicVariable("_pet_post_id")

_pet_post_name = dependencies.DynamicVariable("_pet_post_name")

_pet_post_photoUrls_0 = dependencies.DynamicVariable("_pet_post_photoUrls_0")

_pet_post_status = dependencies.DynamicVariable("_pet_post_status")

_pet_put_id = dependencies.DynamicVariable("_pet_put_id")

_store_order_post_id = dependencies.DynamicVariable("_store_order_post_id")

def parse_petpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    temp_8173 = None
    temp_7680 = None
    temp_5581 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8173 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7680 = str(data["photoUrls"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5581 = str(data["status"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262 or temp_8173 or temp_7680 or temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_pet_post_id", temp_7262)
    if temp_8173:
        dependencies.set_variable("_pet_post_name", temp_8173)
    if temp_7680:
        dependencies.set_variable("_pet_post_photoUrls_0", temp_7680)
    if temp_5581:
        dependencies.set_variable("_pet_post_status", temp_5581)


def parse_petput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2060 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_2060 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_pet_put_id", temp_2060)


def parse_storeorderpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5588 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_5588 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_store_order_post_id", temp_5588)

req_collection = requests.RequestCollection([])
# Endpoint: /pet, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"10"']),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["doggie"]),
    primitives.restler_static_string(""",
    "category":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"1"']),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Dogs"]),
    primitives.restler_static_string("""
        }
    ,
    "photoUrls":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "tags":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "status":"""),
    primitives.restler_fuzzable_group("status", ['available','pending','sold']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_petpost,
            'dependencies':
            [
                _pet_post_id.writer(),
                _pet_post_name.writer(),
                _pet_post_photoUrls_0.writer(),
                _pet_post_status.writer()
            ]
        }

    },

],
requestId="/pet"
)
req_collection.add_request(request)

# Endpoint: /pet, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_static_string(_pet_post_id.reader(), quoted=False),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_pet_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "category":
        {
            "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"1"']),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["Dogs"]),
    primitives.restler_static_string("""
        }
    ,
    "photoUrls":"""),
    primitives.restler_static_string(_pet_post_photoUrls_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "tags":
    [
        {
            "id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "status":"""),
    primitives.restler_static_string(_pet_post_status.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_petput,
            'dependencies':
            [
                _pet_put_id.writer()
            ]
        }

    },

],
requestId="/pet"
)
req_collection.add_request(request)

# Endpoint: /pet/findByStatus, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("findByStatus"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_group("status", ['available','pending','sold'] , default_enum="available" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pet/findByStatus"
)
req_collection.add_request(request)

# Endpoint: /pet/findByTags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("findByTags"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("tags="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pet/findByTags"
)
req_collection.add_request(request)

# Endpoint: /pet/{petId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pet_put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pet/{petId}"
)
req_collection.add_request(request)

# Endpoint: /pet/{petId}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pet_put_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pet/{petId}"
)
req_collection.add_request(request)

# Endpoint: /pet/{petId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pet_put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("api_key: "),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pet/{petId}"
)
req_collection.add_request(request)

# Endpoint: /pet/{petId}/uploadImage, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pet"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_pet_put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("uploadImage"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("additionalMetadata="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/pet/{petId}/uploadImage"
)
req_collection.add_request(request)

# Endpoint: /store/inventory, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("store"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("inventory"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/store/inventory"
)
req_collection.add_request(request)

# Endpoint: /store/order, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("store"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("order"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"10"']),
    primitives.restler_static_string(""",
    "petId":"""),
    primitives.restler_fuzzable_int("1", examples=['"198772"']),
    primitives.restler_static_string(""",
    "quantity":"""),
    primitives.restler_fuzzable_int("1", examples=['"7"']),
    primitives.restler_static_string(""",
    "shipDate":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "status":"""),
    primitives.restler_fuzzable_group("status", ['placed','approved','delivered']  ,quoted=True, examples=["approved"]),
    primitives.restler_static_string(""",
    "complete":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_storeorderpost,
            'dependencies':
            [
                _store_order_post_id.writer()
            ]
        }

    },

],
requestId="/store/order"
)
req_collection.add_request(request)

# Endpoint: /store/order/{orderId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("store"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("order"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_store_order_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/store/order/{orderId}"
)
req_collection.add_request(request)

# Endpoint: /store/order/{orderId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("store"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("order"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_store_order_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/store/order/{orderId}"
)
req_collection.add_request(request)

# Endpoint: /user, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"10"']),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["theUser"]),
    primitives.restler_static_string(""",
    "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["John"]),
    primitives.restler_static_string(""",
    "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["James"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["john@email.com"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
    "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
    "userStatus":"""),
    primitives.restler_fuzzable_int("1", examples=['"1"']),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user"
)
req_collection.add_request(request)

# Endpoint: /user/createWithList, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("createWithList"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("["),
    primitives.restler_static_string("""
    {
        "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"10"']),
    primitives.restler_static_string(""",
        "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["theUser"]),
    primitives.restler_static_string(""",
        "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["John"]),
    primitives.restler_static_string(""",
        "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["James"]),
    primitives.restler_static_string(""",
        "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["john@email.com"]),
    primitives.restler_static_string(""",
        "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
        "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
        "userStatus":"""),
    primitives.restler_fuzzable_int("1", examples=['"1"']),
    primitives.restler_static_string("""
    }]"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/createWithList"
)
req_collection.add_request(request)

# Endpoint: /user/login, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("login"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("username="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("password="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/login"
)
req_collection.add_request(request)

# Endpoint: /user/logout, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("logout"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/logout"
)
req_collection.add_request(request)

# Endpoint: /user/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/{username}"
)
req_collection.add_request(request)

# Endpoint: /user/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "id":"""),
    primitives.restler_fuzzable_int("1", examples=['"10"']),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["theUser"]),
    primitives.restler_static_string(""",
    "firstName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["John"]),
    primitives.restler_static_string(""",
    "lastName":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["James"]),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["john@email.com"]),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
    "phone":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["12345"]),
    primitives.restler_static_string(""",
    "userStatus":"""),
    primitives.restler_fuzzable_int("1", examples=['"1"']),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/{username}"
)
req_collection.add_request(request)

# Endpoint: /user/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8080\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/{username}"
)
req_collection.add_request(request)
