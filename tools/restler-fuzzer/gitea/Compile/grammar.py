""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_admin_hooks_post_id = dependencies.DynamicVariable("_admin_hooks_post_id")

_admin_users_post_active = dependencies.DynamicVariable("_admin_users_post_active")

_admin_users_post_description = dependencies.DynamicVariable("_admin_users_post_description")

_admin_users_post_email = dependencies.DynamicVariable("_admin_users_post_email")

_admin_users_post_full_name = dependencies.DynamicVariable("_admin_users_post_full_name")

_admin_users_post_id = dependencies.DynamicVariable("_admin_users_post_id")

_admin_users_post_location = dependencies.DynamicVariable("_admin_users_post_location")

_admin_users_post_login = dependencies.DynamicVariable("_admin_users_post_login")

_admin_users_post_login_name = dependencies.DynamicVariable("_admin_users_post_login_name")

_admin_users_post_restricted = dependencies.DynamicVariable("_admin_users_post_restricted")

_admin_users_post_visibility = dependencies.DynamicVariable("_admin_users_post_visibility")

_admin_users_post_website = dependencies.DynamicVariable("_admin_users_post_website")

_admin_users__username__keys_post_id = dependencies.DynamicVariable("_admin_users__username__keys_post_id")

_orgs__org__hooks_post_id = dependencies.DynamicVariable("_orgs__org__hooks_post_id")

_orgs__org__labels_post_id = dependencies.DynamicVariable("_orgs__org__labels_post_id")

_orgs__org__teams_post_can_create_org_repo = dependencies.DynamicVariable("_orgs__org__teams_post_can_create_org_repo")

_orgs__org__teams_post_description = dependencies.DynamicVariable("_orgs__org__teams_post_description")

_orgs__org__teams_post_includes_all_repositories = dependencies.DynamicVariable("_orgs__org__teams_post_includes_all_repositories")

_orgs__org__teams_post_name = dependencies.DynamicVariable("_orgs__org__teams_post_name")

_orgs__org__teams_post_permission = dependencies.DynamicVariable("_orgs__org__teams_post_permission")

_orgs__org__teams_post_units_0 = dependencies.DynamicVariable("_orgs__org__teams_post_units_0")

_orgs__org__teams_post_units_map = dependencies.DynamicVariable("_orgs__org__teams_post_units_map")

_repos__owner___repo__branch_protections_post_approvals_whitelist_teams_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_approvals_whitelist_teams_0")

_repos__owner___repo__branch_protections_post_approvals_whitelist_username_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_approvals_whitelist_username_0")

_repos__owner___repo__branch_protections_post_block_on_official_review_requests = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_block_on_official_review_requests")

_repos__owner___repo__branch_protections_post_block_on_outdated_branch = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_block_on_outdated_branch")

_repos__owner___repo__branch_protections_post_block_on_rejected_reviews = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_block_on_rejected_reviews")

_repos__owner___repo__branch_protections_post_dismiss_stale_approvals = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_dismiss_stale_approvals")

_repos__owner___repo__branch_protections_post_enable_approvals_whitelist = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_enable_approvals_whitelist")

_repos__owner___repo__branch_protections_post_enable_merge_whitelist = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_enable_merge_whitelist")

_repos__owner___repo__branch_protections_post_enable_push = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_enable_push")

_repos__owner___repo__branch_protections_post_enable_push_whitelist = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_enable_push_whitelist")

_repos__owner___repo__branch_protections_post_enable_status_check = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_enable_status_check")

_repos__owner___repo__branch_protections_post_merge_whitelist_teams_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_merge_whitelist_teams_0")

_repos__owner___repo__branch_protections_post_merge_whitelist_usernames_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_merge_whitelist_usernames_0")

_repos__owner___repo__branch_protections_post_protected_file_patterns = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_protected_file_patterns")

_repos__owner___repo__branch_protections_post_push_whitelist_deploy_keys = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_push_whitelist_deploy_keys")

_repos__owner___repo__branch_protections_post_push_whitelist_teams_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_push_whitelist_teams_0")

_repos__owner___repo__branch_protections_post_push_whitelist_usernames_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_push_whitelist_usernames_0")

_repos__owner___repo__branch_protections_post_require_signed_commits = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_require_signed_commits")

_repos__owner___repo__branch_protections_post_required_approvals = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_required_approvals")

_repos__owner___repo__branch_protections_post_status_check_contexts_0 = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_status_check_contexts_0")

_repos__owner___repo__branch_protections_post_unprotected_file_patterns = dependencies.DynamicVariable("_repos__owner___repo__branch_protections_post_unprotected_file_patterns")

_repos__owner___repo__contents__filepath__put_content_name = dependencies.DynamicVariable("_repos__owner___repo__contents__filepath__put_content_name")

_repos__owner___repo__hooks_post_id = dependencies.DynamicVariable("_repos__owner___repo__hooks_post_id")

_repos__owner___repo__issues_post_body = dependencies.DynamicVariable("_repos__owner___repo__issues_post_body")

_repos__owner___repo__issues_post_due_date = dependencies.DynamicVariable("_repos__owner___repo__issues_post_due_date")

_repos__owner___repo__issues_post_ref = dependencies.DynamicVariable("_repos__owner___repo__issues_post_ref")

_repos__owner___repo__issues_post_state = dependencies.DynamicVariable("_repos__owner___repo__issues_post_state")

_repos__owner___repo__issues_post_title = dependencies.DynamicVariable("_repos__owner___repo__issues_post_title")

_repos__owner___repo__issues_comments__id__assets_post_id = dependencies.DynamicVariable("_repos__owner___repo__issues_comments__id__assets_post_id")

_repos__owner___repo__issues__index__assets_post_id = dependencies.DynamicVariable("_repos__owner___repo__issues__index__assets_post_id")

_repos__owner___repo__issues__index__comments_post_assets_0_id = dependencies.DynamicVariable("_repos__owner___repo__issues__index__comments_post_assets_0_id")

_repos__owner___repo__issues__index__comments_post_body = dependencies.DynamicVariable("_repos__owner___repo__issues__index__comments_post_body")

_repos__owner___repo__issues__index__labels_put_0_id = dependencies.DynamicVariable("_repos__owner___repo__issues__index__labels_put_0_id")

_repos__owner___repo__issues__index__times_post_id = dependencies.DynamicVariable("_repos__owner___repo__issues__index__times_post_id")

_repos__owner___repo__keys_post_id = dependencies.DynamicVariable("_repos__owner___repo__keys_post_id")

_repos__owner___repo__labels_post_id = dependencies.DynamicVariable("_repos__owner___repo__labels_post_id")

_repos__owner___repo__milestones_post_description = dependencies.DynamicVariable("_repos__owner___repo__milestones_post_description")

_repos__owner___repo__milestones_post_due_on = dependencies.DynamicVariable("_repos__owner___repo__milestones_post_due_on")

_repos__owner___repo__milestones_post_id = dependencies.DynamicVariable("_repos__owner___repo__milestones_post_id")

_repos__owner___repo__milestones_post_state = dependencies.DynamicVariable("_repos__owner___repo__milestones_post_state")

_repos__owner___repo__milestones_post_title = dependencies.DynamicVariable("_repos__owner___repo__milestones_post_title")

_repos__owner___repo__pulls_post_allow_maintainer_edit = dependencies.DynamicVariable("_repos__owner___repo__pulls_post_allow_maintainer_edit")

_repos__owner___repo__pulls_post_body = dependencies.DynamicVariable("_repos__owner___repo__pulls_post_body")

_repos__owner___repo__pulls_post_due_date = dependencies.DynamicVariable("_repos__owner___repo__pulls_post_due_date")

_repos__owner___repo__pulls_post_state = dependencies.DynamicVariable("_repos__owner___repo__pulls_post_state")

_repos__owner___repo__pulls_post_title = dependencies.DynamicVariable("_repos__owner___repo__pulls_post_title")

