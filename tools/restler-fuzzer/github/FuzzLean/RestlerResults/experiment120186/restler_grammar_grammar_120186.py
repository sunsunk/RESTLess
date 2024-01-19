""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_v3_groups_post_id = dependencies.DynamicVariable("_v3_groups_post_id")

_v3_groups__id__access_requests_post_id = dependencies.DynamicVariable("_v3_groups__id__access_requests_post_id")

_v3_groups__id__members_post_id = dependencies.DynamicVariable("_v3_groups__id__members_post_id")

_v3_hooks_post_id = dependencies.DynamicVariable("_v3_hooks_post_id")

_v3_projects_post_forked_from_project_id = dependencies.DynamicVariable("_v3_projects_post_forked_from_project_id")

_v3_projects__id__access_requests_post_id = dependencies.DynamicVariable("_v3_projects__id__access_requests_post_id")

_v3_projects__id__boards__board_id__lists_post_id = dependencies.DynamicVariable("_v3_projects__id__boards__board_id__lists_post_id")

_v3_projects__id__deploy_keys_post_id = dependencies.DynamicVariable("_v3_projects__id__deploy_keys_post_id")

_v3_projects__id__environments_post_id = dependencies.DynamicVariable("_v3_projects__id__environments_post_id")

_v3_projects__id__hooks_post_id = dependencies.DynamicVariable("_v3_projects__id__hooks_post_id")

_v3_projects__id__issues_post_assignee_id = dependencies.DynamicVariable("_v3_projects__id__issues_post_assignee_id")

_v3_projects__id__issues__issue_id__award_emoji_post_id = dependencies.DynamicVariable("_v3_projects__id__issues__issue_id__award_emoji_post_id")

_v3_projects__id__issues__issue_id__notes__note_id__award_emoji_post_id = dependencies.DynamicVariable("_v3_projects__id__issues__issue_id__notes__note_id__award_emoji_post_id")

_v3_projects__id__issues__noteable_id__notes_post_author_id = dependencies.DynamicVariable("_v3_projects__id__issues__noteable_id__notes_post_author_id")

_v3_projects__id__keys_post_id = dependencies.DynamicVariable("_v3_projects__id__keys_post_id")

_v3_projects__id__labels_put_id = dependencies.DynamicVariable("_v3_projects__id__labels_put_id")

_v3_projects__id__members_post_id = dependencies.DynamicVariable("_v3_projects__id__members_post_id")

_v3_projects__id__merge_request__merge_request_id__put_id = dependencies.DynamicVariable("_v3_projects__id__merge_request__merge_request_id__put_id")

_v3_projects__id__merge_requests_post_assignee_id = dependencies.DynamicVariable("_v3_projects__id__merge_requests_post_assignee_id")

_v3_projects__id__merge_requests__merge_request_id__award_emoji_post_id = dependencies.DynamicVariable("_v3_projects__id__merge_requests__merge_request_id__award_emoji_post_id")

_v3_projects__id__merge_requests__merge_request_id__notes__note_id__award_emoji_post_id = dependencies.DynamicVariable("_v3_projects__id__merge_requests__merge_request_id__notes__note_id__award_emoji_post_id")

_v3_projects__id__merge_requests__noteable_id__notes_post_author_id = dependencies.DynamicVariable("_v3_projects__id__merge_requests__noteable_id__notes_post_author_id")

_v3_projects__id__milestones_post_id = dependencies.DynamicVariable("_v3_projects__id__milestones_post_id")

_v3_projects__id__repository_tags_post_name = dependencies.DynamicVariable("_v3_projects__id__repository_tags_post_name")

_v3_projects__id__runners_post_id = dependencies.DynamicVariable("_v3_projects__id__runners_post_id")

_v3_projects__id__share_post_id = dependencies.DynamicVariable("_v3_projects__id__share_post_id")

_v3_projects__id__snippets_post_author_id = dependencies.DynamicVariable("_v3_projects__id__snippets_post_author_id")

_v3_projects__id__snippets__noteable_id__notes_post_author_id = dependencies.DynamicVariable("_v3_projects__id__snippets__noteable_id__notes_post_author_id")

_v3_projects__id__snippets__snippet_id__award_emoji_post_id = dependencies.DynamicVariable("_v3_projects__id__snippets__snippet_id__award_emoji_post_id")

_v3_projects__id__snippets__snippet_id__notes__note_id__award_emoji_post_id = dependencies.DynamicVariable("_v3_projects__id__snippets__snippet_id__notes__note_id__award_emoji_post_id")

_v3_projects__id__triggers_post_token = dependencies.DynamicVariable("_v3_projects__id__triggers_post_token")

_v3_projects__id__variables_post_key = dependencies.DynamicVariable("_v3_projects__id__variables_post_key")

_v3_runners__id__put_id = dependencies.DynamicVariable("_v3_runners__id__put_id")

