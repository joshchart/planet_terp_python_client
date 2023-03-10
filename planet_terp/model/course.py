# coding: utf-8

"""
    PlanetTerp API

    Welcome to [PlanetTerp](https://planetterp.com)'s API. This API provides access to data relating to courses, professors, and grade data at UMD.  Base URL: https://planetterp.com/api/v1  The API does not require any authentication, but please be respectful and don't hammer it with too many requests without a pause. We have a [Python wrapper](https://github.com/planetterp/PlanetTerp-API-Python-Wrapper), and we've also written an [example program](https://gist.github.com/tybug/3fcebc8a2b63d471270bda86f0756cdf) in python if you want a step by step walkthrough.  If you want a more general UMD API, check out [umd.io](https://umd.io).  For support, please email us at the email above.  The course and professor data on this website was obtained using a combination of [umd.io](https://umd.io) and UMD's [Schedule of Classes](https://app.testudo.umd.edu/soc/). The grade data is from [IRPA](https://www.irpa.umd.edu) and obtained through a [PIA](https://www.umd.edu/administration/public-information-request) request.   # noqa: E501

    The version of the OpenAPI document: v1
    Contact: admin@planetterp.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from planet_terp import schemas  # noqa: F401


class Course(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "course_number",
            "credits",
            "professors",
            "description",
            "department",
            "title",
        }
        
        class properties:
            department = schemas.StrSchema
            course_number = schemas.StrSchema
            title = schemas.StrSchema
            description = schemas.StrSchema
            credits = schemas.IntSchema
            
            
            class professors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'professors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            average_gpa = schemas.NumberSchema
            __annotations__ = {
                "department": department,
                "course_number": course_number,
                "title": title,
                "description": description,
                "credits": credits,
                "professors": professors,
                "average_gpa": average_gpa,
            }
    
    course_number: MetaOapg.properties.course_number
    credits: MetaOapg.properties.credits
    professors: MetaOapg.properties.professors
    description: MetaOapg.properties.description
    department: MetaOapg.properties.department
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["course_number"]) -> MetaOapg.properties.course_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credits"]) -> MetaOapg.properties.credits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["professors"]) -> MetaOapg.properties.professors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["average_gpa"]) -> MetaOapg.properties.average_gpa: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["department", "course_number", "title", "description", "credits", "professors", "average_gpa", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["course_number"]) -> MetaOapg.properties.course_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credits"]) -> MetaOapg.properties.credits: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["professors"]) -> MetaOapg.properties.professors: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["average_gpa"]) -> typing.Union[MetaOapg.properties.average_gpa, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["department", "course_number", "title", "description", "credits", "professors", "average_gpa", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        course_number: typing.Union[MetaOapg.properties.course_number, str, ],
        credits: typing.Union[MetaOapg.properties.credits, decimal.Decimal, int, ],
        professors: typing.Union[MetaOapg.properties.professors, list, tuple, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        department: typing.Union[MetaOapg.properties.department, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        average_gpa: typing.Union[MetaOapg.properties.average_gpa, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Course':
        return super().__new__(
            cls,
            *_args,
            course_number=course_number,
            credits=credits,
            professors=professors,
            description=description,
            department=department,
            title=title,
            average_gpa=average_gpa,
            _configuration=_configuration,
            **kwargs,
        )
