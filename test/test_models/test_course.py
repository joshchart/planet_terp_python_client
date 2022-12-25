# coding: utf-8

"""
    PlanetTerp API

    Welcome to [PlanetTerp](https://planetterp.com)'s API. This API provides access to data relating to courses, professors, and grade data at UMD.  Base URL: https://planetterp.com/api/v1  The API does not require any authentication, but please be respectful and don't hammer it with too many requests without a pause. We have a [Python wrapper](https://github.com/planetterp/PlanetTerp-API-Python-Wrapper), and we've also written an [example program](https://gist.github.com/tybug/3fcebc8a2b63d471270bda86f0756cdf) in python if you want a step by step walkthrough.  If you want a more general UMD API, check out [umd.io](https://umd.io).  For support, please email us at the email above.  The course and professor data on this website was obtained using a combination of [umd.io](https://umd.io) and UMD's [Schedule of Classes](https://app.testudo.umd.edu/soc/). The grade data is from [IRPA](https://www.irpa.umd.edu) and obtained through a [PIA](https://www.umd.edu/administration/public-information-request) request.   # noqa: E501

    The version of the OpenAPI document: v1
    Contact: admin@planetterp.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import planet_terp
from planet_terp.model.course import Course
from planet_terp import configuration


class TestCourse(unittest.TestCase):
    """Course unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()
