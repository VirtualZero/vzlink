from flask import redirect
from vzlink import app, db
from vzlink.models.link import Link


@app.route('/<hash_id>')
def redirect_to_long_link(hash_id):
    long_link = Link.query.filter_by(
        hash_id=hash_id
    ).first_or_404().long_link

    return redirect(long_link)