_v3_snippets_post_author_id = dependencies.DynamicVariable("_v3_snippets_post_author_id")

_v3_user_emails_post_id = dependencies.DynamicVariable("_v3_user_emails_post_id")

_v3_user_keys_post_id = dependencies.DynamicVariable("_v3_user_keys_post_id")

_v3_users_post_id = dependencies.DynamicVariable("_v3_users_post_id")

_v3_users__id__emails_post_id = dependencies.DynamicVariable("_v3_users__id__emails_post_id")

_v3_users__id__keys_post_id = dependencies.DynamicVariable("_v3_users__id__keys_post_id")

def parse_v3groupspost(data, **kwargs):
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
        dependencies.set_variable("_v3_groups_post_id", temp_7262)


def parse_v3groupsidaccess_requestspost(data, **kwargs):
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
            temp_8173 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_v3_groups__id__access_requests_post_id", temp_8173)


def parse_v3groupsidmemberspost(data, **kwargs):
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
            temp_7680 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7680:
        dependencies.set_variable("_v3_groups__id__members_post_id", temp_7680)


def parse_v3hookspost(data, **kwargs):
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
            temp_5581 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5581):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5581:
        dependencies.set_variable("_v3_hooks_post_id", temp_5581)


def parse_v3projectspost(data, **kwargs):
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
            temp_2060 = str(data["forked_from_project"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2060):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2060:
        dependencies.set_variable("_v3_projects_post_forked_from_project_id", temp_2060)


def parse_v3projectsidaccess_requestspost(data, **kwargs):
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
        dependencies.set_variable("_v3_projects__id__access_requests_post_id", temp_5588)


def parse_v3projectsidboardsboard_idlistspost(data, **kwargs):
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
        dependencies.set_variable("_v3_projects__id__boards__board_id__lists_post_id", temp_9060)


def parse_v3projectsiddeploy_keyspost(data, **kwargs):
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
            temp_4421 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4421):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4421:
        dependencies.set_variable("_v3_projects__id__deploy_keys_post_id", temp_4421)


def parse_v3projectsidenvironmentspost(data, **kwargs):
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
            temp_9775 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9775):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9775:
        dependencies.set_variable("_v3_projects__id__environments_post_id", temp_9775)


def parse_v3projectsidhookspost(data, **kwargs):
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
        dependencies.set_variable("_v3_projects__id__hooks_post_id", temp_2737)


def parse_v3projectsidissuespost(data, **kwargs):
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
            temp_2919 = str(data["assignee"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2919):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2919:
        dependencies.set_variable("_v3_projects__id__issues_post_assignee_id", temp_2919)


def parse_v3projectsidissuesissue_idaward_emojipost(data, **kwargs):
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
        dependencies.set_variable("_v3_projects__id__issues__issue_id__award_emoji_post_id", temp_4673)


def parse_v3projectsidissuesissue_idnotesnote_idaward_emojipost(data, **kwargs):
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
            temp_6326 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6326:
        dependencies.set_variable("_v3_projects__id__issues__issue_id__notes__note_id__award_emoji_post_id", temp_6326)


def parse_v3projectsidissuesnoteable_idnotespost(data, **kwargs):
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
            temp_4695 = str(data["author"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4695):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4695:
        dependencies.set_variable("_v3_projects__id__issues__noteable_id__notes_post_author_id", temp_4695)


def parse_v3projectsidkeyspost(data, **kwargs):
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
            temp_9821 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9821):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9821:
        dependencies.set_variable("_v3_projects__id__keys_post_id", temp_9821)


def parse_v3projectsidlabelsput(data, **kwargs):
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
        dependencies.set_variable("_v3_projects__id__labels_put_id", temp_303)


def parse_v3projectsidmemberspost(data, **kwargs):
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
            temp_8623 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8623):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8623:
        dependencies.set_variable("_v3_projects__id__members_post_id", temp_8623)


def parse_v3projectsidmerge_requestmerge_request_idput(data, **kwargs):
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
        dependencies.set_variable("_v3_projects__id__merge_request__merge_request_id__put_id", temp_9953)


def parse_v3projectsidmerge_requestspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6771 = None

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
            temp_6771 = str(data["assignee"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6771):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6771:
        dependencies.set_variable("_v3_projects__id__merge_requests_post_assignee_id", temp_6771)


def parse_v3projectsidmerge_requestsmerge_request_idaward_emojipost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_3145 = None

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
            temp_3145 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_3145):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_3145:
        dependencies.set_variable("_v3_projects__id__merge_requests__merge_request_id__award_emoji_post_id", temp_3145)


def parse_v3projectsidmerge_requestsmerge_request_idnotesnote_idaward_emojipost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8169 = None

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
            temp_8169 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8169):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8169:
        dependencies.set_variable("_v3_projects__id__merge_requests__merge_request_id__notes__note_id__award_emoji_post_id", temp_8169)


