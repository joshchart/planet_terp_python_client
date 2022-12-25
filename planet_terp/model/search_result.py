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


class SearchResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "type",
            "slug",
        }
        
        class properties:
            name = schemas.StrSchema
            slug = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "professor": "PROFESSOR",
                        "course": "COURSE",
                    }
                
                @schemas.classproperty
                def PROFESSOR(cls):
                    return cls("professor")
                
                @schemas.classproperty
                def COURSE(cls):
                    return cls("course")
            __annotations__ = {
                "name": name,
                "slug": slug,
                "type": type,
            }
    
    name: MetaOapg.properties.name
    type: MetaOapg.properties.type
    slug: MetaOapg.properties.slug
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "slug", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "slug", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        slug: typing.Union[MetaOapg.properties.slug, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SearchResult':
        return super().__new__(
            cls,
            *_args,
            name=name,
            type=type,
            slug=slug,
            _configuration=_configuration,
            **kwargs,
        )
