import os
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():
    return "Microsoft Graph Webhook is running."


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    # Microsoft Graph validation request
    validation_token = request.args.get("validationToken")

    if validation_token:
        print("Validation request received")
        return Response(
            validation_token,
            status=200,
            mimetype="text/plain"
        )

    # Notification received
    notifications = request.get_json(silent=True)

    print("Notifications:")
    print(notifications)

    # TODO:
    # Process the notifications here
    # Fetch the email/message from Microsoft Graph if needed

    return jsonify({"status": "received"}), 202


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )