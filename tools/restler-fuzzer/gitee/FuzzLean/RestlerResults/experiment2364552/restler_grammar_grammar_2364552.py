""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_v5_repos__owner___repo__keys_post_id = dependencies.DynamicVariable("_v5_repos__owner___repo__keys_post_id")

_v5_repos__owner___repo__contents__path__put_content_path = dependencies.DynamicVariable("_v5_repos__owner___repo__contents__path__put_content_path")

_v5_repos__owner__issues_post_number = dependencies.DynamicVariable("_v5_repos__owner__issues_post_number")

_v5_repos__owner___repo__labels_post_name = dependencies.DynamicVariable("_v5_repos__owner___repo__labels_post_name")

_v5_repos__owner___repo__issues__number__labels_put_name = dependencies.DynamicVariable("_v5_repos__owner___repo__issues__number__labels_put_name")

_v5_repos__owner___repo__milestones_post_number = dependencies.DynamicVariable("_v5_repos__owner___repo__milestones_post_number")

_v5_repos__owner___repo__collaborators__username__put_id = dependencies.DynamicVariable("_v5_repos__owner___repo__collaborators__username__put_id")

_v5_repos__owner___repo__pulls_post_number = dependencies.DynamicVariable("_v5_repos__owner___repo__pulls_post_number")

_v5_repos__owner___repo__pulls__number__labels_put_name = dependencies.DynamicVariable("_v5_repos__owner___repo__pulls__number__labels_put_name")

_v5_repos__owner___repo__releases_post_id = dependencies.DynamicVariable("_v5_repos__owner___repo__releases_post_id")

_v5_repos__owner___repo__hooks_post_id = dependencies.DynamicVariable("_v5_repos__owner___repo__hooks_post_id")

_v5_user_keys_post_id = dependencies.DynamicVariable("_v5_user_keys_post_id")

_v5_gists_post_0_id = dependencies.DynamicVariable("_v5_gists_post_0_id")

_v5_gists__gist_id__comments_post_id = dependencies.DynamicVariable("_v5_gists__gist_id__comments_post_id")

_v5_orgs__org__memberships__username__put_organization_id = dependencies.DynamicVariable("_v5_orgs__org__memberships__username__put_organization_id")

_v5_enterprises__enterprise__week_report_post_id = dependencies.DynamicVariable("_v5_enterprises__enterprise__week_report_post_id")

_v5_enterprises__enterprise__members__username__put_enterprise_id = dependencies.DynamicVariable("_v5_enterprises__enterprise__members__username__put_enterprise_id")

_v5_notifications_messages_post_id = dependencies.DynamicVariable("_v5_notifications_messages_post_id")

def parse_v5reposownerrepokeyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

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



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_v5_repos__owner___repo__keys_post_id", temp_7262)