def parse_v3projectsidmerge_requestsnoteable_idnotespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8480 = None

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
            temp_8480 = str(data["author"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8480):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8480:
        dependencies.set_variable("_v3_projects__id__merge_requests__noteable_id__notes_post_author_id", temp_8480)


def parse_v3projectsidmilestonespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9919 = None

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
            temp_9919 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9919):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9919:
        dependencies.set_variable("_v3_projects__id__milestones_post_id", temp_9919)


def parse_v3projectsidrepositorytagspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_326 = None

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
            temp_326 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_326):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_326:
        dependencies.set_variable("_v3_projects__id__repository_tags_post_name", temp_326)


def parse_v3projectsidrunnerspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6999 = None

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
            temp_6999 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6999):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6999:
        dependencies.set_variable("_v3_projects__id__runners_post_id", temp_6999)


def parse_v3projectsidsharepost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5262 = None

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
            temp_5262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5262:
        dependencies.set_variable("_v3_projects__id__share_post_id", temp_5262)


def parse_v3projectsidsnippetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9340 = None

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
            temp_9340 = str(data["author"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9340):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9340:
        dependencies.set_variable("_v3_projects__id__snippets_post_author_id", temp_9340)


def parse_v3projectsidsnippetsnoteable_idnotespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6876 = None

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
            temp_6876 = str(data["author"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6876):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6876:
        dependencies.set_variable("_v3_projects__id__snippets__noteable_id__notes_post_author_id", temp_6876)


def parse_v3projectsidsnippetssnippet_idaward_emojipost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_5468 = None

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
            temp_5468 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_5468):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_5468:
        dependencies.set_variable("_v3_projects__id__snippets__snippet_id__award_emoji_post_id", temp_5468)


def parse_v3projectsidsnippetssnippet_idnotesnote_idaward_emojipost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_811 = None

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
            temp_811 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_811):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_811:
        dependencies.set_variable("_v3_projects__id__snippets__snippet_id__notes__note_id__award_emoji_post_id", temp_811)


def parse_v3projectsidtriggerspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_1871 = None

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
            temp_1871 = str(data["token"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_1871):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_1871:
        dependencies.set_variable("_v3_projects__id__triggers_post_token", temp_1871)


def parse_v3projectsidvariablespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4533 = None

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
            temp_4533 = str(data["key"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4533):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4533:
        dependencies.set_variable("_v3_projects__id__variables_post_key", temp_4533)


def parse_v3runnersidput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2971 = None

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
            temp_2971 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2971):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2971:
        dependencies.set_variable("_v3_runners__id__put_id", temp_2971)


def parse_v3snippetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9885 = None

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
            temp_9885 = str(data["author"]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9885):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9885:
        dependencies.set_variable("_v3_snippets_post_author_id", temp_9885)


def parse_v3useremailspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6426 = None

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
            temp_6426 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6426):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6426:
        dependencies.set_variable("_v3_user_emails_post_id", temp_6426)


def parse_v3userkeyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7629 = None

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
            temp_7629 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7629):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7629:
        dependencies.set_variable("_v3_user_keys_post_id", temp_7629)


def parse_v3userspost(data, **kwargs):
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
        dependencies.set_variable("_v3_users_post_id", temp_303)


def parse_v3usersidemailspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_3810 = None

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
            temp_3810 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_3810):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_3810:
        dependencies.set_variable("_v3_users__id__emails_post_id", temp_3810)


def parse_v3usersidkeyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_3431 = None

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
            temp_3431 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_3431):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_3431:
        dependencies.set_variable("_v3_users__id__keys_post_id", temp_3431)

req_collection = requests.RequestCollection([])
# Endpoint: /v3/application/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("application"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/application/settings"
)
req_collection.add_request(request)

# Endpoint: /v3/application/settings, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("application"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/application/settings"
)
req_collection.add_request(request)

# Endpoint: /v3/ci/lint, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ci"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lint"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/ci/lint"
)
req_collection.add_request(request)

# Endpoint: /v3/deploy_keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/deploy_keys"
)
req_collection.add_request(request)

# Endpoint: /v3/dockerfiles, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dockerfiles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/dockerfiles"
)
req_collection.add_request(request)

# Endpoint: /v3/dockerfiles/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dockerfiles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/dockerfiles/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/gitignores, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignores"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/gitignores"
)
req_collection.add_request(request)

# Endpoint: /v3/gitignores/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignores"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/gitignores/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/gitlab_ci_ymls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitlab_ci_ymls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/gitlab_ci_ymls"
)
req_collection.add_request(request)

# Endpoint: /v3/gitlab_ci_ymls/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitlab_ci_ymls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/gitlab_ci_ymls/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("statistics="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("all_available="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['name','path'] , default_enum="name" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="asc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups"
)
req_collection.add_request(request)

