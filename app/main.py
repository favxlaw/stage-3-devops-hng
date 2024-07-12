from flask import Blueprint, request, jsonify
from .tasks import send_email_task, log_time_task

app = Blueprint('app', __name__)

@app.route('/message')
def message():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email_task.delay(sendmail)
        return jsonify({"status": "Email is being sent."})

    if talktome:
        log_time_task.delay()
        return jsonify({"status": "Time is being logged."})

    return jsonify({"status": "No action specified."})

if __name__ == '__main__':
    from . import create_app
    app = create_app()
    app.run(debug=True)