def parse_v5reposownerrepocontentspathput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None

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
            temp_8173 = str(data["content"]["path"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_v5_repos__owner___repo__contents__path__put_content_path", temp_8173)


def parse_v5reposownerissuespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7680 = None

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
            temp_7680 = str(data["number"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_v5_repos__owner__issues_post_number", temp_7680)


def parse_v5reposownerrepolabelspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
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
            temp_5581 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_v5_repos__owner___repo__labels_post_name", temp_5581)


def parse_v5reposownerrepoissuesnumberlabelsput(data, **kwargs):
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
            temp_2060 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_v5_repos__owner___repo__issues__number__labels_put_name", temp_2060)


def parse_v5reposownerrepomilestonespost(data, **kwargs):
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
            temp_5588 = str(data["number"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5588):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5588:
        dependencies.set_variable("_v5_repos__owner___repo__milestones_post_number", temp_5588)


def parse_v5reposownerrepocollaboratorsusernameput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9060 = None

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
            temp_9060 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9060:
        dependencies.set_variable("_v5_repos__owner___repo__collaborators__username__put_id", temp_9060)


def parse_v5reposownerrepopullspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4421 = None

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
            temp_4421 = str(data["number"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4421):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4421:
        dependencies.set_variable("_v5_repos__owner___repo__pulls_post_number", temp_4421)


def parse_v5reposownerrepopullsnumberlabelsput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9775 = None

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
            temp_9775 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9775):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9775:
        dependencies.set_variable("_v5_repos__owner___repo__pulls__number__labels_put_name", temp_9775)


def parse_v5reposownerreporeleasespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2737 = None

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
            temp_2737 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2737):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2737:
        dependencies.set_variable("_v5_repos__owner___repo__releases_post_id", temp_2737)


def parse_v5reposownerrepohookspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2919 = None

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
            temp_2919 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2919):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2919:
        dependencies.set_variable("_v5_repos__owner___repo__hooks_post_id", temp_2919)


def parse_v5userkeyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4673 = None

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
            temp_4673 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4673):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4673:
        dependencies.set_variable("_v5_user_keys_post_id", temp_4673)


def parse_v5gistspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6326 = None

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
            temp_6326 = str(data[0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6326:
        dependencies.set_variable("_v5_gists_post_0_id", temp_6326)


def parse_v5gistsgist_idcommentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4695 = None

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
            temp_4695 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4695):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4695:
        dependencies.set_variable("_v5_gists__gist_id__comments_post_id", temp_4695)


def parse_v5orgsorgmembershipsusernameput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9821 = None

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
            temp_9821 = str(data["organization"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9821):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9821:
        dependencies.set_variable("_v5_orgs__org__memberships__username__put_organization_id", temp_9821)


def parse_v5enterprisesenterpriseweek_reportpost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_303 = None

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
            temp_303 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_303):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_303:
        dependencies.set_variable("_v5_enterprises__enterprise__week_report_post_id", temp_303)


def parse_v5enterprisesenterprisemembersusernameput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8623 = None

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
            temp_8623 = str(data["enterprise"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8623):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8623:
        dependencies.set_variable("_v5_enterprises__enterprise__members__username__put_enterprise_id", temp_8623)


def parse_v5notificationsmessagespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9953 = None

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
            temp_9953 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9953):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9953:
        dependencies.set_variable("_v5_notifications_messages_post_id", temp_9953)

req_collection = requests.RequestCollection([])
# Endpoint: /v5/repos/{owner}/{repo}/branches, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches/{branch}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches/{branch}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches/{branch}/protection, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("protection"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches/{branch}/protection"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches/{branch}/protection, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("protection"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches/{branch}/protection"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches/{wildcard}/setting, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches/{wildcard}/setting"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches/{wildcard}/setting, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches/{wildcard}/setting"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/branches/setting/new, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("setting"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("new"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/branches/setting/new"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/commits/{ref}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/commits/{ref}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/comments/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/comments/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/commits/{sha}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/commits/{sha}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="asc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/comments/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/comments/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sha="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("until="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/commits"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/commits/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/commits/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/compare/{base}...{head}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("compare"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/compare/{base}...{head}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/keys"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepokeyspost,
            'dependencies':
            [
                _v5_repos__owner___repo__keys_post_id.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/keys"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys/available, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("available"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/keys/available"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys/enable/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enable"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("id", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/keys/enable/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys/enable/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enable"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/keys/enable/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/keys/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/readme, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("readme"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/readme"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/contents(/{path}), method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents("),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/contents(/{path})"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/contents/{path}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__contents__path__put_content_path.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/contents/{path}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/contents/{path}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("path", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepocontentspathput,
            'dependencies':
            [
                _v5_repos__owner___repo__contents__path__put_content_path.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/contents/{path}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/contents/{path}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__contents__path__put_content_path.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sha="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("message="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("branch="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("committer[name]="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("committer[email]="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author[name]="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author[email]="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/contents/{path}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/git/blobs/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blobs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/git/blobs/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/git/trees/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trees"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recursive="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/git/trees/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/git/gitee_metrics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitee_metrics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/git/gitee_metrics"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','progressing','closed','rejected','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("schedule="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deadline="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("finished_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assignee="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("creator="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("program="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/issues, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerissuespost,
            'dependencies':
            [
                _v5_repos__owner__issues_post_number.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/issues/{number}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner__issues_post_number.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/issues/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/issues/{number}/pull_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner__issues_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pull_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/issues/{number}/pull_requests"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/issues/{number}/operate_logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner__issues_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operate_logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['desc','asc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/issues/{number}/operate_logs"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepolabelspost,
            'dependencies':
            [
                _v5_repos__owner___repo__labels_post_name.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/labels/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__labels_post_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/labels/{name}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/labels/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__labels_post_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/labels/{name}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/labels/{original_name}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__labels_post_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/labels/{original_name}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/labels, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepoissuesnumberlabelsput,
            'dependencies':
            [
                _v5_repos__owner___repo__issues__number__labels_put_name.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/labels, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/issues/{number}/labels/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__issues__number__labels_put_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/issues/{number}/labels/{name}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/project_labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("project_labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/project_labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/project_labels, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("project_labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/project_labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/project_labels, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("project_labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/project_labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/milestones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','closed','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['due_on'] , default_enum="due_on" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/milestones"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/milestones, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepomilestonespost,
            'dependencies':
            [
                _v5_repos__owner___repo__milestones_post_number.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/milestones"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/milestones/{number}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__milestones_post_number.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/milestones/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/milestones/{number}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__milestones_post_number.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/milestones/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/milestones/{number}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__milestones_post_number.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/milestones/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/license, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("license"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/license"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pages"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pages, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pages"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pages/builds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pages/builds"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/reviewer, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviewer"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/reviewer"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/push_config, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_config"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/push_config"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/push_config, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_config"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/push_config"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/contributors, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['authors','committers'] , default_enum="committers" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/contributors"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/tags"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/tags, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/tags"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/clear, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("clear"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/clear"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/collaborators, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/collaborators"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/collaborators/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__collaborators__username__put_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/collaborators/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/collaborators/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepocollaboratorsusernameput,
            'dependencies':
            [
                _v5_repos__owner___repo__collaborators__username__put_id.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/collaborators/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/collaborators/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__collaborators__username__put_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/collaborators/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/collaborators/{username}/permission, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__collaborators__username__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permission"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/collaborators/{username}/permission"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/forks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['newest','oldest','stargazers'] , default_enum="newest" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/forks"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/forks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/forks"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/baidu_statistic_key, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baidu_statistic_key"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/baidu_statistic_key"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/baidu_statistic_key, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baidu_statistic_key"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/baidu_statistic_key"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/baidu_statistic_key, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baidu_statistic_key"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/baidu_statistic_key"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/traffic-data, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("traffic-data"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/traffic-data"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','closed','merged','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("head="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("base="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated','popularity','long-running'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepopullspost,
            'dependencies':
            [
                _v5_repos__owner___repo__pulls_post_number.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/pulls"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/operate_logs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("operate_logs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['desc','asc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/operate_logs"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/commits"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/files"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/merge, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/merge"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/merge, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/merge"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/review, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("review"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/review"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/test, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("test"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/test"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/assignees, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/assignees"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/assignees, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignees"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assignees="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/assignees"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/assignees, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/assignees"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/testers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("testers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/testers"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/testers, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("testers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("testers="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/testers"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/testers, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("testers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/testers"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("comment_type="),
    primitives.restler_fuzzable_group("comment_type", ['diff_comment','pr_comment']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/labels, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepopullsnumberlabelsput,
            'dependencies':
            [
                _v5_repos__owner___repo__pulls__number__labels_put_name.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/{number}/labels/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls_post_number.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__pulls__number__labels_put_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/{number}/labels/{name}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/comments/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/comments/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/pulls/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/pulls/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/releases"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerreporeleasespost,
            'dependencies':
            [
                _v5_repos__owner___repo__releases_post_id.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/releases"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__releases_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/releases/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__releases_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/releases/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__releases_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/releases/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases/latest, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("latest"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/releases/latest"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/releases/tags/{tag}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/releases/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/hooks"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5reposownerrepohookspost,
            'dependencies':
            [
                _v5_repos__owner___repo__hooks_post_id.writer()
            ]
        }

    },

],
requestId="/v5/repos/{owner}/{repo}/hooks"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/hooks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/hooks/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/hooks/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/hooks/{id}/tests, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/hooks/{id}/tests"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/stargazers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stargazers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/stargazers"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/subscribers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscribers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/subscribers"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/events"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/notifications, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("unread="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("participating="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','event','referer'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/notifications"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/notifications, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/notifications"
)
req_collection.add_request(request)

# Endpoint: /v5/repos/{owner}/{repo}/open, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("open"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/repos/{owner}/{repo}/open"
)
req_collection.add_request(request)

# Endpoint: /v5/user/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/keys"
)
req_collection.add_request(request)

# Endpoint: /v5/user/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5userkeyspost,
            'dependencies':
            [
                _v5_user_keys_post_id.writer()
            ]
        }

    },

],
requestId="/v5/user/keys"
)
req_collection.add_request(request)

# Endpoint: /v5/user/keys/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_user_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/keys/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_user_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("admin="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/orgs"
)
req_collection.add_request(request)

# Endpoint: /v5/user/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['assigned','created','all'] , default_enum="assigned" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','progressing','closed','rejected','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("schedule="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deadline="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("finished_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/user/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['private','public','all']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("affiliation="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','owner','personal','member','public','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated','pushed','full_name'] , default_enum="full_name" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/user/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user"
)
req_collection.add_request(request)

# Endpoint: /v5/user, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user"
)
req_collection.add_request(request)

# Endpoint: /v5/user/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/followers"
)
req_collection.add_request(request)

# Endpoint: /v5/user/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/following"
)
req_collection.add_request(request)

# Endpoint: /v5/user/namespaces, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("namespaces"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("mode="),
    primitives.restler_fuzzable_group("mode", ['project','intrant','all']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/namespaces"
)
req_collection.add_request(request)

# Endpoint: /v5/user/namespace, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("namespace"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/namespace"
)
req_collection.add_request(request)

# Endpoint: /v5/user/starred, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','last_push'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/starred"
)
req_collection.add_request(request)

# Endpoint: /v5/user/subscriptions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','last_push'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/subscriptions"
)
req_collection.add_request(request)

# Endpoint: /v5/user/enterprises, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("admin="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/enterprises"
)
req_collection.add_request(request)

# Endpoint: /v5/user/memberships/orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("active="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/memberships/orgs"
)
req_collection.add_request(request)

# Endpoint: /v5/user/memberships/orgs/{org}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/memberships/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/memberships/orgs/{org}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/memberships/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/memberships/orgs/{org}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/memberships/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/following/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/following/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/following/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/following/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/following/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/following/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/starred/{owner}/{repo}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/starred/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/starred/{owner}/{repo}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("repo", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/starred/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/starred/{owner}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/starred/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/subscriptions/{owner}/{repo}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/subscriptions/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/subscriptions/{owner}/{repo}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("repo", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/subscriptions/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/user/subscriptions/{owner}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/user/subscriptions/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists"
)
req_collection.add_request(request)

# Endpoint: /v5/gists, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5gistspost,
            'dependencies':
            [
                _v5_gists_post_0_id.writer()
            ]
        }

    },

],
requestId="/v5/gists"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/starred, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/starred"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{gist_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{gist_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{gist_id}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5gistsgist_idcommentspost,
            'dependencies':
            [
                _v5_gists__gist_id__comments_post_id.writer()
            ]
        }

    },

],
requestId="/v5/gists/{gist_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{gist_id}/comments/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists__gist_id__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{gist_id}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{gist_id}/comments/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists__gist_id__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{gist_id}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{gist_id}/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists__gist_id__comments_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{gist_id}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}/commits"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}/star, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("star"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}/star"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}/star, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("star"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}/star"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}/star, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("star"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}/star"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}/forks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}/forks"
)
req_collection.add_request(request)