# Endpoint: /v3/groups, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3groupspost,
            'dependencies':
            [
                _v3_groups_post_id.writer()
            ]
        }

    },

],
requestId="/v3/groups"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/owned, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owned"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("statistics="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/owned"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/access_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/access_requests"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/access_requests, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3groupsidaccess_requestspost,
            'dependencies':
            [
                _v3_groups__id__access_requests_post_id.writer()
            ]
        }

    },

],
requestId="/v3/groups/{id}/access_requests"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/access_requests/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups__id__access_requests_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/access_requests/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/access_requests/{user_id}/approve, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups__id__access_requests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("approve"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/access_requests/{user_id}/approve"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['opened','closed','all'] , default_enum="opened" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['created_at','updated_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/issues"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/members"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3groupsidmemberspost,
            'dependencies':
            [
                _v3_groups__id__members_post_id.writer()
            ]
        }

    },

],
requestId="/v3/groups/{id}/members"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/members/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups__id__members_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/members/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/members/{user_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups__id__members_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/members/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/members/{user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups__id__members_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/members/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/notification_settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notification_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/notification_settings"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/notification_settings, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notification_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/notification_settings"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['public','internal','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("simple="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/projects"
)
req_collection.add_request(request)

# Endpoint: /v3/groups/{id}/projects/{project_id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("groups"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_groups_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/groups/{id}/projects/{project_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/hooks"
)
req_collection.add_request(request)

# Endpoint: /v3/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3hookspost,
            'dependencies':
            [
                _v3_hooks_post_id.writer()
            ]
        }

    },

],
requestId="/v3/hooks"
)
req_collection.add_request(request)

# Endpoint: /v3/hooks/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/hooks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/allowed, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("allowed"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/allowed"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/broadcast_message, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("broadcast_message"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/broadcast_message"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/check, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("check"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/check"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/discover, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("discover"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/discover"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/lfs_authenticate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lfs_authenticate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/lfs_authenticate"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/merge_request_urls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request_urls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/merge_request_urls"
)
req_collection.add_request(request)

# Endpoint: /v3/internal/two_factor_recovery_codes, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("internal"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("two_factor_recovery_codes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/internal/two_factor_recovery_codes"
)
req_collection.add_request(request)

# Endpoint: /v3/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['opened','closed','all'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['created_at','updated_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/issues"
)
req_collection.add_request(request)

# Endpoint: /v3/keys/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/licenses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("popular="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/licenses"
)
req_collection.add_request(request)

# Endpoint: /v3/licenses/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/licenses/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/namespaces, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("namespaces"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/namespaces"
)
req_collection.add_request(request)

# Endpoint: /v3/notification_settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notification_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/notification_settings"
)
req_collection.add_request(request)

# Endpoint: /v3/notification_settings, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notification_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/notification_settings"
)
req_collection.add_request(request)

# Endpoint: /v3/projects, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['public','internal','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("simple="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects"
)
req_collection.add_request(request)

