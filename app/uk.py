import re


'Thanks UK government to provide this regex: https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/488478/Bulk_Data_Transfer_-_additional_validation_valid_from_12_November_2015.pdf'  # noqa: E501
POSTCODE_REGEX = re.compile(
    r'^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'  # noqa: E501
)

AREAS_SINGLE_DIGIT_DISTRICT = set(
    'BR FY HA HD HG HR HS HX JE LD SM SR WC WN ZE'.split()
)
AREAS_DOUBLE_DIGITS_DISTRICT = {'AB', 'LL', 'SO'}
AREAS_DISTRICT_ZERO = set('BL BS CM CR FY HA PR SL SS'.split())
OUTWARD_CODE_DISTRICTS_WITH_FINAL_LETTER = set(
    'EC1 EC4 SW1 W1 WC1 WC2 E1 N1 NW1 SE1'.split()
)
INVALID_AREA_FIST_LETTER = {'Q', 'V', 'X'}
INVALID_AREA_SECOND_LETTER = {'I', 'J', 'Z'}
VALID_DISTRICT_LETTER = {
    1: set(list('ABCDEFGHJKPSTUW')),
    2: set(list('ABEHMNPRVWXY')),
}
INVALID_LETTERS_IN_UNIT = set(list('CIKMOV'))


def is_valid_uk_postcode(postcode: str) -> bool:
    """Function to validade UK postcodes"""
    if not POSTCODE_REGEX.match(postcode):
        return False

    outward_code, inward_code = postcode.split(' ')

    if outward_code[1].isdigit():
        area, district = outward_code[0:1], outward_code[1:]
    else:
        area, district = outward_code[0:2], outward_code[2:]

    sector, unit = inward_code[0], inward_code[1:]

    """
        Areas with only single-digit districts:
        BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    """
    if area in AREAS_SINGLE_DIGIT_DISTRICT and len(district) != 1:
        return False

    """
        Areas with only double-digit districts: AB, LL, SO.
    """
    if area in AREAS_DOUBLE_DIGITS_DISTRICT and len(district) != 2:
        return False

    """
        Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS
        (BS is the only area to have both a district 0 and a district 10).
    """
    if district == '0' and area not in AREAS_DISTRICT_ZERO:
        return False

    """
        The following central London single-digit districts have been further
        divided by inserting a letter after the digit and before the space:
        EC1–EC4 (but not EC50), SW1, W1, WC1, WC2, and part of E1 (E1W),
        N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
    """
    if (
        not district[-1].isdigit() and
        outward_code[:-1] not in OUTWARD_CODE_DISTRICTS_WITH_FINAL_LETTER
    ):
        return False

    """
        The letters QVX are not used in the first position.
    """
    if area[0] in INVALID_AREA_FIST_LETTER:
        return False

    """
        The letters IJZ are not used in the second position.
    """
    if len(area) > 1 and area[1] in INVALID_AREA_SECOND_LETTER:
        return False

    """
        The only letters to appear in the third position are ABCDEFGHJKPSTUW
        when the structure starts with A9A.
        The only letters to appear in the fourth position are ABEHMNPRVWXY
        when the structure starts with AA9A
    """
    if (
        not district[-1].isdigit() and
        district[-1] not in VALID_DISTRICT_LETTER[len(area)]
    ):
        return False

    """
        The final two letters do not use the letters CIKMOV,
        so as not to resemble digits or each other when hand-written.
    """
    if set(list(unit)) & INVALID_LETTERS_IN_UNIT:
        return False

    return True


class InvalidUKPostcode(Exception):
    pass


def format_uk_postcode(postcode: str, validate: bool = False) -> str:
    """Function to format UK postcodes"""
    postcode_no_spaces = postcode.replace(' ', '').upper()
    new_postcode = f'{postcode_no_spaces[:-3]} {postcode_no_spaces[-3:]}'
    if not is_valid_uk_postcode(new_postcode):
        if not validate:
            return ''
        raise InvalidUKPostcode

    return new_postcode
