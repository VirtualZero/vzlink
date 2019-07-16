from flask import request, abort, Blueprint
from vzlink import app, db, csrf
from flask_restplus import Api, Resource, fields


from vzlink.helpers.api_helpers import (
    token_required,
    valid_email_required,
    create_account_creds_required,
    create_new_user,
    refresh_token_required,
    make_new_api_key,
    creds_required,
    get_api_keys,
    make_new_refresh_api_key,
    update_password,
    shorten_url,
    validate_url
)

from vzlink.helpers.description_text import (
    api_description_text,
    ns_datetime_description_text,
    ns_user_description_text,
    get_current_timestamp_description_text,
    create_account_description_text,
    convert_timezones_description_text,
    addition_description_text,
    subtraction_description_text,
    difference_description_text,
    get_new_api_key_description_text,
    forgot_api_keys_description_text,
    get_new_refresh_api_key_description_text,
    update_password_description_text
)

blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api/v1'
)

csrf.exempt(blueprint)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

api = Api(
    blueprint,
    authorizations=authorizations,
    title='VIRTUALZERO LINK SHORTENER API',
    version='1.0',
    description=api_description_text(),
    validate=True
)

app.register_blueprint(blueprint)


# Namespaces
ns_shorten = api.namespace(
    'link-shortener',
    description='Link Shortener...'
)

ns_user = api.namespace(
    'user',
    description=ns_user_description_text()
)


# API Models
new_api_user = ns_user.model(
    'NewUser',
    {
        'email': fields.String('email', required=True),
        'password': fields.String('password', required=True),
        'confirm_password': fields.String('confirm_password', required=True)
    }
)

api_user = ns_user.model(
    'User',
    {
        'email': fields.String('email', required=True),
        'password': fields.String('password', required=True)
    }
)

new_password = ns_user.model(
    'UpdatePassword',
    {
        'email': fields.String('email', required=True),
        'password': fields.String('password', required=True),
        'new_password': fields.String('password', required=True)
    }
)

long_url = ns_shorten.model(
    'LongURL',
    {
        'url': fields.String('url', required=True)
    }
)


# Endpoints
@ns_user.route('/create-account')
class CreateAccount(Resource):
    @ns_user.expect(new_api_user)
    @ns_user.doc(
        description=create_account_description_text()
    )
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        })
    @create_account_creds_required
    def post(self):
        return create_new_user(), 200


@ns_shorten.route('/shorten')
class Shorten(Resource):
    @ns_shorten.expect(long_url)
    @ns_shorten.doc(
        description='coming soon',
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @token_required
    @validate_url
    def post(self):
        return shorten_url(), 200


@ns_user.route('/get-new-api-key')
class GetNewAPIKey(Resource):
    @ns_user.doc(
        description=get_new_api_key_description_text()
    )
    @ns_user.doc(security='apikey')
    @ns_user.header(
        'X-API-KEY',
        'Must include the refresh API key in header.'
    )
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @refresh_token_required
    def get(self):
        return make_new_api_key(), 200


@ns_user.route('/forgot-api-keys')
class ForgotAPIKeys(Resource):
    @ns_user.doc(
        description=forgot_api_keys_description_text()
    )
    @ns_user.expect(api_user)
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @creds_required
    def post(self):
        return get_api_keys(), 200


@ns_user.route('/get-new-refresh-api-key')
class GetNewRefreshAPIKey(Resource):
    @ns_user.doc(
        description=get_new_refresh_api_key_description_text()
    )
    @ns_user.expect(api_user)
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @creds_required
    def post(self):
        return make_new_refresh_api_key(), 200


@ns_user.route('/update-password')
class UpdatePassword(Resource):
    @ns_user.doc(
        description=update_password_description_text()
    )
    @ns_user.expect(new_password)
    @ns_user.doc(
        responses={
            200: 'Success',
            401: 'Not Authorized',
            500: 'Something went wrong.'
        }
    )
    @creds_required
    def post(self):
        return update_password(), 200
