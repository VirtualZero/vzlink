from flask import request, redirect, render_template, jsonify
from vzlink import app, db, csrf, cache
from vzlink.models.link import Link
from vzlink.forms.forms import URL_Form, ContactForm
from vzlink import hashids_
import requests
import os


@app.route('/<hash_id>')
@cache.cached()
def redirect_to_long_link(hash_id):
    print(hash_id)
    long_link = Link.query.filter_by(
        hash_id=hash_id
    ).first_or_404().long_link

    return redirect(long_link)


@app.route('/')
def home():
    contact_form = ContactForm()
    url_form = URL_Form()
    cdn_https = app.config['CDN_HTTPS_ROOT']
    return render_template(
        'landing.html',
        title='VZLink',
        cdn_https=cdn_https,
        url_form=url_form,
        contact_form=contact_form
    )


@app.route('/app/get-short-link', methods=['POST'])
def make_short_link():
    url_form = URL_Form()

    new_short_link = Link(
        1, # Default App User for App Side
        url_form.url.data
    )

    db.session.add(new_short_link)
    db.session.flush()

    hash_id = hashids_.encode(new_short_link.id)
    short_url = f'https://vzl.ink/{hash_id}'

    new_short_link.hash_id = hash_id
    db.session.commit()

    return jsonify(
        {
            "url": short_url
        }
    )

@app.route('/submit-message', methods=['POST'])
def submit_message():
    contact_form = ContactForm()

    if contact_form.validate_on_submit():
        send_message = requests.post(
            os.environ['MAIL_API_URL'],
            headers={
                'X-API-KEY': os.environ['MAIL_API_KEY']
            },
            json={
                "recipients": ["birtchum@virtualzero.net"],
                "subject": "New message from VZLink",
                "message": make_message(contact_form)
            }
        )

        return jsonify(
            {
                'status': 'success'
            }
        ), 200

    else:
        errors = {}

        for fieldName, errorMessages in contact_form.errors.items():
            errors[fieldName] = errorMessages[0]

        return jsonify(
            {
                'status': 'error',
                'errors': errors
            }
        ), 400


def make_message(contact_form):
    return f"Here are the details of the message:\n" \
           f"First Name: {contact_form.contact_first_name.data}\n" \
           f"Last Name: {contact_form.contact_last_name.data}\n" \
           f"Email: {contact_form.contact_email.data}\n" \
           f"Phone: {contact_form.contact_phone.data}\n" \
           f"Email: {contact_form.message.data}"
