"""Auto-generated file, do not edit by hand. AU metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AU = PhoneMetadata(id='AU', country_code=61, international_prefix='001[14-689]|14(?:1[14]|34|4[17]|[56]6|7[47]|88)0011',
    general_desc=PhoneNumberDesc(national_number_pattern='1\\d{4,9}|(?:[2-478]\\d\\d|550)\\d{6}', possible_length=(5, 6, 7, 8, 9, 10), possible_length_local_only=(8,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:[237]\\d{5}|8(?:51(?:0(?:0[03-9]|[1247]\\d|3[2-9]|5[0-8]|6[1-9]|8[0-6])|1(?:1[69]|[23]\\d|4[0-4]))|(?:[6-8]\\d{3}|9(?:[02-9]\\d\\d|1(?:[0-57-9]\\d|6[0135-9])))\\d))\\d{3}', example_number='212345678', possible_length=(9,), possible_length_local_only=(8,)),
    mobile=PhoneNumberDesc(national_number_pattern='4(?:[0-3]\\d|4[047-9]|5[0-25-9]|6[6-9]|7[02-9]|8[0-2457-9]|9[017-9])\\d{6}', example_number='412345678', possible_length=(9,)),
    toll_free=PhoneNumberDesc(national_number_pattern='180(?:0\\d{3}|2)\\d{3}', example_number='1800123456', possible_length=(7, 10)),
    premium_rate=PhoneNumberDesc(national_number_pattern='190[0-26]\\d{6}', example_number='1900123456', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='13(?:00\\d{3}|45[0-4])\\d{3}|13\\d{4}', example_number='1300123456', possible_length=(6, 8, 10)),
    voip=PhoneNumberDesc(national_number_pattern='(?:14(?:5(?:1[0458]|[23][458])|71\\d)|550\\d\\d)\\d{4}', example_number='550123456', possible_length=(9,)),
    pager=PhoneNumberDesc(national_number_pattern='16\\d{3,7}', example_number='1612345', possible_length=(5, 6, 7, 8, 9)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='1[38]00\\d{6}|1(?:345[0-4]|802)\\d{3}|13\\d{4}', possible_length=(6, 7, 8, 10)),
    preferred_international_prefix='0011',
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['16'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['13']),
        NumberFormat(pattern='(\\d{3})(\\d{3})', format='\\1 \\2', leading_digits_pattern=['19']),
        NumberFormat(pattern='(\\d{3})(\\d{4})', format='\\1 \\2', leading_digits_pattern=['180', '1802']),
        NumberFormat(pattern='(\\d{4})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['19']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['16'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['14|[45]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2378]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:30|[89])'])],
    intl_number_format=[NumberFormat(pattern='(\\d{2})(\\d{3,4})', format='\\1 \\2', leading_digits_pattern=['16']),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{2,4})', format='\\1 \\2 \\3', leading_digits_pattern=['16']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['14|[45]']),
        NumberFormat(pattern='(\\d)(\\d{4})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['[2378]']),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['1(?:30|[89])'])],
    main_country_for_code=True,
    mobile_number_portable_region=True)
