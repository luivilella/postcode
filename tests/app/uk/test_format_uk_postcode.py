import pytest
from postcode.uk import format_uk_postcode, InvalidUKPostcode


class TestFormatUKPostcode:
    def test_when_space_is_missing_returns_well_formated(self):
        expected_value = 'DN55 1PT'
        assert format_uk_postcode('DN551PT') == expected_value

    def test_when_in_lower_case_returns_well_formated(self):
        expected_value = 'DN55 1PT'
        assert format_uk_postcode('dn551pt') == expected_value

    def test_returns_well_formated(self):
        expected_value = 'DN55 1PT'
        assert format_uk_postcode('D N 5 5 1 P T') == expected_value

    def test_when_validation_is_required_and_is_invalid_raise_an_error(self):
        with pytest.raises(InvalidUKPostcode):
            assert format_uk_postcode('D N 5 5 1 P *', True)