_repos__owner___repo__pulls__index__reviews_post_id = dependencies.DynamicVariable("_repos__owner___repo__pulls__index__reviews_post_id")

_repos__owner___repo__releases_post_assets_0_id = dependencies.DynamicVariable("_repos__owner___repo__releases_post_assets_0_id")

_repos__owner___repo__releases_post_body = dependencies.DynamicVariable("_repos__owner___repo__releases_post_body")

_repos__owner___repo__releases_post_draft = dependencies.DynamicVariable("_repos__owner___repo__releases_post_draft")

_repos__owner___repo__releases_post_name = dependencies.DynamicVariable("_repos__owner___repo__releases_post_name")

_repos__owner___repo__releases_post_prerelease = dependencies.DynamicVariable("_repos__owner___repo__releases_post_prerelease")

_repos__owner___repo__releases_post_target_commitish = dependencies.DynamicVariable("_repos__owner___repo__releases_post_target_commitish")

_repos__owner___repo__releases__id__assets_post_id = dependencies.DynamicVariable("_repos__owner___repo__releases__id__assets_post_id")

_user_applications_oauth2_post_id = dependencies.DynamicVariable("_user_applications_oauth2_post_id")

_user_gpg_keys_post_id = dependencies.DynamicVariable("_user_gpg_keys_post_id")

_user_keys_post_id = dependencies.DynamicVariable("_user_keys_post_id")

def parse_adminhookspost(data, **kwargs):
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
        dependencies.set_variable("_admin_hooks_post_id", temp_7262)