# Endpoint: /v3/projects, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectspost,
            'dependencies':
            [
                _v3_projects_post_forked_from_project_id.writer()
            ]
        }

    },

],
requestId="/v3/projects"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/all, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("all"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['public','internal','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("simple="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("statistics="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/all"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/fork/{id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fork"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/fork/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/owned, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("owned"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['public','internal','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("simple="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("statistics="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/owned"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/search/{query}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/search/{query}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/starred, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['public','internal','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("simple="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/starred"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/user/{user_id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/user/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/visible, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("visible"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['id','name','path','created_at','updated_at','last_activity_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("visibility="),
    primitives.restler_fuzzable_group("visibility", ['public','internal','private']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("simple="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/visible"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/(ref/{ref}/)trigger/builds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("(ref"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(")trigger"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/(ref/{ref}/)trigger/builds"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/access_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/access_requests"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/access_requests, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidaccess_requestspost,
            'dependencies':
            [
                _v3_projects__id__access_requests_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/access_requests"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/access_requests/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__access_requests_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/access_requests/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/access_requests/{user_id}/approve, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("access_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__access_requests_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("approve"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/access_requests/{user_id}/approve"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/archive, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/archive"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/boards, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boards"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/boards"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/boards/{board_id}/lists, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/boards/{board_id}/lists"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/boards/{board_id}/lists, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lists"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidboardsboard_idlistspost,
            'dependencies':
            [
                _v3_projects__id__boards__board_id__lists_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/boards/{board_id}/lists"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/boards/{board_id}/lists/{list_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__boards__board_id__lists_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/boards/{board_id}/lists/{list_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/boards/{board_id}/lists/{list_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__boards__board_id__lists_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/boards/{board_id}/lists/{list_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/boards/{board_id}/lists/{list_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("boards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("lists"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__boards__board_id__lists_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/boards/{board_id}/lists/{list_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_group("scope", ['pending','running','failed','success','canceled']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/artifacts/{ref_name}/download, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artifacts"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("download"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("job="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/artifacts/{ref_name}/download"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/artifacts, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artifacts"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/artifacts"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/artifacts/keep, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("artifacts"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keep"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/artifacts/keep"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/cancel, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cancel"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/cancel"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/erase, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("erase"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/erase"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/play, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("play"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/play"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/retry, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("retry"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/retry"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/builds/{build_id}/trace, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trace"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/builds/{build_id}/trace"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deploy_keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deploy_keys"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deploy_keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsiddeploy_keyspost,
            'dependencies':
            [
                _v3_projects__id__deploy_keys_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/deploy_keys"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deploy_keys/{key_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__deploy_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deploy_keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deploy_keys/{key_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__deploy_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deploy_keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deploy_keys/{key_id}/disable, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__deploy_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("disable"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deploy_keys/{key_id}/disable"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deploy_keys/{key_id}/enable, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deploy_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__deploy_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enable"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deploy_keys/{key_id}/enable"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deployments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deployments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/deployments/{deployment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/deployments/{deployment_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/environments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("environments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/environments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/environments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("environments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidenvironmentspost,
            'dependencies':
            [
                _v3_projects__id__environments_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/environments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/environments/{environment_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("environments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__environments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/environments/{environment_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/environments/{environment_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("environments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__environments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/environments/{environment_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/events"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/fork, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fork"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/fork"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/fork/{forked_from_id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("fork"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/fork/{forked_from_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/hooks"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidhookspost,
            'dependencies':
            [
                _v3_projects__id__hooks_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/hooks"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/hooks/{hook_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/hooks/{hook_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/hooks/{hook_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/hooks/{hook_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/hooks/{hook_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/hooks/{hook_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['opened','closed','all'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("iid="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['created_at','updated_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidissuespost,
            'dependencies':
            [
                _v3_projects__id__issues_post_assignee_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/issues"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/add_spent_time, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("add_spent_time"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/add_spent_time"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/award_emoji, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/award_emoji, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidissuesissue_idaward_emojipost,
            'dependencies':
            [
                _v3_projects__id__issues__issue_id__award_emoji_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/issues/{issue_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__issue_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__issue_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/move, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("move"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/move"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidissuesissue_idnotesnote_idaward_emojipost,
            'dependencies':
            [
                _v3_projects__id__issues__issue_id__notes__note_id__award_emoji_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__issue_id__notes__note_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__issue_id__notes__note_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/notes/{note_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/reset_spent_time, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reset_spent_time"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/reset_spent_time"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/reset_time_estimate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reset_time_estimate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/reset_time_estimate"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/time_estimate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("time_estimate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/time_estimate"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/time_stats, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("time_stats"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/time_stats"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{issue_id}/todo, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("todo"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{issue_id}/todo"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{noteable_id}/notes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{noteable_id}/notes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{noteable_id}/notes, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidissuesnoteable_idnotespost,
            'dependencies':
            [
                _v3_projects__id__issues__noteable_id__notes_post_author_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/issues/{noteable_id}/notes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{noteable_id}/notes/{note_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{noteable_id}/notes/{note_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{noteable_id}/notes/{note_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{subscribable_id}/subscription, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/issues/{subscribable_id}/subscription, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__issues_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/issues/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/keys"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidkeyspost,
            'dependencies':
            [
                _v3_projects__id__keys_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/keys"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/keys/{key_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/keys/{key_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/keys/{key_id}/disable, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("disable"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/keys/{key_id}/disable"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/keys/{key_id}/enable, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("enable"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/keys/{key_id}/enable"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/labels, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/labels"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/labels"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/labels"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/labels, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidlabelsput,
            'dependencies':
            [
                _v3_projects__id__labels_put_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/labels"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/labels/{subscribable_id}/subscription, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__labels_put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/labels/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/labels/{subscribable_id}/subscription, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__labels_put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/labels/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/members"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/members, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmemberspost,
            'dependencies':
            [
                _v3_projects__id__members_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/members"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/members/{user_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__members_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/members/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/members/{user_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__members_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/members/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/members/{user_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__members_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/members/{user_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("merge_request_id", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmerge_requestmerge_request_idput,
            'dependencies':
            [
                _v3_projects__id__merge_request__merge_request_id__put_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/cancel_merge_when_build_succeeds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cancel_merge_when_build_succeeds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/cancel_merge_when_build_succeeds"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/changes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/changes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/closes_issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("closes_issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/closes_issues"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/commits"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{merge_request_id}/merge, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_request__merge_request_id__put_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{merge_request_id}/merge"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{subscribable_id}/subscription, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_request/{subscribable_id}/subscription, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_request"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_request/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['opened','closed','merged','all'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order_by="),
    primitives.restler_fuzzable_group("order_by", ['created_at','updated_at'] , default_enum="created_at" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['asc','desc'] , default_enum="desc" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmerge_requestspost,
            'dependencies':
            [
                _v3_projects__id__merge_requests_post_assignee_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/merge_requests"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/add_spent_time, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("add_spent_time"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/add_spent_time"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmerge_requestsmerge_request_idaward_emojipost,
            'dependencies':
            [
                _v3_projects__id__merge_requests__merge_request_id__award_emoji_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__merge_request_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__merge_request_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/cancel_merge_when_build_succeeds, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cancel_merge_when_build_succeeds"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/cancel_merge_when_build_succeeds"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/changes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("changes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/changes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/closes_issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("closes_issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/closes_issues"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/comments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/commits"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/merge, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/merge"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmerge_requestsmerge_request_idnotesnote_idaward_emojipost,
            'dependencies':
            [
                _v3_projects__id__merge_requests__merge_request_id__notes__note_id__award_emoji_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__merge_request_id__notes__note_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__merge_request_id__notes__note_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/notes/{note_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/reset_spent_time, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reset_spent_time"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/reset_spent_time"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/reset_time_estimate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reset_time_estimate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/reset_time_estimate"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/time_estimate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("time_estimate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/time_estimate"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/time_stats, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("time_stats"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/time_stats"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/todo, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("todo"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/todo"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/versions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("versions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/versions"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{merge_request_id}/versions/{version_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("versions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{merge_request_id}/versions/{version_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{noteable_id}/notes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{noteable_id}/notes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{noteable_id}/notes, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmerge_requestsnoteable_idnotespost,
            'dependencies':
            [
                _v3_projects__id__merge_requests__noteable_id__notes_post_author_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/merge_requests/{noteable_id}/notes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{subscribable_id}/subscription, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/merge_requests/{subscribable_id}/subscription, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge_requests"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__merge_requests_post_assignee_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/merge_requests/{subscribable_id}/subscription"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/milestones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['active','closed','all'] , default_enum="all" ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/milestones"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/milestones, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidmilestonespost,
            'dependencies':
            [
                _v3_projects__id__milestones_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/milestones"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/milestones/{milestone_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__milestones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/milestones/{milestone_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/milestones/{milestone_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__milestones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/milestones/{milestone_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/milestones/{milestone_id}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__milestones_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/milestones/{milestone_id}/issues"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/notification_settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notification_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/notification_settings"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/notification_settings, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notification_settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/notification_settings"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/pipeline, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipeline"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/pipeline"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/pipelines, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_group("scope", ['running','branches','tags']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/pipelines"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/pipelines/{pipeline_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/pipelines/{pipeline_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/pipelines/{pipeline_id}/cancel, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cancel"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/pipelines/{pipeline_id}/cancel"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/pipelines/{pipeline_id}/retry, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("retry"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/pipelines/{pipeline_id}/retry"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/archive, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sha="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("format="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/archive"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/blobs/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blobs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filepath="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/blobs/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/branches, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/branches"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/branches, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/branches"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/branches/{branch}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/branches/{branch}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/branches/{branch}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/branches/{branch}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/branches/{branch}/protect, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("protect"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/branches/{branch}/protect"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/branches/{branch}/unprotect, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unprotect"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/branches/{branch}/unprotect"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref_name="),
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
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/blob, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blob"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("filepath="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/blob"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/builds, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_group("scope", ['pending','running','failed','success','canceled']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/builds"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/cherry_pick, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cherry_pick"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/cherry_pick"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/comments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/comments"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/diff, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("diff"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/diff"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/commits/{sha}/statuses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stage="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/commits/{sha}/statuses"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/compare, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("compare"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("from="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/compare"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/contributors, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contributors"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/contributors"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/files, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("file_path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("branch_name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("commit_message="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author_email="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("author_name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/files"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("file_path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/files"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/files, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/files"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/files, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/files"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/merged_branches, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merged_branches"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/merged_branches"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/raw_blobs/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw_blobs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/raw_blobs/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/tags"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tags, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidrepositorytagspost,
            'dependencies':
            [
                _v3_projects__id__repository_tags_post_name.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/repository/tags"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tags/{tag_name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__repository_tags_post_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/tags/{tag_name}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tags/{tag_name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__repository_tags_post_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/tags/{tag_name}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tags/{tag_name}/release, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__repository_tags_post_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("release"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/tags/{tag_name}/release"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tags/{tag_name}/release, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__repository_tags_post_name.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("release"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/tags/{tag_name}/release"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/repository/tree, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tree"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref_name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("recursive="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/repository/tree"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/runners, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_group("scope", ['active','paused','online','specific','shared']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/runners"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/runners, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidrunnerspost,
            'dependencies':
            [
                _v3_projects__id__runners_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/runners"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/runners/{runner_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__runners_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/runners/{runner_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/asana, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("asana"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/asana"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/assembla, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assembla"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/assembla"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/bamboo, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("bamboo"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/bamboo"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/bugzilla, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("bugzilla"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/bugzilla"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/buildkite, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("buildkite"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/buildkite"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/builds-email, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("builds-email"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/builds-email"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/campfire, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("campfire"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/campfire"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/custom-issue-tracker, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("custom-issue-tracker"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/custom-issue-tracker"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/drone-ci, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("drone-ci"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/drone-ci"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/emails-on-push, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails-on-push"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/emails-on-push"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/external-wiki, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("external-wiki"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/external-wiki"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/flowdock, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("flowdock"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/flowdock"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/gemnasium, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gemnasium"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/gemnasium"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/hipchat, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hipchat"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/hipchat"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/irker, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("irker"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/irker"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/jira, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("jira"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/jira"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/kubernetes, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("kubernetes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/kubernetes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/mattermost, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mattermost"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/mattermost"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/mattermost-slash-commands, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mattermost-slash-commands"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/mattermost-slash-commands"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/mattermost_slash_commands/trigger, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mattermost_slash_commands"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trigger"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/mattermost_slash_commands/trigger"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/pipelines-email, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pipelines-email"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/pipelines-email"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/pivotaltracker, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pivotaltracker"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/pivotaltracker"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/pushover, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pushover"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/pushover"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/redmine, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("redmine"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/redmine"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/slack, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("slack"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/slack"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/slack-slash-commands, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("slack-slash-commands"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/slack-slash-commands"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/slack_slash_commands/trigger, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("slack_slash_commands"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trigger"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/slack_slash_commands/trigger"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/teamcity, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teamcity"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/teamcity"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/{service_slug}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['asana','assembla','bamboo','bugzilla','buildkite','builds-email','campfire','custom-issue-tracker','drone-ci','emails-on-push','external-wiki','flowdock','gemnasium','hipchat','irker','jira','kubernetes','mattermost-slash-commands','slack-slash-commands','pipelines-email','pivotaltracker','pushover','redmine','slack','mattermost','teamcity']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/{service_slug}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/services/{service_slug}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("services"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("", ['asana','assembla','bamboo','bugzilla','buildkite','builds-email','campfire','custom-issue-tracker','drone-ci','emails-on-push','external-wiki','flowdock','gemnasium','hipchat','irker','jira','kubernetes','mattermost-slash-commands','slack-slash-commands','pipelines-email','pivotaltracker','pushover','redmine','slack','mattermost','teamcity']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/services/{service_slug}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/share, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("share"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidsharepost,
            'dependencies':
            [
                _v3_projects__id__share_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/share"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/share/{group_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("share"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__share_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/share/{group_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidsnippetspost,
            'dependencies':
            [
                _v3_projects__id__snippets_post_author_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/snippets"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{noteable_id}/notes, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{noteable_id}/notes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{noteable_id}/notes, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidsnippetsnoteable_idnotespost,
            'dependencies':
            [
                _v3_projects__id__snippets__noteable_id__notes_post_author_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/snippets/{noteable_id}/notes"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__noteable_id__notes_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{noteable_id}/notes/{note_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/award_emoji, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/award_emoji, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidsnippetssnippet_idaward_emojipost,
            'dependencies':
            [
                _v3_projects__id__snippets__snippet_id__award_emoji_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__snippet_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__snippet_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidsnippetssnippet_idnotesnote_idaward_emojipost,
            'dependencies':
            [
                _v3_projects__id__snippets__snippet_id__notes__note_id__award_emoji_post_id.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__snippet_id__notes__note_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("award_emoji"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets__snippet_id__notes__note_id__award_emoji_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/notes/{note_id}/award_emoji/{award_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/snippets/{snippet_id}/raw, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/snippets/{snippet_id}/raw"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/star, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("star"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/star"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/star, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("star"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/star"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/statuses/{sha}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/statuses/{sha}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/triggers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("triggers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/triggers"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/triggers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("triggers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidtriggerspost,
            'dependencies':
            [
                _v3_projects__id__triggers_post_token.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/triggers"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/triggers/{token}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("triggers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__triggers_post_token.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/triggers/{token}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/triggers/{token}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("triggers"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__triggers_post_token.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/triggers/{token}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/unarchive, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unarchive"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/unarchive"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/uploads, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("uploads"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/uploads"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/users"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/variables, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/variables"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/variables, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3projectsidvariablespost,
            'dependencies':
            [
                _v3_projects__id__variables_post_key.writer()
            ]
        }

    },

],
requestId="/v3/projects/{id}/variables"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/variables/{key}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__variables_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/variables/{key}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/variables/{key}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__variables_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/variables/{key}"
)
req_collection.add_request(request)

# Endpoint: /v3/projects/{id}/variables/{key}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("projects"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects_post_forked_from_project_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("variables"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_projects__id__variables_post_key.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/projects/{id}/variables/{key}"
)
req_collection.add_request(request)

# Endpoint: /v3/runners, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_group("scope", ['active','paused','online']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/runners"
)
req_collection.add_request(request)

# Endpoint: /v3/runners/all, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("all"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("scope="),
    primitives.restler_fuzzable_group("scope", ['active','paused','online','specific','shared']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/runners/all"
)
req_collection.add_request(request)

# Endpoint: /v3/runners/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_runners__id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/runners/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/runners/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_runners__id__put_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/runners/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/runners/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("runners"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("id", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3runnersidput,
            'dependencies':
            [
                _v3_runners__id__put_id.writer()
            ]
        }

    },

],
requestId="/v3/runners/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/session, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("session"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/session"
)
req_collection.add_request(request)

# Endpoint: /v3/sidekiq/compound_metrics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sidekiq"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("compound_metrics"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/sidekiq/compound_metrics"
)
req_collection.add_request(request)

# Endpoint: /v3/sidekiq/job_stats, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sidekiq"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("job_stats"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/sidekiq/job_stats"
)
req_collection.add_request(request)

# Endpoint: /v3/sidekiq/process_metrics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sidekiq"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("process_metrics"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/sidekiq/process_metrics"
)
req_collection.add_request(request)

# Endpoint: /v3/sidekiq/queue_metrics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("sidekiq"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("queue_metrics"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/sidekiq/queue_metrics"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/snippets"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3snippetspost,
            'dependencies':
            [
                _v3_snippets_post_author_id.writer()
            ]
        }

    },

],
requestId="/v3/snippets"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets/public, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/snippets/public"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/snippets/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/snippets/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/snippets/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/snippets/{id}/raw, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("snippets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_snippets_post_author_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/snippets/{id}/raw"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/dockerfiles, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dockerfiles"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/dockerfiles"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/dockerfiles/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dockerfiles"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/dockerfiles/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/gitignores, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignores"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/gitignores"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/gitignores/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitignores"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/gitignores/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/gitlab_ci_ymls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitlab_ci_ymls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/gitlab_ci_ymls"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/gitlab_ci_ymls/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gitlab_ci_ymls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/gitlab_ci_ymls/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/licenses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("popular="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/licenses"
)
req_collection.add_request(request)

# Endpoint: /v3/templates/licenses/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("templates"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("licenses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/templates/licenses/{name}"
)
req_collection.add_request(request)

# Endpoint: /v3/todos, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("todos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/todos"
)
req_collection.add_request(request)

# Endpoint: /v3/todos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("todos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/todos"
)
req_collection.add_request(request)

# Endpoint: /v3/todos/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("todos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/todos/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user"
)
req_collection.add_request(request)

# Endpoint: /v3/user/emails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user/emails"
)
req_collection.add_request(request)

# Endpoint: /v3/user/emails, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3useremailspost,
            'dependencies':
            [
                _v3_user_emails_post_id.writer()
            ]
        }

    },

],
requestId="/v3/user/emails"
)
req_collection.add_request(request)

# Endpoint: /v3/user/emails/{email_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_user_emails_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user/emails/{email_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/user/emails/{email_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_user_emails_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user/emails/{email_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/user/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user/keys"
)
req_collection.add_request(request)

# Endpoint: /v3/user/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3userkeyspost,
            'dependencies':
            [
                _v3_user_keys_post_id.writer()
            ]
        }

    },

],
requestId="/v3/user/keys"
)
req_collection.add_request(request)

# Endpoint: /v3/user/keys/{key_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_user_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user/keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/user/keys/{key_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_user_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/user/keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("username="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("search="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("active="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("external="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("blocked="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users"
)
req_collection.add_request(request)

# Endpoint: /v3/users, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3userspost,
            'dependencies':
            [
                _v3_users_post_id.writer()
            ]
        }

    },

],
requestId="/v3/users"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/block, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("block"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/block"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/emails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/emails"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/emails, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3usersidemailspost,
            'dependencies':
            [
                _v3_users__id__emails_post_id.writer()
            ]
        }

    },

],
requestId="/v3/users/{id}/emails"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/emails/{email_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users__id__emails_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/emails/{email_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/events, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("events"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/events"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/keys"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_v3usersidkeyspost,
            'dependencies':
            [
                _v3_users__id__keys_post_id.writer()
            ]
        }

    },

],
requestId="/v3/users/{id}/keys"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/keys/{key_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users__id__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/keys/{key_id}"
)
req_collection.add_request(request)

# Endpoint: /v3/users/{id}/unblock, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_v3_users_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unblock"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/users/{id}/unblock"
)
req_collection.add_request(request)

# Endpoint: /v3/version, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("v3"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: gitlab.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/v3/version"
)
req_collection.add_request(request)
