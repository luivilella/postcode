from app.uk import is_valid_uk_postcode


class TestIsValidUKPostcode:
    def test_when_area_do_not_starts_with_a_letter_returns_invalid(self):
        assert not is_valid_uk_postcode('*C1A 1BB')

    def test_when_district_is_not_digit_returns_invalid(self):
        assert not is_valid_uk_postcode('EC*A 1BB')

    def test_when_sector_is_not_digit_returns_invalid(self):
        assert not is_valid_uk_postcode('EC1A *BB')

    def test_when_unit_are_not_letters_returns_invalid(self):
        assert not is_valid_uk_postcode('EC1A 1**')

    def test_when_unit_does_not_have_two_letters_returns_invalid(self):
        assert not is_valid_uk_postcode('EC1A 1B')

    def test_when_the_space_is_missing_retunrs_invalid(self):
        assert not is_valid_uk_postcode('EC1A1BB')

    def test_when_format_is_AA9A_9AA_returns_valid(self):
        'The format is as follows, where A signifies a letter and 9 a digit'
        assert is_valid_uk_postcode('EC1A 1BB')

    def test_when_format_is_A9A_9AA_returns_valid(self):
        'The format is as follows, where A signifies a letter and 9 a digit'
        assert is_valid_uk_postcode('W1A 0AX')

    def test_when_format_is_A9_9AA_returns_valid(self):
        'The format is as follows, where A signifies a letter and 9 a digit'
        assert is_valid_uk_postcode('M1 1AE')

    def test_when_format_is_A99_9AA_returns_valid(self):
        'The format is as follows, where A signifies a letter and 9 a digit'
        assert is_valid_uk_postcode('B33 8TH')

    def test_when_format_is_AA9_9AA_returns_valid(self):
        'The format is as follows, where A signifies a letter and 9 a digit'
        assert is_valid_uk_postcode('CR2 6XH')

    def test_when_format_is_AA99_9AA_returns_valid(self):
        'The format is as follows, where A signifies a letter and 9 a digit'
        assert is_valid_uk_postcode('DN55 1PT')

    def test_when_AB_area_should_have_two_digits_in_district(self):
        assert not is_valid_uk_postcode('AB1 1AA')
