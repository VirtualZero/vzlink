from flask import request, redirect, render_template, jsonify
from vzlink import app, db, csrf
from vzlink.models.link import Link
from vzlink.forms.forms import URL_Form
from vzlink import hashids_
import os


@app.route('/<hash_id>')
def redirect_to_long_link(hash_id):
    long_link = Link.query.filter_by(
        hash_id=hash_id
    ).first_or_404().long_link

    return redirect(long_link)


@app.route('/')
def home():
    url_form = URL_Form()
    cdn_https = app.config['CDN_HTTPS_ROOT']
    return render_template(
        'landing.html',
        title='VZLink',
        cdn_https=cdn_https,
        url_form=url_form
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
