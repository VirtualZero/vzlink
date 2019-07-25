def ns_shorten_description_text():
    return """<p style='font-size: 16px;'>The link-shortener namespace \
    contains the routes for link-shortening services. \
    <a href='#'>Click here</a> to view the routes.</p>"""


def shorten_description_text():
    return """<p style='font-size: 16px;'>Make a POST request to this 
    route to shorten a link. The request must include a URL as the 
    payload and your API key in the header. The API will return a 
    short URL as the response payload.</p>"""



def api_description_text():
    return """<p style='font-size: 16px;'>VZLink is a RESTful API that 
    provides link shortener services to independent applications. Similar 
    to the popular link shortener service, Bitly, VZLink accepts a long URL, 
    or link, and returns a much shorter and memorable link. This API is 
    open source and the code can be viewed or cloned on 
    <a href='https://github.com/VirtualZero/vzlink' target='_blank'>
    GitHub</a>.</p>"""
    #Once complete, add -
    #Additionally, a preconfigured virtual machine in OVA format \
    #is available for download <a href='https://vzl.ink/#download' 
    # target='_blank'>here</a>.


def ns_user_description_text():
    return """<p style='font-size: 16px;'>The user namespace contains \
    the routes for user operations, such as creating an account, \
    refreshing an API key, etc. <a href='#'>Click here</a> to view \
    the routes.</p>"""


def create_account_description_text():
    return """<p style='font-size: 16px;'>Make a POST request to 
    this route to create an account. The request must include a 
    valid email address and matching password and confirm_password 
    fields as the request payload. Upon successful account creation, 
    the API will return an API key and refresh API key as the 
    response payload. You must use the API key when requesting 
    datetime data from the API. The API key will expire in 365 days. 
    You must use your refresh API key to obtain a new API key.</p>"""


def get_new_api_key_description_text():
    return """<p style='font-size: 16px;'>Obtain a new API key by making a GET 
    request to this route. The request must include the refresh API key in the 
    header. The new API key will be returned in the response payload and the 
    old API key will be invalidated immediately.</p>"""


def forgot_api_keys_description_text():
    return """<p style='font-size: 16px;'>If you lose your API keys, make a 
    POST request to this route. The request must contain the email address 
    and password that the account was created with. The API will return the 
    API key and refresh API as the response payload.</p>"""


def get_new_refresh_api_key_description_text():
    return """<p style='font-size: 16px;'>Obtain a new refresh API key by 
    making a POST request to this route. The request must contain the email 
    address that the account was created with and the current account password. 
    The new refresh API key will be returned as the response payload and the 
    old refresh API key will be invalidated immediately.</p>"""


def update_password_description_text():
    return """<p style='font-size: 16px;'>Make a POST request to this route 
    to update a password. The request must contain the email address that the 
    account was created with, the current account password, and a 'new_password' 
    field containing the desired new password. The new password must be between 
    8-64 characters. Upon successful completion of the request, the API will 
    return a success message and the old password will be invalidated 
    immediately.</p>"""
