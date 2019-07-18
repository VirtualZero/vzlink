from vzlink import app
from flask import jsonify, request, render_template

@app.errorhandler(404)
def error_404(error):
    if request.content_type == 'application/json':
        return jsonify({
            "message": "ERROR: Not Found (404)"
        }), 404

    error_msg = "The page you're looking for does not exist."
    status_msg = "<strong>Status:</strong> Not Found"
    status_code = 404
    code_msg = "<strong>Status Code:</strong> "
    return render_template(
        'http_error/error.html',
        title="Not Found (404)",
        error_msg=error_msg,
        status_msg=status_msg,
        code_msg=code_msg,
        status_code=status_code), 404


@app.errorhandler(403)
def error_403(error):
    if request.content_type == 'application/json':
        return jsonify({
            "message": "ERROR: Forbidden (403)"
        }), 403

    error_msg = "Permission Denied."
    status_msg = "<strong>Status:</strong> Forbidden"
    status_code = 403
    code_msg = "<strong>Status Code:</strong> "
    return render_template(
        'http_error/error.html',
        title="Forbidden (403)",
        error_msg=error_msg,
        status_msg=status_msg,
        code_msg=code_msg,
        status_code=status_code), 403


@app.errorhandler(500)
def error_500(error):
    if request.content_type == 'application/json':
        return jsonify({
            "message": "ERROR: Something went wrong. (500)"
        }), 500

    error_msg = "Something went wrong on our end."
    status_msg = "<strong>Status:</strong> Internal Server Error"
    status_code = 500
    code_msg = "<strong>Status Code:</strong> "
    return render_template(
        'http_error/error.html',
        title="Internal Server Error (500)",
        error_msg=error_msg,
        status_msg=status_msg,
        code_msg=code_msg,
        status_code=status_code), 500


@app.errorhandler(405)
def error_405(error):
    if request.content_type == 'application/json':
        return jsonify({
            "message": "ERROR: Invalid request method. (405)"
        }), 405

    error_msg = "Invalid request method."
    status_msg = "<strong>Status:</strong> Method Not Allowed"
    status_code = 405
    code_msg = "<strong>Status Code:</strong> "
    return render_template(
        'http_error/error.html',
        title="Internal Server Error (405)",
        error_msg=error_msg,
        status_msg=status_msg,
        code_msg=code_msg,
        status_code=status_code), 405


@app.errorhandler(400)
def error_400(error):
    if request.content_type == 'application/json':
        return jsonify({
            "message": "Something was not right about the request. (400)"
        }), 400

    error_msg = "A bad request was made on your end."
    status_msg = "<strong>Status:</strong> Bad Request"
    status_code = 400
    code_msg = "<strong>Status Code:</strong> "
    return render_template(
        'http_error/error.html',
        title="Bad Request (400)",
        error_msg=error_msg,
        status_msg=status_msg,
        code_msg=code_msg,
        status_code=status_code), 400
