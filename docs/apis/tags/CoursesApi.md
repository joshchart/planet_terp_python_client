<a name="__pageTop"></a>
# planet_terp.apis.tags.courses_api.CoursesApi

All URIs are relative to *https://planetterp.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_a_course**](#get_a_course) | **get** /course | 
[**get_courses**](#get_courses) | **get** /courses | 

# **get_a_course**
<a name="get_a_course"></a>
> Course get_a_course(name)



Gets the specified courses

### Example

```python
import planet_terp
from planet_terp.apis.tags import courses_api
from planet_terp.model.course import Course
from pprint import pprint
# Defining the host is optional and defaults to https://planetterp.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = planet_terp.Configuration(
    host = "https://planetterp.com/api/v1"
)

# Enter a context with an instance of the API client
with planet_terp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'name': "MATH140",
    }
    try:
        api_response = api_instance.get_a_course(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling CoursesApi->get_a_course: %s\n" % e)

    # example passing only optional values
    query_params = {
        'name': "MATH140",
        'reviews': False,
    }
    try:
        api_response = api_instance.get_a_course(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling CoursesApi->get_a_course: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
reviews | ReviewsSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ReviewsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_a_course.ApiResponseFor200) | Returns course matching query
400 | [ApiResponseFor400](#get_a_course.ApiResponseFor400) | bad input parameter

#### get_a_course.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Course**](../../models/Course.md) |  | 


#### get_a_course.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_courses**
<a name="get_courses"></a>
> [Course] get_courses()



Get all courses, in alphabetical order

### Example

```python
import planet_terp
from planet_terp.apis.tags import courses_api
from planet_terp.model.course import Course
from pprint import pprint
# Defining the host is optional and defaults to https://planetterp.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = planet_terp.Configuration(
    host = "https://planetterp.com/api/v1"
)

# Enter a context with an instance of the API client
with planet_terp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = courses_api.CoursesApi(api_client)

    # example passing only optional values
    query_params = {
        'department': "MATH",
        'reviews': False,
        'limit': 1,
        'offset': 0,
    }
    try:
        api_response = api_instance.get_courses(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling CoursesApi->get_courses: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
department | DepartmentSchema | | optional
reviews | ReviewsSchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# DepartmentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ReviewsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 100

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_courses.ApiResponseFor200) | Returns courses matching query
400 | [ApiResponseFor400](#get_courses.ApiResponseFor400) | bad input parameter

#### get_courses.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Course**]({{complexTypePrefix}}Course.md) | [**Course**]({{complexTypePrefix}}Course.md) | [**Course**]({{complexTypePrefix}}Course.md) |  | 

#### get_courses.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

