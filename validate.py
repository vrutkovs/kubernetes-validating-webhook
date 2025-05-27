from flask import Flask, request, jsonify
from os import environ
import logging

webhook = Flask(__name__)

webhook.config['LABEL'] = environ.get('LABEL')

webhook.logger.setLevel(logging.INFO)

@webhook.route('/validate', methods=['POST'])
def validating_webhook():
    request_info = request.get_json()
    uid = request_info["request"].get("uid")
    webhook.logger.info(f"request:\n{request_info}")

    return admission_response(True, uid, "lets go")


def admission_response(allowed, uid, message):
    return jsonify({"apiVersion": "admission.k8s.io/v1",
                    "kind": "AdmissionReview",
                    "response":
                        {"allowed": allowed,
                         "uid": uid,
                         "status": {"message": message}
                         }
                    })


if __name__ == '__main__':
    webhook.run(host='0.0.0.0',
                port=5000)