def parse_adminuserspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None
    temp_7680 = None
    temp_5581 = None
    temp_2060 = None
    temp_5588 = None
    temp_9060 = None
    temp_4421 = None
    temp_9775 = None
    temp_2737 = None
    temp_2919 = None
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
            temp_8173 = str(data["active"])
            temp_8173 = temp_8173.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7680 = str(data["description"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5581 = str(data["email"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2060 = str(data["full_name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5588 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9060 = str(data["location"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4421 = str(data["login"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9775 = str(data["login_name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2737 = str(data["restricted"])
            temp_2737 = temp_2737.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2919 = str(data["visibility"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4673 = str(data["website"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8173 or temp_7680 or temp_5581 or temp_2060 or temp_5588 or temp_9060 or temp_4421 or temp_9775 or temp_2737 or temp_2919 or temp_4673):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_admin_users_post_active", temp_8173)
    if temp_7680:
        dependencies.set_variable("_admin_users_post_description", temp_7680)
    if temp_5581:
        dependencies.set_variable("_admin_users_post_email", temp_5581)
    if temp_2060:
        dependencies.set_variable("_admin_users_post_full_name", temp_2060)
    if temp_5588:
        dependencies.set_variable("_admin_users_post_id", temp_5588)
    if temp_9060:
        dependencies.set_variable("_admin_users_post_location", temp_9060)
    if temp_4421:
        dependencies.set_variable("_admin_users_post_login", temp_4421)
    if temp_9775:
        dependencies.set_variable("_admin_users_post_login_name", temp_9775)
    if temp_2737:
        dependencies.set_variable("_admin_users_post_restricted", temp_2737)
    if temp_2919:
        dependencies.set_variable("_admin_users_post_visibility", temp_2919)
    if temp_4673:
        dependencies.set_variable("_admin_users_post_website", temp_4673)


def parse_adminusersusernamekeyspost(data, **kwargs):
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
        dependencies.set_variable("_admin_users__username__keys_post_id", temp_6326)


def parse_orgsorghookspost(data, **kwargs):
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
        dependencies.set_variable("_orgs__org__hooks_post_id", temp_4695)


def parse_orgsorglabelspost(data, **kwargs):
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
        dependencies.set_variable("_orgs__org__labels_post_id", temp_9821)


def parse_orgsorgteamspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_303 = None
    temp_8623 = None
    temp_9953 = None
    temp_6771 = None
    temp_3145 = None
    temp_8169 = None
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
            temp_303 = str(data["can_create_org_repo"])
            temp_303 = temp_303.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8623 = str(data["description"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9953 = str(data["includes_all_repositories"])
            temp_9953 = temp_9953.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6771 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3145 = str(data["permission"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8169 = str(data["units"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8480 = str(data["units_map"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_303 or temp_8623 or temp_9953 or temp_6771 or temp_3145 or temp_8169 or temp_8480):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_303:
        dependencies.set_variable("_orgs__org__teams_post_can_create_org_repo", temp_303)
    if temp_8623:
        dependencies.set_variable("_orgs__org__teams_post_description", temp_8623)
    if temp_9953:
        dependencies.set_variable("_orgs__org__teams_post_includes_all_repositories", temp_9953)
    if temp_6771:
        dependencies.set_variable("_orgs__org__teams_post_name", temp_6771)
    if temp_3145:
        dependencies.set_variable("_orgs__org__teams_post_permission", temp_3145)
    if temp_8169:
        dependencies.set_variable("_orgs__org__teams_post_units_0", temp_8169)
    if temp_8480:
        dependencies.set_variable("_orgs__org__teams_post_units_map", temp_8480)


def parse_reposownerrepobranch_protectionspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9919 = None
    temp_326 = None
    temp_6999 = None
    temp_5262 = None
    temp_9340 = None
    temp_6876 = None
    temp_5468 = None
    temp_811 = None
    temp_1871 = None
    temp_4533 = None
    temp_2971 = None
    temp_9885 = None
    temp_6426 = None
    temp_7629 = None
    temp_303 = None
    temp_3810 = None
    temp_3431 = None
    temp_9574 = None
    temp_5051 = None
    temp_7159 = None
    temp_1189 = None

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
            temp_9919 = str(data["approvals_whitelist_teams"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_326 = str(data["approvals_whitelist_username"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6999 = str(data["block_on_official_review_requests"])
            temp_6999 = temp_6999.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5262 = str(data["block_on_outdated_branch"])
            temp_5262 = temp_5262.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9340 = str(data["block_on_rejected_reviews"])
            temp_9340 = temp_9340.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6876 = str(data["dismiss_stale_approvals"])
            temp_6876 = temp_6876.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5468 = str(data["enable_approvals_whitelist"])
            temp_5468 = temp_5468.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_811 = str(data["enable_merge_whitelist"])
            temp_811 = temp_811.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1871 = str(data["enable_push"])
            temp_1871 = temp_1871.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4533 = str(data["enable_push_whitelist"])
            temp_4533 = temp_4533.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2971 = str(data["enable_status_check"])
            temp_2971 = temp_2971.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9885 = str(data["merge_whitelist_teams"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6426 = str(data["merge_whitelist_usernames"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7629 = str(data["protected_file_patterns"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_303 = str(data["push_whitelist_deploy_keys"])
            temp_303 = temp_303.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3810 = str(data["push_whitelist_teams"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3431 = str(data["push_whitelist_usernames"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9574 = str(data["require_signed_commits"])
            temp_9574 = temp_9574.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_5051 = str(data["required_approvals"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7159 = str(data["status_check_contexts"][0])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1189 = str(data["unprotected_file_patterns"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9919 or temp_326 or temp_6999 or temp_5262 or temp_9340 or temp_6876 or temp_5468 or temp_811 or temp_1871 or temp_4533 or temp_2971 or temp_9885 or temp_6426 or temp_7629 or temp_303 or temp_3810 or temp_3431 or temp_9574 or temp_5051 or temp_7159 or temp_1189):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9919:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_approvals_whitelist_teams_0", temp_9919)
    if temp_326:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_approvals_whitelist_username_0", temp_326)
    if temp_6999:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_block_on_official_review_requests", temp_6999)
    if temp_5262:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_block_on_outdated_branch", temp_5262)
    if temp_9340:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_block_on_rejected_reviews", temp_9340)
    if temp_6876:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_dismiss_stale_approvals", temp_6876)
    if temp_5468:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_enable_approvals_whitelist", temp_5468)
    if temp_811:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_enable_merge_whitelist", temp_811)
    if temp_1871:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_enable_push", temp_1871)
    if temp_4533:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_enable_push_whitelist", temp_4533)
    if temp_2971:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_enable_status_check", temp_2971)
    if temp_9885:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_merge_whitelist_teams_0", temp_9885)
    if temp_6426:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_merge_whitelist_usernames_0", temp_6426)
    if temp_7629:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_protected_file_patterns", temp_7629)
    if temp_303:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_push_whitelist_deploy_keys", temp_303)
    if temp_3810:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_push_whitelist_teams_0", temp_3810)
    if temp_3431:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_push_whitelist_usernames_0", temp_3431)
    if temp_9574:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_require_signed_commits", temp_9574)
    if temp_5051:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_required_approvals", temp_5051)
    if temp_7159:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_status_check_contexts_0", temp_7159)
    if temp_1189:
        dependencies.set_variable("_repos__owner___repo__branch_protections_post_unprotected_file_patterns", temp_1189)


def parse_reposownerrepocontentsfilepathput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2734 = None

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
            temp_2734 = str(data["content"]["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2734):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2734:
        dependencies.set_variable("_repos__owner___repo__contents__filepath__put_content_name", temp_2734)


def parse_reposownerrepohookspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_9070 = None

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
            temp_9070 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_9070):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_9070:
        dependencies.set_variable("_repos__owner___repo__hooks_post_id", temp_9070)


def parse_reposownerrepoissuespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7947 = None
    temp_3371 = None
    temp_4572 = None
    temp_1468 = None
    temp_2213 = None

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
            temp_7947 = str(data["body"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_3371 = str(data["due_date"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4572 = str(data["ref"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1468 = str(data["state"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2213 = str(data["title"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7947 or temp_3371 or temp_4572 or temp_1468 or temp_2213):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7947:
        dependencies.set_variable("_repos__owner___repo__issues_post_body", temp_7947)
    if temp_3371:
        dependencies.set_variable("_repos__owner___repo__issues_post_due_date", temp_3371)
    if temp_4572:
        dependencies.set_variable("_repos__owner___repo__issues_post_ref", temp_4572)
    if temp_1468:
        dependencies.set_variable("_repos__owner___repo__issues_post_state", temp_1468)
    if temp_2213:
        dependencies.set_variable("_repos__owner___repo__issues_post_title", temp_2213)


def parse_reposownerrepoissuescommentsidassetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_4100 = None

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
            temp_4100 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_4100):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_4100:
        dependencies.set_variable("_repos__owner___repo__issues_comments__id__assets_post_id", temp_4100)


def parse_reposownerrepoissuesindexassetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7187 = None

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
            temp_7187 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7187):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7187:
        dependencies.set_variable("_repos__owner___repo__issues__index__assets_post_id", temp_7187)


def parse_reposownerrepoissuesindexcommentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_6198 = None
    temp_4879 = None

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
            temp_6198 = str(data["assets"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4879 = str(data["body"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_6198 or temp_4879):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_6198:
        dependencies.set_variable("_repos__owner___repo__issues__index__comments_post_assets_0_id", temp_6198)
    if temp_4879:
        dependencies.set_variable("_repos__owner___repo__issues__index__comments_post_body", temp_4879)


def parse_reposownerrepoissuesindexlabelsput(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_1949 = None

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
            temp_1949 = str(data[0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_1949):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_1949:
        dependencies.set_variable("_repos__owner___repo__issues__index__labels_put_0_id", temp_1949)


def parse_reposownerrepoissuesindextimespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8781 = None

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
            temp_8781 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8781):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8781:
        dependencies.set_variable("_repos__owner___repo__issues__index__times_post_id", temp_8781)


def parse_reposownerrepokeyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8254 = None

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
            temp_8254 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8254):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8254:
        dependencies.set_variable("_repos__owner___repo__keys_post_id", temp_8254)


def parse_reposownerrepolabelspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7353 = None

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
            temp_7353 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7353):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7353:
        dependencies.set_variable("_repos__owner___repo__labels_post_id", temp_7353)


def parse_reposownerrepomilestonespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8582 = None
    temp_6797 = None
    temp_6248 = None
    temp_2184 = None
    temp_8953 = None

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
            temp_8582 = str(data["description"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6797 = str(data["due_on"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6248 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_2184 = str(data["state"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8953 = str(data["title"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8582 or temp_6797 or temp_6248 or temp_2184 or temp_8953):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8582:
        dependencies.set_variable("_repos__owner___repo__milestones_post_description", temp_8582)
    if temp_6797:
        dependencies.set_variable("_repos__owner___repo__milestones_post_due_on", temp_6797)
    if temp_6248:
        dependencies.set_variable("_repos__owner___repo__milestones_post_id", temp_6248)
    if temp_2184:
        dependencies.set_variable("_repos__owner___repo__milestones_post_state", temp_2184)
    if temp_8953:
        dependencies.set_variable("_repos__owner___repo__milestones_post_title", temp_8953)


def parse_reposownerrepopullspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8964 = None
    temp_865 = None
    temp_8385 = None
    temp_1701 = None
    temp_6441 = None

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
            temp_8964 = str(data["allow_maintainer_edit"])
            temp_8964 = temp_8964.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_865 = str(data["body"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8385 = str(data["due_date"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_1701 = str(data["state"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6441 = str(data["title"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8964 or temp_865 or temp_8385 or temp_1701 or temp_6441):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8964:
        dependencies.set_variable("_repos__owner___repo__pulls_post_allow_maintainer_edit", temp_8964)
    if temp_865:
        dependencies.set_variable("_repos__owner___repo__pulls_post_body", temp_865)
    if temp_8385:
        dependencies.set_variable("_repos__owner___repo__pulls_post_due_date", temp_8385)
    if temp_1701:
        dependencies.set_variable("_repos__owner___repo__pulls_post_state", temp_1701)
    if temp_6441:
        dependencies.set_variable("_repos__owner___repo__pulls_post_title", temp_6441)


def parse_reposownerrepopullsindexreviewspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8268 = None

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
            temp_8268 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_8268):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8268:
        dependencies.set_variable("_repos__owner___repo__pulls__index__reviews_post_id", temp_8268)


def parse_reposownerreporeleasespost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_2191 = None
    temp_9999 = None
    temp_4813 = None
    temp_6522 = None
    temp_7197 = None
    temp_8094 = None

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
            temp_2191 = str(data["assets"][0]["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_9999 = str(data["body"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_4813 = str(data["draft"])
            temp_4813 = temp_4813.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_6522 = str(data["name"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_7197 = str(data["prerelease"])
            temp_7197 = temp_7197.lower()
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass


        try:
            temp_8094 = str(data["target_commitish"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_2191 or temp_9999 or temp_4813 or temp_6522 or temp_7197 or temp_8094):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_2191:
        dependencies.set_variable("_repos__owner___repo__releases_post_assets_0_id", temp_2191)
    if temp_9999:
        dependencies.set_variable("_repos__owner___repo__releases_post_body", temp_9999)
    if temp_4813:
        dependencies.set_variable("_repos__owner___repo__releases_post_draft", temp_4813)
    if temp_6522:
        dependencies.set_variable("_repos__owner___repo__releases_post_name", temp_6522)
    if temp_7197:
        dependencies.set_variable("_repos__owner___repo__releases_post_prerelease", temp_7197)
    if temp_8094:
        dependencies.set_variable("_repos__owner___repo__releases_post_target_commitish", temp_8094)


def parse_reposownerreporeleasesidassetspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_1009 = None

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
            temp_1009 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_1009):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_1009:
        dependencies.set_variable("_repos__owner___repo__releases__id__assets_post_id", temp_1009)


def parse_userapplicationsoauth2post(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7290 = None

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
            temp_7290 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7290):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7290:
        dependencies.set_variable("_user_applications_oauth2_post_id", temp_7290)


def parse_usergpg_keyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7184 = None

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
            temp_7184 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7184):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7184:
        dependencies.set_variable("_user_gpg_keys_post_id", temp_7184)


def parse_userkeyspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_1255 = None

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
            temp_1255 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_1255):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_1255:
        dependencies.set_variable("_user_keys_post_id", temp_1255)

req_collection = requests.RequestCollection([])
# Endpoint: /activitypub/user/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("activitypub"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/activitypub/user/{username}"
)
req_collection.add_request(request)

# Endpoint: /activitypub/user/{username}/inbox, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("activitypub"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("inbox"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/activitypub/user/{username}/inbox"
)
req_collection.add_request(request)

# Endpoint: /admin/cron, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cron"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/cron"
)
req_collection.add_request(request)

# Endpoint: /admin/cron/{task}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("cron"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/cron/{task}"
)
req_collection.add_request(request)

# Endpoint: /admin/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/hooks"
)
req_collection.add_request(request)

# Endpoint: /admin/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_adminhookspost,
            'dependencies':
            [
                _admin_hooks_post_id.writer()
            ]
        }

    },

],
requestId="/admin/hooks"
)
req_collection.add_request(request)

# Endpoint: /admin/hooks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_admin_hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /admin/hooks/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_admin_hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /admin/orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/orgs"
)
req_collection.add_request(request)

# Endpoint: /admin/unadopted, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unadopted"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pattern="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/unadopted"
)
req_collection.add_request(request)

# Endpoint: /admin/unadopted/{owner}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unadopted"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/unadopted/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /admin/unadopted/{owner}/{repo}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("unadopted"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/unadopted/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /admin/users, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/users"
)
req_collection.add_request(request)

# Endpoint: /admin/users, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "created_at":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "login_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "must_change_password":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "restricted":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "send_notify":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "source_id":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_adminuserspost,
            'dependencies':
            [
                _admin_users_post_active.writer(),
                _admin_users_post_description.writer(),
                _admin_users_post_email.writer(),
                _admin_users_post_full_name.writer(),
                _admin_users_post_id.writer(),
                _admin_users_post_location.writer(),
                _admin_users_post_login.writer(),
                _admin_users_post_login_name.writer(),
                _admin_users_post_restricted.writer(),
                _admin_users_post_visibility.writer(),
                _admin_users_post_website.writer()
            ]
        }

    },

],
requestId="/admin/users"
)
req_collection.add_request(request)

# Endpoint: /admin/users/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/users/{username}"
)
req_collection.add_request(request)

# Endpoint: /admin/users/{username}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "active":"""),
    primitives.restler_static_string(_admin_users_post_active.reader(), quoted=False),
    primitives.restler_static_string(""",
    "admin":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_create_organization":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_git_hook":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_import_local":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_static_string(_admin_users_post_description.reader(), quoted=True),
    primitives.restler_static_string(""",
    "email":"""),
    primitives.restler_static_string(_admin_users_post_email.reader(), quoted=True),
    primitives.restler_static_string(""",
    "full_name":"""),
    primitives.restler_static_string(_admin_users_post_full_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_static_string(_admin_users_post_location.reader(), quoted=True),
    primitives.restler_static_string(""",
    "login_name":"""),
    primitives.restler_static_string(_admin_users_post_login_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "max_repo_creation":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "must_change_password":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "prohibit_login":"""),
    primitives.restler_static_string(_admin_users_post_login.reader(), quoted=False),
    primitives.restler_static_string(""",
    "restricted":"""),
    primitives.restler_static_string(_admin_users_post_restricted.reader(), quoted=False),
    primitives.restler_static_string(""",
    "source_id":"""),
    primitives.restler_static_string(_admin_users_post_id.reader(), quoted=False),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_static_string(_admin_users_post_visibility.reader(), quoted=True),
    primitives.restler_static_string(""",
    "website":"""),
    primitives.restler_static_string(_admin_users_post_website.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/users/{username}"
)
req_collection.add_request(request)

# Endpoint: /admin/users/{username}/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_adminusersusernamekeyspost,
            'dependencies':
            [
                _admin_users__username__keys_post_id.writer()
            ]
        }

    },

],
requestId="/admin/users/{username}/keys"
)
req_collection.add_request(request)

# Endpoint: /admin/users/{username}/keys/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_admin_users__username__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/users/{username}/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /admin/users/{username}/orgs, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/users/{username}/orgs"
)
req_collection.add_request(request)

# Endpoint: /admin/users/{username}/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("admin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auto_init":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "default_branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "gitignores":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "issue_labels":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "license":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "readme":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "template":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "trust_model":"""),
    primitives.restler_fuzzable_group("trust_model", ['default','collaborator','committer','collaboratorcommitter']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/admin/users/{username}/repos"
)
req_collection.add_request(request)

# Endpoint: /amdin/hooks/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("amdin"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/amdin/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /markdown, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("markdown"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Context":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Mode":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Text":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "Wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/markdown"
)
req_collection.add_request(request)

# Endpoint: /markdown/raw, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("markdown"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/markdown/raw"
)
req_collection.add_request(request)

# Endpoint: /nodeinfo, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("nodeinfo"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/nodeinfo"
)
req_collection.add_request(request)

# Endpoint: /notifications, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status-types="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("subject-type="),
    primitives.restler_fuzzable_group("", ['issue','pull','commit','repository']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/notifications"
)
req_collection.add_request(request)

# Endpoint: /notifications, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("last_read_at="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status-types="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to-status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/notifications"
)
req_collection.add_request(request)

# Endpoint: /notifications/new, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("new"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/notifications/new"
)
req_collection.add_request(request)

# Endpoint: /notifications/threads/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/notifications/threads/{id}"
)
req_collection.add_request(request)

# Endpoint: /notifications/threads/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("threads"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("to-status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/notifications/threads/{id}"
)
req_collection.add_request(request)

# Endpoint: /org/{org}/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("org"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/org/{org}/repos"
)
req_collection.add_request(request)

# Endpoint: /orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs"
)
req_collection.add_request(request)

# Endpoint: /orgs, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "repo_admin_change_team_access":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "visibility":"""),
    primitives.restler_fuzzable_group("visibility", ['public','limited','private']  ,quoted=True),
    primitives.restler_static_string(""",
    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/hooks"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_orgsorghookspost,
            'dependencies':
            [
                _orgs__org__hooks_post_id.writer()
            ]
        }

    },

],
requestId="/orgs/{org}/hooks"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/hooks/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_orgs__org__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/hooks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_orgs__org__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/hooks/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_orgs__org__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/labels"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_orgsorglabelspost,
            'dependencies':
            [
                _orgs__org__labels_post_id.writer()
            ]
        }

    },

],
requestId="/orgs/{org}/labels"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/labels/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_orgs__org__labels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/labels/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_orgs__org__labels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/labels/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_orgs__org__labels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/members"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/members/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/members/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/public_members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public_members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/public_members"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/public_members/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public_members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/public_members/{username}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/public_members/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public_members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/public_members/{username}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/public_members/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("public_members"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/public_members/{username}"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/repos"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/repos"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/teams, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/teams"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/teams, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "can_create_org_repo":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "includes_all_repositories":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "permission":"""),
    primitives.restler_fuzzable_group("permission", ['read','write','admin']  ,quoted=True),
    primitives.restler_static_string(""",
    "units":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["repo.code"]),
    primitives.restler_static_string(""",
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["repo.issues"]),
    primitives.restler_static_string(""",
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["repo.ext_issues"]),
    primitives.restler_static_string(""",
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["repo.wiki"]),
    primitives.restler_static_string(""",
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["repo.pulls"]),
    primitives.restler_static_string("""
    ],
    "units_map":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }", examples=["{\"repo.code\":\"read\",\"repo.ext_issues\":\"none\",\"repo.ext_wiki\":\"none\",\"repo.issues\":\"write\",\"repo.projects\":\"none\",\"repo.pulls\":\"owner\",\"repo.releases\":\"none\",\"repo.wiki\":\"admin\"}"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_orgsorgteamspost,
            'dependencies':
            [
                _orgs__org__teams_post_can_create_org_repo.writer(),
                _orgs__org__teams_post_description.writer(),
                _orgs__org__teams_post_includes_all_repositories.writer(),
                _orgs__org__teams_post_name.writer(),
                _orgs__org__teams_post_permission.writer(),
                _orgs__org__teams_post_units_0.writer(),
                _orgs__org__teams_post_units_map.writer()
            ]
        }

    },

],
requestId="/orgs/{org}/teams"
)
req_collection.add_request(request)

# Endpoint: /orgs/{org}/teams/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("include_desc="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orgs/{org}/teams/search"
)
req_collection.add_request(request)

# Endpoint: /packages/{owner}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("packages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['cargo','chef','composer','conan','conda','container','generic','helm','maven','npm','nuget','pub','pypi','rubygems','vagrant']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/packages/{owner}"
)
req_collection.add_request(request)

# Endpoint: /packages/{owner}/{type}/{name}/{version}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("packages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/packages/{owner}/{type}/{name}/{version}"
)
req_collection.add_request(request)

# Endpoint: /packages/{owner}/{type}/{name}/{version}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("packages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/packages/{owner}/{type}/{name}/{version}"
)
req_collection.add_request(request)

# Endpoint: /packages/{owner}/{type}/{name}/{version}/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("packages"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/packages/{owner}/{type}/{name}/{version}/files"
)
req_collection.add_request(request)

# Endpoint: /repos/issues/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestones="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("priority_repo_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assigned="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("mentioned="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("review_requested="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("reviewed="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("owner="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/issues/search"
)
req_collection.add_request(request)

# Endpoint: /repos/migrate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("migrate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "auth_password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "auth_token":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "auth_username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "clone_addr":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "labels":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "lfs":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "lfs_endpoint":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "milestones":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "mirror":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "mirror_interval":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "pull_requests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "releases":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "repo_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "repo_owner":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "service":"""),
    primitives.restler_fuzzable_group("service", ['git','github','gitea','gitlab']  ,quoted=True),
    primitives.restler_static_string(""",
    "uid":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/migrate"
)
req_collection.add_request(request)

# Endpoint: /repos/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("topic="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("includeDesc="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("uid="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("priority_owner_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("team_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("starredBy="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("private="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("is_private="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("template="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("archived="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("mode="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("exclusive="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("order="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/search"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "allow_manual_merge":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_merge_commits":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_rebase":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_rebase_explicit":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_rebase_update":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "allow_squash_merge":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "archived":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "autodetect_manual_merge":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "default_allow_maintainer_edit":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "default_branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "default_delete_branch_after_merge":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "default_merge_style":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "enable_prune":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "external_tracker":
        {
            "external_tracker_format":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "external_tracker_regexp_pattern":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "external_tracker_style":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "external_tracker_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "external_wiki":
        {
            "external_wiki_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "has_issues":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "has_projects":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "has_pull_requests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "has_wiki":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "ignore_whitespace_conflicts":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "internal_tracker":
        {
            "allow_only_contributors_to_track_time":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "enable_issue_dependencies":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "enable_time_tracker":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "mirror_interval":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "template":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/archive/{archive}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("archive"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/archive/{archive}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/assignees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assignees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/assignees"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branch_protections, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch_protections"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branch_protections"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branch_protections, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch_protections"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "approvals_whitelist_teams":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "approvals_whitelist_username":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "block_on_official_review_requests":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "block_on_outdated_branch":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "block_on_rejected_reviews":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "branch_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "dismiss_stale_approvals":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "enable_approvals_whitelist":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "enable_merge_whitelist":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "enable_push":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "enable_push_whitelist":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "enable_status_check":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "merge_whitelist_teams":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "merge_whitelist_usernames":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "protected_file_patterns":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "push_whitelist_deploy_keys":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "push_whitelist_teams":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "push_whitelist_usernames":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "require_signed_commits":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "required_approvals":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "rule_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "status_check_contexts":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "unprotected_file_patterns":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepobranch_protectionspost,
            'dependencies':
            [
                _repos__owner___repo__branch_protections_post_approvals_whitelist_teams_0.writer(),
                _repos__owner___repo__branch_protections_post_approvals_whitelist_username_0.writer(),
                _repos__owner___repo__branch_protections_post_block_on_official_review_requests.writer(),
                _repos__owner___repo__branch_protections_post_block_on_outdated_branch.writer(),
                _repos__owner___repo__branch_protections_post_block_on_rejected_reviews.writer(),
                _repos__owner___repo__branch_protections_post_dismiss_stale_approvals.writer(),
                _repos__owner___repo__branch_protections_post_enable_approvals_whitelist.writer(),
                _repos__owner___repo__branch_protections_post_enable_merge_whitelist.writer(),
                _repos__owner___repo__branch_protections_post_enable_push.writer(),
                _repos__owner___repo__branch_protections_post_enable_push_whitelist.writer(),
                _repos__owner___repo__branch_protections_post_enable_status_check.writer(),
                _repos__owner___repo__branch_protections_post_merge_whitelist_teams_0.writer(),
                _repos__owner___repo__branch_protections_post_merge_whitelist_usernames_0.writer(),
                _repos__owner___repo__branch_protections_post_protected_file_patterns.writer(),
                _repos__owner___repo__branch_protections_post_push_whitelist_deploy_keys.writer(),
                _repos__owner___repo__branch_protections_post_push_whitelist_teams_0.writer(),
                _repos__owner___repo__branch_protections_post_push_whitelist_usernames_0.writer(),
                _repos__owner___repo__branch_protections_post_require_signed_commits.writer(),
                _repos__owner___repo__branch_protections_post_required_approvals.writer(),
                _repos__owner___repo__branch_protections_post_status_check_contexts_0.writer(),
                _repos__owner___repo__branch_protections_post_unprotected_file_patterns.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/branch_protections"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branch_protections/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch_protections"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branch_protections/{name}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branch_protections/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch_protections"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branch_protections/{name}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branch_protections/{name}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branch_protections"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "approvals_whitelist_teams":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_approvals_whitelist_teams_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "approvals_whitelist_username":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_approvals_whitelist_username_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "block_on_official_review_requests":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_block_on_official_review_requests.reader(), quoted=False),
    primitives.restler_static_string(""",
    "block_on_outdated_branch":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_block_on_outdated_branch.reader(), quoted=False),
    primitives.restler_static_string(""",
    "block_on_rejected_reviews":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_block_on_rejected_reviews.reader(), quoted=False),
    primitives.restler_static_string(""",
    "dismiss_stale_approvals":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_dismiss_stale_approvals.reader(), quoted=False),
    primitives.restler_static_string(""",
    "enable_approvals_whitelist":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_enable_approvals_whitelist.reader(), quoted=False),
    primitives.restler_static_string(""",
    "enable_merge_whitelist":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_enable_merge_whitelist.reader(), quoted=False),
    primitives.restler_static_string(""",
    "enable_push":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_enable_push.reader(), quoted=False),
    primitives.restler_static_string(""",
    "enable_push_whitelist":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_enable_push_whitelist.reader(), quoted=False),
    primitives.restler_static_string(""",
    "enable_status_check":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_enable_status_check.reader(), quoted=False),
    primitives.restler_static_string(""",
    "merge_whitelist_teams":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_merge_whitelist_teams_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "merge_whitelist_usernames":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_merge_whitelist_usernames_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "protected_file_patterns":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_protected_file_patterns.reader(), quoted=True),
    primitives.restler_static_string(""",
    "push_whitelist_deploy_keys":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_push_whitelist_deploy_keys.reader(), quoted=False),
    primitives.restler_static_string(""",
    "push_whitelist_teams":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_push_whitelist_teams_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "push_whitelist_usernames":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_push_whitelist_usernames_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "require_signed_commits":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_require_signed_commits.reader(), quoted=False),
    primitives.restler_static_string(""",
    "required_approvals":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_required_approvals.reader(), quoted=False),
    primitives.restler_static_string(""",
    "status_check_contexts":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_status_check_contexts_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "unprotected_file_patterns":"""),
    primitives.restler_static_string(_repos__owner___repo__branch_protections_post_unprotected_file_patterns.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branch_protections/{name}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branches, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branches"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branches, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "new_branch_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "old_branch_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branches"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branches/{branch}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branches/{branch}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/branches/{branch}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("branches"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/branches/{branch}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/collaborators, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/collaborators"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/collaborators/{collaborator}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/collaborators/{collaborator}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/collaborators/{collaborator}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/collaborators/{collaborator}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/collaborators/{collaborator}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("collaborator", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "permission":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/collaborators/{collaborator}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/collaborators/{collaborator}/permission, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("collaborators"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permission"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/collaborators/{collaborator}/permission"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sha="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("path="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("stat="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/commits"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/commits/{ref}/status, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("status"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/commits/{ref}/status"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/commits/{ref}/statuses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['oldest','recentupdate','leastupdate','leastindex','highestindex']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['pending','success','error','failure','warning']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/commits/{ref}/statuses"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/contents, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/contents"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/contents/{filepath}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__contents__filepath__put_content_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "author":
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "committer":
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "dates":
        {
            "author":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "committer":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "new_branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "sha":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "signoff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/contents/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/contents/{filepath}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__contents__filepath__put_content_name.reader(), quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/contents/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/contents/{filepath}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__contents__filepath__put_content_name.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "author":
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "committer":
        {
            "email":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
            "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "content":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "dates":
        {
            "author":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
            "committer":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("""
        }
    ,
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "new_branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "signoff":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/contents/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/contents/{filepath}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("contents"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("filepath", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepocontentsfilepathput,
            'dependencies':
            [
                _repos__owner___repo__contents__filepath__put_content_name.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/contents/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/diffpatch, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("diffpatch"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/diffpatch"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/editorconfig/{filepath}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("editorconfig"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/editorconfig/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/forks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/forks"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/forks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("forks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "organization":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/forks"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/blobs/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("blobs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/blobs/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/commits/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/commits/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/commits/{sha}.{diffType}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/commits/{sha}.{diffType}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/notes/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notes"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/notes/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/refs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/refs"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/refs/{ref}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("refs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/refs/{ref}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/tags/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/tags/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/git/trees/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("trees"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("recursive="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/git/trees/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "active":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "authorization_header":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "branch_filter":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "config":
        """),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("""
    ,
    "events":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "type":"""),
    primitives.restler_fuzzable_group("type", ['dingtalk','discord','gitea','gogs','msteams','slack','telegram','feishu','wechatwork','packagist']  ,quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepohookspost,
            'dependencies':
            [
                _repos__owner___repo__hooks_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/hooks"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/git, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/git"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/git/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/git/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/git/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/git/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/git/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("git"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "content":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/git/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "active":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "authorization_header":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "branch_filter":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "config":"""),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(""",
    "events":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/hooks/{id}/tests, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("hooks"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__hooks_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/hooks/{id}/tests"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issue_templates, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issue_templates"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issue_templates"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['closed','open','all']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("type="),
    primitives.restler_fuzzable_group("type", ['issues','pulls']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestones="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("created_by="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("assigned_by="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("mentioned_by="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "assignee":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "assignees":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "closed":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "due_date":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "labels":
    [
        """),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
    ],
    "milestone":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "ref":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepoissuespost,
            'dependencies':
            [
                _repos__owner___repo__issues_post_body.writer(),
                _repos__owner___repo__issues_post_due_date.writer(),
                _repos__owner___repo__issues_post_ref.writer(),
                _repos__owner___repo__issues_post_state.writer(),
                _repos__owner___repo__issues_post_title.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/issues"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/assets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/assets"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/assets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepoissuescommentsidassetspost,
            'dependencies':
            [
                _repos__owner___repo__issues_comments__id__assets_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/assets"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues_comments__id__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues_comments__id__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues_comments__id__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/reactions, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reactions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/reactions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/reactions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reactions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/reactions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/comments/{id}/reactions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reactions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/comments/{id}/reactions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "assignee":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "assignees":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "body":"""),
    primitives.restler_static_string(_repos__owner___repo__issues_post_body.reader(), quoted=True),
    primitives.restler_static_string(""",
    "due_date":"""),
    primitives.restler_static_string(_repos__owner___repo__issues_post_due_date.reader(), quoted=True),
    primitives.restler_static_string(""",
    "milestone":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "ref":"""),
    primitives.restler_static_string(_repos__owner___repo__issues_post_ref.reader(), quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_static_string(_repos__owner___repo__issues_post_state.reader(), quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_static_string(_repos__owner___repo__issues_post_title.reader(), quoted=True),
    primitives.restler_static_string(""",
    "unset_due_date":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/assets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/assets"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/assets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepoissuesindexassetspost,
            'dependencies':
            [
                _repos__owner___repo__issues__index__assets_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/issues/{index}/assets"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/comments"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/comments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepoissuesindexcommentspost,
            'dependencies':
            [
                _repos__owner___repo__issues__index__comments_post_assets_0_id.writer(),
                _repos__owner___repo__issues__index__comments_post_body.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/issues/{index}/comments"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/comments/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__comments_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/comments/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__comments_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/comments/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/deadline, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deadline"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "due_date":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/deadline"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/labels, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/labels"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/labels"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/labels"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/labels, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepoissuesindexlabelsput,
            'dependencies':
            [
                _repos__owner___repo__issues__index__labels_put_0_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/issues/{index}/labels"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/labels/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__labels_put_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/reactions, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reactions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/reactions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/reactions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reactions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/reactions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/reactions, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reactions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/reactions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/stopwatch/delete, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stopwatch"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delete"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/stopwatch/delete"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/stopwatch/start, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stopwatch"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("start"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/stopwatch/start"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/stopwatch/stop, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stopwatch"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stop"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/stopwatch/stop"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/subscriptions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/subscriptions"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/subscriptions/check, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("check"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/subscriptions/check"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/subscriptions/{user}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/subscriptions/{user}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("user", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/timeline, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("timeline"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/timeline"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/times, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/times"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/times, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("user="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/times"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/times, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "created":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "time":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "user_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepoissuesindextimespost,
            'dependencies':
            [
                _repos__owner___repo__issues__index__times_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/issues/{index}/times"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/issues/{index}/times/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("issues"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__issues__index__times_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/issues/{index}/times/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("key_id="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("fingerprint="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/keys"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepokeyspost,
            'dependencies':
            [
                _repos__owner___repo__keys_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/keys"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/keys/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/keys/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/labels, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/labels"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/labels, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepolabelspost,
            'dependencies':
            [
                _repos__owner___repo__labels_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/labels"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/labels/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__labels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/labels/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__labels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/labels/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("labels"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__labels_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/labels/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/languages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("languages"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/languages"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/media/{filepath}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("media"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/media/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/milestones, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/milestones"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/milestones, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "due_on":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_fuzzable_group("state", ['open','closed']  ,quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepomilestonespost,
            'dependencies':
            [
                _repos__owner___repo__milestones_post_description.writer(),
                _repos__owner___repo__milestones_post_due_on.writer(),
                _repos__owner___repo__milestones_post_id.writer(),
                _repos__owner___repo__milestones_post_state.writer(),
                _repos__owner___repo__milestones_post_title.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/milestones"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/milestones/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/milestones/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/milestones/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/milestones/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/milestones/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("milestones"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_description.reader(), quoted=True),
    primitives.restler_static_string(""",
    "due_on":"""),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_due_on.reader(), quoted=True),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_state.reader(), quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_static_string(_repos__owner___repo__milestones_post_title.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/milestones/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/mirror-sync, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("mirror-sync"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/mirror-sync"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/notifications, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status-types="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("subject-type="),
    primitives.restler_fuzzable_group("", ['issue','pull','commit','repository']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/notifications"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/notifications, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("notifications"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("all="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("status-types="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("to-status="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("last_read_at="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/notifications"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['closed','open','all']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['oldest','recentupdate','leastupdate','mostcomment','leastcomment','priority']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("milestone="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("labels="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "assignee":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "assignees":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "base":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "due_date":"""),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=True),
    primitives.restler_static_string(""",
    "head":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "labels":
    [
        """),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
    ],
    "milestone":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepopullspost,
            'dependencies':
            [
                _repos__owner___repo__pulls_post_allow_maintainer_edit.writer(),
                _repos__owner___repo__pulls_post_body.writer(),
                _repos__owner___repo__pulls_post_due_date.writer(),
                _repos__owner___repo__pulls_post_state.writer(),
                _repos__owner___repo__pulls_post_title.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/pulls"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "allow_maintainer_edit":"""),
    primitives.restler_static_string(_repos__owner___repo__pulls_post_allow_maintainer_edit.reader(), quoted=False),
    primitives.restler_static_string(""",
    "assignee":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "assignees":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ],
    "base":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "body":"""),
    primitives.restler_static_string(_repos__owner___repo__pulls_post_body.reader(), quoted=True),
    primitives.restler_static_string(""",
    "due_date":"""),
    primitives.restler_static_string(_repos__owner___repo__pulls_post_due_date.reader(), quoted=True),
    primitives.restler_static_string(""",
    "labels":
    [
        """),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
    ],
    "milestone":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
    "state":"""),
    primitives.restler_static_string(_repos__owner___repo__pulls_post_state.reader(), quoted=True),
    primitives.restler_static_string(""",
    "title":"""),
    primitives.restler_static_string(_repos__owner___repo__pulls_post_title.reader(), quoted=True),
    primitives.restler_static_string(""",
    "unset_due_date":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}.{diffType}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("binary="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}.{diffType}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/commits, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("commits"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/commits"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/files, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("files"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("skip-to="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("whitespace="),
    primitives.restler_fuzzable_group("whitespace", ['ignore-all','ignore-change','ignore-eol','show-all']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/files"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/merge, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/merge"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/merge, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/merge"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/merge, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("merge"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "Do":"""),
    primitives.restler_fuzzable_group("Do", ['merge','rebase','rebase-merge','squash','manually-merged']  ,quoted=True),
    primitives.restler_static_string(""",
    "MergeCommitID":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "MergeMessageField":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "MergeTitleField":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "delete_branch_after_merge":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "force_merge":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "head_commit_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "merge_when_checks_succeed":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/merge"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/requested_reviewers, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requested_reviewers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/requested_reviewers"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/requested_reviewers, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requested_reviewers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/requested_reviewers"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "comments":
    [
        {
            "body":"""),
    primitives.restler_static_string(_repos__owner___repo__issues__index__comments_post_body.reader(), quoted=True),
    primitives.restler_static_string(""",
            "new_position":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "old_position":"""),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(""",
            "path":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
        }
    ],
    "commit_id":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "event":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    }"""),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerrepopullsindexreviewspost,
            'dependencies':
            [
                _repos__owner___repo__pulls__index__reviews_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__pulls__index__reviews_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__pulls__index__reviews_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews/{id}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__pulls__index__reviews_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "event":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    }"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__pulls__index__reviews_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("comments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__pulls__index__reviews_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("dismissals"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "priors":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__pulls__index__reviews_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("undismissals"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/pulls/{index}/update, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pulls"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("update"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("style="),
    primitives.restler_fuzzable_group("style", ['merge','rebase']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/pulls/{index}/update"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/push_mirrors, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_mirrors"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/push_mirrors"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/push_mirrors, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_mirrors"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "interval":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "remote_address":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "remote_password":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "remote_username":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "sync_on_commit":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/push_mirrors"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/push_mirrors-sync, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_mirrors-sync"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/push_mirrors-sync"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/push_mirrors/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_mirrors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/push_mirrors/{name}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/push_mirrors/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("push_mirrors"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/push_mirrors/{name}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/raw/{filepath}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("raw"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("ref="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/raw/{filepath}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("draft="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("pre-release="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("per_page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "body":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "draft":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "prerelease":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "tag_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "target_commitish":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerreporeleasespost,
            'dependencies':
            [
                _repos__owner___repo__releases_post_assets_0_id.writer(),
                _repos__owner___repo__releases_post_body.writer(),
                _repos__owner___repo__releases_post_draft.writer(),
                _repos__owner___repo__releases_post_name.writer(),
                _repos__owner___repo__releases_post_prerelease.writer(),
                _repos__owner___repo__releases_post_target_commitish.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/releases"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/latest, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("latest"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/latest"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/tags/{tag}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/tags/{tag}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "body":"""),
    primitives.restler_static_string(_repos__owner___repo__releases_post_body.reader(), quoted=True),
    primitives.restler_static_string(""",
    "draft":"""),
    primitives.restler_static_string(_repos__owner___repo__releases_post_draft.reader(), quoted=False),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_repos__owner___repo__releases_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "prerelease":"""),
    primitives.restler_static_string(_repos__owner___repo__releases_post_prerelease.reader(), quoted=False),
    primitives.restler_static_string(""",
    "tag_name":"""),
    primitives.restler_static_string(_repos__owner___repo__releases_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "target_commitish":"""),
    primitives.restler_static_string(_repos__owner___repo__releases_post_target_commitish.reader(), quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}/assets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}/assets"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}/assets, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_reposownerreporeleasesidassetspost,
            'dependencies':
            [
                _repos__owner___repo__releases__id__assets_post_id.writer()
            ]
        }

    },

],
requestId="/repos/{owner}/{repo}/releases/{id}/assets"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases__id__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases__id__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("releases"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases_post_assets_0_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("assets"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_repos__owner___repo__releases__id__assets_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/reviewers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviewers"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/reviewers"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/signing-key.gpg, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("signing-key.gpg"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/signing-key.gpg"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/stargazers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stargazers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/stargazers"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/statuses/{sha}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['oldest','recentupdate','leastupdate','leastindex','highestindex']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("state="),
    primitives.restler_fuzzable_group("state", ['pending','success','error','failure','warning']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/statuses/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/statuses/{sha}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statuses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "context":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "state":
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ,
    "target_url":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/statuses/{sha}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/subscribers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscribers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/subscribers"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/subscription, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/subscription"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/subscription, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/subscription"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/subscription, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscription"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/subscription"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/tags, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/tags"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/tags, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "message":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "tag_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "target":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/tags"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/tags/{tag}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/tags/{tag}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tags"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/tags/{tag}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/teams, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/teams"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/teams/{team}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/teams/{team}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/teams/{team}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/teams/{team}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/teams/{team}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("team", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/teams/{team}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/times, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("user="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/times"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/times/{user}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/times/{user}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/topics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("topics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/topics"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/topics, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("topics"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "topics":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/topics"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/topics/{topic}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("topics"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/topics/{topic}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/topics/{topic}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("topics"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("topic", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/topics/{topic}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/transfer, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transfer"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "new_owner":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "team_ids":
    [
        """),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/transfer"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/transfer/accept, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transfer"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("accept"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/transfer/accept"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/transfer/reject, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("transfer"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reject"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/transfer/reject"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/wiki/new, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wiki"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("new"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/wiki/new"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/wiki/page/{pageName}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wiki"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("page"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/wiki/page/{pageName}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/wiki/page/{pageName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wiki"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("page"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/wiki/page/{pageName}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/wiki/page/{pageName}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wiki"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("page"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/wiki/page/{pageName}"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/wiki/pages, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wiki"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("pages"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/wiki/pages"
)
req_collection.add_request(request)

# Endpoint: /repos/{owner}/{repo}/wiki/revisions/{pageName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("wiki"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("revisions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{owner}/{repo}/wiki/revisions/{pageName}"
)
req_collection.add_request(request)

# Endpoint: /repos/{template_owner}/{template_repo}/generate, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("generate"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "avatar":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "default_branch":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "git_content":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "git_hooks":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "labels":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "owner":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "private":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "topics":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "webhooks":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repos/{template_owner}/{template_repo}/generate"
)
req_collection.add_request(request)

# Endpoint: /repositories/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repositories"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/repositories/{id}"
)
req_collection.add_request(request)

# Endpoint: /settings/api, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/settings/api"
)
req_collection.add_request(request)

# Endpoint: /settings/attachment, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("attachment"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/settings/attachment"
)
req_collection.add_request(request)

# Endpoint: /settings/repository, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repository"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/settings/repository"
)
req_collection.add_request(request)

# Endpoint: /settings/ui, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("ui"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/settings/ui"
)
req_collection.add_request(request)

# Endpoint: /signing-key.gpg, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("signing-key.gpg"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/signing-key.gpg"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "can_create_org_repo":"""),
    primitives.restler_static_string(_orgs__org__teams_post_can_create_org_repo.reader(), quoted=False),
    primitives.restler_static_string(""",
    "description":"""),
    primitives.restler_static_string(_orgs__org__teams_post_description.reader(), quoted=True),
    primitives.restler_static_string(""",
    "includes_all_repositories":"""),
    primitives.restler_static_string(_orgs__org__teams_post_includes_all_repositories.reader(), quoted=False),
    primitives.restler_static_string(""",
    "name":"""),
    primitives.restler_static_string(_orgs__org__teams_post_name.reader(), quoted=True),
    primitives.restler_static_string(""",
    "permission":"""),
    primitives.restler_static_string(_orgs__org__teams_post_permission.reader(), quoted=True),
    primitives.restler_static_string(""",
    "units":"""),
    primitives.restler_static_string(_orgs__org__teams_post_units_0.reader(), quoted=False),
    primitives.restler_static_string(""",
    "units_map":"""),
    primitives.restler_static_string(_orgs__org__teams_post_units_map.reader(), quoted=False),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/members, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/members"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/members/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/members/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/members/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("members"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/members/{username}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/repos"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/repos/{org}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/repos/{org}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/repos/{org}/{repo}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/repos/{org}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /teams/{id}/repos/{org}/{repo}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("repo", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/teams/{id}/repos/{org}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /topics/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("topics"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/topics/search"
)
req_collection.add_request(request)

# Endpoint: /user, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user"
)
req_collection.add_request(request)

# Endpoint: /user/applications/oauth2, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("applications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth2"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/applications/oauth2"
)
req_collection.add_request(request)

# Endpoint: /user/applications/oauth2, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("applications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth2"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_userapplicationsoauth2post,
            'dependencies':
            [
                _user_applications_oauth2_post_id.writer()
            ]
        }

    },

],
requestId="/user/applications/oauth2"
)
req_collection.add_request(request)

# Endpoint: /user/applications/oauth2/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("applications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_applications_oauth2_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/applications/oauth2/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/applications/oauth2/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("applications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_applications_oauth2_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/applications/oauth2/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/applications/oauth2/{id}, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("applications"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("oauth2"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_applications_oauth2_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/applications/oauth2/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/emails, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "emails":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/emails"
)
req_collection.add_request(request)

# Endpoint: /user/emails, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/emails"
)
req_collection.add_request(request)

# Endpoint: /user/emails, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("emails"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "emails":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/emails"
)
req_collection.add_request(request)

# Endpoint: /user/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/followers"
)
req_collection.add_request(request)

# Endpoint: /user/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/following"
)
req_collection.add_request(request)

# Endpoint: /user/following/{username}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/following/{username}"
)
req_collection.add_request(request)

# Endpoint: /user/following/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/following/{username}"
)
req_collection.add_request(request)

# Endpoint: /user/following/{username}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("username", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/following/{username}"
)
req_collection.add_request(request)

# Endpoint: /user/gpg_key_token, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_key_token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/gpg_key_token"
)
req_collection.add_request(request)

# Endpoint: /user/gpg_key_verify, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_key_verify"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/gpg_key_verify"
)
req_collection.add_request(request)

# Endpoint: /user/gpg_keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/gpg_keys"
)
req_collection.add_request(request)

# Endpoint: /user/gpg_keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "armored_public_key":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "armored_signature":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_usergpg_keyspost,
            'dependencies':
            [
                _user_gpg_keys_post_id.writer()
            ]
        }

    },

],
requestId="/user/gpg_keys"
)
req_collection.add_request(request)

# Endpoint: /user/gpg_keys/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_gpg_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/gpg_keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/gpg_keys/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_gpg_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/gpg_keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("fingerprint="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/keys"
)
req_collection.add_request(request)

# Endpoint: /user/keys, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_userkeyspost,
            'dependencies':
            [
                _user_keys_post_id.writer()
            ]
        }

    },

],
requestId="/user/keys"
)
req_collection.add_request(request)

# Endpoint: /user/keys/{id}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/keys/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_user_keys_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/keys/{id}"
)
req_collection.add_request(request)

# Endpoint: /user/orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/orgs"
)
req_collection.add_request(request)

# Endpoint: /user/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/repos"
)
req_collection.add_request(request)

# Endpoint: /user/repos, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/repos"
)
req_collection.add_request(request)

# Endpoint: /user/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/settings"
)
req_collection.add_request(request)

# Endpoint: /user/settings, method: Patch
request = requests.Request([
    primitives.restler_static_string("PATCH "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "description":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "diff_view_style":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "full_name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "hide_activity":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "hide_email":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "language":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "location":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "theme":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "website":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/settings"
)
req_collection.add_request(request)

# Endpoint: /user/starred, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/starred"
)
req_collection.add_request(request)

# Endpoint: /user/starred/{owner}/{repo}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/starred/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /user/starred/{owner}/{repo}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/starred/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /user/starred/{owner}/{repo}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("repo", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/starred/{owner}/{repo}"
)
req_collection.add_request(request)

# Endpoint: /user/stopwatches, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stopwatches"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/stopwatches"
)
req_collection.add_request(request)

# Endpoint: /user/subscriptions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/subscriptions"
)
req_collection.add_request(request)

# Endpoint: /user/teams, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("teams"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/teams"
)
req_collection.add_request(request)

