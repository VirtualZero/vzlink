from flask import request, redirect, render_template, url_for
from vzlink import app, db
from vzlink.models.link import Link
import os


@app.route('/<hash_id>')
def redirect_to_long_link(hash_id):
    long_link = Link.query.filter_by(
        hash_id=hash_id
    ).first_or_404().long_link

    return redirect(long_link)


@app.route('/')
def home():
    cdn_https = app.config['CDN_HTTPS_ROOT']
    return render_template(
        'landing.html',
        title='VZLink',
        cdn_https=cdn_https
    )