# Endpoint: /v5/gists/{id}/forks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_gists_post_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gists/{id}/forks"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/orgs"
)
req_collection.add_request(request)

# Endpoint: /v5/users/organization, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/organization"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','owner','personal','member'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated','pushed','full_name'] , default_enum="full_name" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/followers"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/following"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/following/{target_user}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/following/{target_user}"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/keys"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/starred, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','last_push'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/starred"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/subscriptions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','last_push'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/subscriptions"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/received_events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("received_events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/received_events"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/received_events/public, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("received_events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/received_events/public"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/events"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/events/public, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/events/public"
)
req_collection.add_request(request)

# Endpoint: /v5/users/{username}/events/orgs/{org}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/users/{username}/events/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("role="),
    primitives.restler_fuzzable_group("role", ['all','admin','member'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/members"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/followers"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['assigned','created','all'] , default_enum="assigned" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','progressing','closed','rejected','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("schedule="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deadline="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("finished_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','public','private'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/memberships/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_orgs__org__memberships__username__put_organization_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/memberships/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/memberships/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_orgs__org__memberships__username__put_organization_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/memberships/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/memberships/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("memberships"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5orgsorgmembershipsusernameput,
            'dependencies':
            [
                _v5_orgs__org__memberships__username__put_organization_id.writer()
            ]
        }

    },

],
requestId="/v5/orgs/{org}/memberships/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/orgs/{org}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/orgs/{org}/events"
)
req_collection.add_request(request)