# Endpoint: /user/times, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("user"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("times"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("since="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("before="),
    primitives.restler_fuzzable_datetime("2019-06-26T20:20:39+00:00", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/user/times"
)
req_collection.add_request(request)

# Endpoint: /users/search, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("search"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("uid="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/search"
)
req_collection.add_request(request)

# Endpoint: /users/{username}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/followers, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("followers"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/followers"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/following, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/following"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/following/{target}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("following"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/following/{target}"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/gpg_keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("gpg_keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/gpg_keys"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/heatmap, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("heatmap"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/heatmap"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/keys, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("keys"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("fingerprint="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/keys"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/orgs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/orgs"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/orgs/{org}/permissions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orgs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("permissions"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/orgs/{org}/permissions"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/repos, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("repos"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/repos"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/starred, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("starred"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/starred"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/subscriptions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("subscriptions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/subscriptions"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/tokens, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tokens"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("page="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("limit="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/tokens"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/tokens, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tokens"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "name":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "scopes":
    [
        """),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string("""
    ]}"""),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/tokens"
)
req_collection.add_request(request)

# Endpoint: /users/{username}/tokens/{token}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("tokens"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/{username}/tokens/{token}"
)
req_collection.add_request(request)

# Endpoint: /version, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/api/v1"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/version"
)
req_collection.add_request(request)
