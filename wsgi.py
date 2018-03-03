from postcode.web_api import application, run  # noqa: F401

if '__main__' in __name__:
    run(host='0.0.0.0', port=8080)