# Endpoint: /v5/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("filter="),
    primitives.restler_fuzzable_group("filter", ['assigned','created','all'] , default_enum="assigned" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','progressing','closed','rejected','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("schedule="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deadline="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("finished_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','progressing','closed','rejected','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("schedule="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deadline="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("finished_at="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assignee="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("creator="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("program="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("role="),
    primitives.restler_fuzzable_group("role", ['all','admin','member'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/members"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/members"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/members/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query_type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("query_value="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/members/search"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_reports/{id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_reports"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/week_reports/{id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_reports/{id}/comment, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_reports"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comment"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/week_reports/{id}/comment"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_reports/{report_id}/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_reports"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/week_reports/{report_id}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/users/{username}/week_reports, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_reports"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/users/{username}/week_reports"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_reports, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_reports"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("username="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("year="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("week_index="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("date="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/week_reports"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_reports/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_reports"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/week_reports/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_report/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_report"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_enterprises__enterprise__week_report_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/week_report/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/week_report, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("week_report"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5enterprisesenterpriseweek_reportpost,
            'dependencies':
            [
                _v5_enterprises__enterprise__week_report_post_id.writer()
            ]
        }

    },

],
requestId="/v5/enterprises/{enterprise}/week_report"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/issues/{number}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/issues/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/issues/{number}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/issues/{number}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/issues/{number}/pull_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pull_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/issues/{number}/pull_requests"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/issues/{number}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/issues/{number}/comments"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/issues/{number}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/issues/{number}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/labels"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/labels/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/labels/{name}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','public','internal','private'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direct="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/repos"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/members/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_enterprises__enterprise__members__username__put_enterprise_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/members/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_enterprises__enterprise__members__username__put_enterprise_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprises/{enterprise}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprises/{enterprise}/members/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprises"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5enterprisesenterprisemembersusernameput,
            'dependencies':
            [
                _v5_enterprises__enterprise__members__username__put_enterprise_id.writer()
            ]
        }

    },

],
requestId="/v5/enterprises/{enterprise}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /v5/gitignore/templates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignore"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gitignore/templates"
)
req_collection.add_request(request)

# Endpoint: /v5/gitignore/templates/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignore"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['Actionscript','Ada','Agda','Android','Anjuta','Ansible','AppEngine','AppceleratorTitanium','ArchLinuxPackages','Archives','Autotools','Backup','Bazaar','BricxCC','C','C++','CFWheels','CMake','CUDA','CVS','CakePHP','Calabash','ChefCookbook','Clojure','Cloud9','CodeIgniter','CodeKit','CommonLisp','Composer','Concrete5','Coq','CraftCMS','D','DM','Dart','DartEditor','Delphi','Diff','Dreamweaver','Dropbox','Drupal','EPiServer','Eagle','Eclipse','EiffelStudio','Elisp','Elixir','Elm','Emacs','Ensime','Erlang','Espresso','ExpressionEngine','ExtJs','Fancy','Finale','FlexBuilder','Flutter','ForceDotCom','Fortran','FuelPHP','GPG','GWT','Gcov','GitBook','Go','Godot','Gradle','Grails','Haskell','IGORPro','Idris','Images','JBoss','JDeveloper','JENKINS_HOME','JEnv','Java','Jekyll','JetBrains','Joomla','Julia','KDevelop4','Kate','KiCad','Kohana','Kotlin','LabVIEW','Laravel','Lazarus','Leiningen','LemonStand','LibreOffice','Lilypond','Linux','Lithium','Lua','LyX','MATLAB','Magento','Maven','Mercurial','Mercury','MetaProgrammingSystem','Metals','MicrosoftOffice','MiniProgram','ModelSim','Momentics','MonoDevelop','Nanoc','NetBeans','Nim','Ninja','Node','NotepadPP','OCaml','Objective-C','Octave','Opa','OpenCart','OracleForms','Otto','PSoCCreator','Packer','Patch','Perl','Phalcon','PlayFramework','Plone','Prestashop','Processing','PuTTY','PureScript','Python','Qooxdoo','Qt','R','ROS','Rails','Raku','Redcar','Redis','RhodesRhomobile','Ruby','Rust','SBT','SCons','SVN','Sass','Scala','Scheme','Scrivener','Sdcc','SeamGen','SketchUp','SlickEdit','Smalltalk','Stata','Stella','SublimeText','SugarCRM','Swift','Symfony','SymphonyCMS','SynopsysVCS','Tags','TeX','Terraform','TextMate','Textpattern','TortoiseGit','TurboGears2','Typo3','Umbraco','Unity','UnrealEngine','VVVV','Vagrant','Vim','VirtualEnv','Virtuoso','VisualStudio','VisualStudioCode','Waf','WebMethods','Windows','WordPress','Xcode','XilinxISE','Xojo','Yeoman','Yii','ZendFramework','Zephir','macOS']  ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gitignore/templates/{name}"
)
req_collection.add_request(request)

# Endpoint: /v5/gitignore/templates/{name}/raw, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignore"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['Actionscript','Ada','Agda','Android','Anjuta','Ansible','AppEngine','AppceleratorTitanium','ArchLinuxPackages','Archives','Autotools','Backup','Bazaar','BricxCC','C','C++','CFWheels','CMake','CUDA','CVS','CakePHP','Calabash','ChefCookbook','Clojure','Cloud9','CodeIgniter','CodeKit','CommonLisp','Composer','Concrete5','Coq','CraftCMS','D','DM','Dart','DartEditor','Delphi','Diff','Dreamweaver','Dropbox','Drupal','EPiServer','Eagle','Eclipse','EiffelStudio','Elisp','Elixir','Elm','Emacs','Ensime','Erlang','Espresso','ExpressionEngine','ExtJs','Fancy','Finale','FlexBuilder','Flutter','ForceDotCom','Fortran','FuelPHP','GPG','GWT','Gcov','GitBook','Go','Godot','Gradle','Grails','Haskell','IGORPro','Idris','Images','JBoss','JDeveloper','JENKINS_HOME','JEnv','Java','Jekyll','JetBrains','Joomla','Julia','KDevelop4','Kate','KiCad','Kohana','Kotlin','LabVIEW','Laravel','Lazarus','Leiningen','LemonStand','LibreOffice','Lilypond','Linux','Lithium','Lua','LyX','MATLAB','Magento','Maven','Mercurial','Mercury','MetaProgrammingSystem','Metals','MicrosoftOffice','MiniProgram','ModelSim','Momentics','MonoDevelop','Nanoc','NetBeans','Nim','Ninja','Node','NotepadPP','OCaml','Objective-C','Octave','Opa','OpenCart','OracleForms','Otto','PSoCCreator','Packer','Patch','Perl','Phalcon','PlayFramework','Plone','Prestashop','Processing','PuTTY','PureScript','Python','Qooxdoo','Qt','R','ROS','Rails','Raku','Redcar','Redis','RhodesRhomobile','Ruby','Rust','SBT','SCons','SVN','Sass','Scala','Scheme','Scrivener','Sdcc','SeamGen','SketchUp','SlickEdit','Smalltalk','Stata','Stella','SublimeText','SugarCRM','Swift','Symfony','SymphonyCMS','SynopsysVCS','Tags','TeX','Terraform','TextMate','Textpattern','TortoiseGit','TurboGears2','Typo3','Umbraco','Unity','UnrealEngine','VVVV','Vagrant','Vim','VirtualEnv','Virtuoso','VisualStudio','VisualStudioCode','Waf','WebMethods','Windows','WordPress','Xcode','XilinxISE','Xojo','Yeoman','Yii','ZendFramework','Zephir','macOS']  ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/gitignore/templates/{name}/raw"
)
req_collection.add_request(request)

# Endpoint: /v5/licenses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/licenses"
)
req_collection.add_request(request)

