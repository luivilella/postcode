# postcode
Project to create validators for postcode.

You can use as a library or you can deploy and have an web api to validate your postcodes.

## Python support
- 3.6.4

## Countries support
- UK

## Import and use
    In [1]: from postcode.uk import is_valid_uk_postcode, format_uk_postcode

    In [2]: is_valid_uk_postcode('EC1A 1BB')
    Out[2]: True

    In [3]: is_valid_uk_postcode('EC1A 1B*')
    Out[3]: False

    In [4]: format_uk_postcode('e C 1 a    1 b B')
    Out[4]: 'EC1A 1BB'

    In [5]: format_uk_postcode('e C 1 a    1 b *')
    Out[5]: ''

## Running tests

    $ pytest
    ========================================================= test session starts =========================================================
    platform linux -- Python 3.6.4, pytest-3.4.1, py-1.5.2, pluggy-0.6.0
    rootdir: /deploy, inifile:
    collected 17 items

    tests/app/uk/test_format_uk_postcode.py ....                                                                                    [ 23%]
    tests/app/uk/test_is_valid_uk_postcode.py .............                                                                         [100%]

    ====================================================== 17 passed in 0.70 seconds ======================================================

## Deploying the web API

- Make sure that you have docker installed

        $ docker --version
        Docker version 17.12.0-ce, build c97c6d6
        
        $ docker-compose --version
        docker-compose version 1.18.0, build 8dd22a9

- Copy the nginx template and change for your needs

        $ cp nginx.conf.template nginx.conf
        $ vi nginx.conf

- Build and run the containers

        $ docker-compose up -d

- Check the web url

        $ curl http://localhost/postcode/uk/DN551PT
        {"data": {"is_valid": true, "formated": "DN55 1PT"}}
