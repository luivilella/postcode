from collections import namedtuple
from bottle import get, abort, run
from .uk import is_valid_uk_postcode, format_uk_postcode


CountryOption = namedtuple('CountryOption', 'is_valid format')
countries = dict(
    UK=CountryOption(is_valid_uk_postcode, format_uk_postcode)
)


@get('/postcode/<country>/<postcode>')
def postcode(country, postcode):

    validator = countries.get(country.upper())
    if not validator:
        abort(400, 'Country not supported.')

    formated = validator.format(postcode)
    return dict(
        data=dict(
            is_valid=validator.is_valid(formated),
            formated=formated,
        )
    )


if '__main__' in __name__:
    run(host='0.0.0.0', port=8080)