# Endpoint: /v5/licenses/{license}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['MulanPSL-2.0','0BSD','AFL-3.0','AGPL-3.0','Apache-2.0','Artistic-2.0','BSD-2-Clause','BSD-3-Clause','BSD-3-Clause-Clear','BSL-1.0','CC-BY-4.0','CC-BY-SA-4.0','CC0-1.0','ECL-2.0','EPL-1.0','EPL-2.0','EUPL-1.1','EUPL-1.2','GPL-2.0','GPL-3.0','ISC','LGPL-2.1','LGPL-3.0','LPPL-1.3c','MIT','MPL-2.0','MS-PL','MS-RL','MulanPSL-1.0','MulanPubL-1.0','MulanPubL-2.0','NCSA','OFL-1.1','OSL-3.0','PostgreSQL','UPL-1.0','Unlicense','WTFPL','Zlib']  ,quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/licenses/{license}"
)
req_collection.add_request(request)

# Endpoint: /v5/licenses/{license}/raw, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['MulanPSL-2.0','0BSD','AFL-3.0','AGPL-3.0','Apache-2.0','Artistic-2.0','BSD-2-Clause','BSD-3-Clause','BSD-3-Clause-Clear','BSL-1.0','CC-BY-4.0','CC-BY-SA-4.0','CC0-1.0','ECL-2.0','EPL-1.0','EPL-2.0','EUPL-1.1','EUPL-1.2','GPL-2.0','GPL-3.0','ISC','LGPL-2.1','LGPL-3.0','LPPL-1.3c','MIT','MPL-2.0','MS-PL','MS-RL','MulanPSL-1.0','MulanPubL-1.0','MulanPubL-2.0','NCSA','OFL-1.1','OSL-3.0','PostgreSQL','UPL-1.0','Unlicense','WTFPL','Zlib']  ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/licenses/{license}/raw"
)
req_collection.add_request(request)

# Endpoint: /v5/markdown, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("markdown"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/markdown"
)
req_collection.add_request(request)

# Endpoint: /v5/enterprise/{enterprise}/pull_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enterprise"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pull_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("issue_number="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_group("repo", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("program_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','closed','merged','all'] , default_enum="open" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("head="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("base="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created','updated','popularity','long-running'] , default_enum="created" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("direction="),
    primitives.restler_fuzzable_group("direction", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone_number="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/enterprise/{enterprise}/pull_requests"
)
req_collection.add_request(request)

# Endpoint: /v5/networks/{owner}/{repo}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("networks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("prev_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/networks/{owner}/{repo}/events"
)
req_collection.add_request(request)

# Endpoint: /v5/search/repositories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("owner="),
    primitives.restler_fuzzable_group("owner", ['giteeshao'] , default_enum="giteeshao" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fork="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['Java','JavaScript','HTML','CSS','Python','C','Shell','C++','PHP','C#','TypeScript','Go','Objective-C','Android','Ruby','Assembly','Swift','NodeJS','Dart','Lua','Matlab','Perl','PowerShell','Scala','Rust','Groovy','XSLT','Verilog','R','Docker','Pascal','QML','FORTRAN','Erlang','CoffeeScript','ActionScript','Smalltalk','Delphi','ASP','Emacs Lisp','TeX/LaTeX','Visual Basic','VHDL','M','Clojure','Common Lisp','Awk','LiveScript','Elixir','Julia','Scheme','Haskell','AutoHotkey','Arduino','Ada','VimL','OCaml','D','Standard ML','Logos','Prolog','ColdFusion','Haxe','Puppet','Vala','Scilab','Racket','Coq','Slash','Eiffel','DOT','eC','Nemerle','wechat','Crystal','Kotlin','SQL','Lisp','XML','C/C++','HTML/CSS','易语言','汇编','other','Pawn','Zephir','YAML']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['last_push_at','stars_count','forks_count','watches_count']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_group("order", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/search/repositories"
)
req_collection.add_request(request)

# Endpoint: /v5/search/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("repo="),
    primitives.restler_fuzzable_group("repo", ['cfp'] , default_enum="cfp" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("language="),
    primitives.restler_fuzzable_group("language", ['Java','JavaScript','HTML','CSS','Python','C','Shell','C++','PHP','C#','TypeScript','Go','Objective-C','Android','Ruby','Assembly','Swift','NodeJS','Dart','Lua','Matlab','Perl','PowerShell','Scala','Rust','Groovy','XSLT','Verilog','R','Docker','Pascal','QML','FORTRAN','Erlang','CoffeeScript','ActionScript','Smalltalk','Delphi','ASP','Emacs Lisp','TeX/LaTeX','Visual Basic','VHDL','M','Clojure','Common Lisp','Awk','LiveScript','Elixir','Julia','Scheme','Haskell','AutoHotkey','Arduino','Ada','VimL','OCaml','D','Standard ML','Logos','Prolog','ColdFusion','Haxe','Puppet','Vala','Scilab','Racket','Coq','Slash','Eiffel','DOT','eC','Nemerle','wechat','Crystal','Kotlin','SQL','Lisp','XML','C/C++','HTML/CSS','易语言','汇编','other','Pawn','Zephir','YAML']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("label="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['open','progressing','closed','rejected']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assignee="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['created_at','updated_at','notes_count']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_group("order", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/search/issues"
)
req_collection.add_request(request)

# Endpoint: /v5/search/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['joined_at']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_group("order", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/search/users"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/count, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("count"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("unread="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/count"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/threads, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("unread="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("participating="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['all','event','referer'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/threads"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/threads, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/threads"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/threads/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/threads/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/threads/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/threads/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/messages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("unread="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ids="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_group("per_page", ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100'] , default_enum="20" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/messages"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/messages, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/messages"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/messages, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v5notificationsmessagespost,
            'dependencies':
            [
                _v5_notifications_messages_post_id.writer()
            ]
        }

    },

],
requestId="/v5/notifications/messages"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/messages/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_notifications_messages_post_id.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/messages/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/notifications/messages/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("messages"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v5_notifications_messages_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/notifications/messages/{id}"
)
req_collection.add_request(request)

# Endpoint: /v5/emails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/emails"
)
req_collection.add_request(request)

# Endpoint: /v5/emojis, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v5"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emojis"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("access_token="),
    primitives.restler_fuzzable_group("access_token", ['6acf6380ce0a8aa993eb235e62aef326'] , default_enum="6acf6380ce0a8aa993eb235e62aef326" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitee.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v5/emojis"
)
req_collection.add_request(request)
