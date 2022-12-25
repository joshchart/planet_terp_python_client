<a name="__pageTop"></a>
# planet_terp.apis.tags.grades_api.GradesApi

All URIs are relative to *https://planetterp.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_grades**](#get_grades) | **get** /grades | 

# **get_grades**
<a name="get_grades"></a>
> [Grades] get_grades()



Get grades for a course, a professor, or both. If by course, returns all of the grades available by section.  <aside class=\"notice\"> At least one of <code>course</code> and <code>professor</code> is required. </aside> 

### Example

```python
import planet_terp
from planet_terp.apis.tags import grades_api
from planet_terp.model.grades import Grades
from pprint import pprint
# Defining the host is optional and defaults to https://planetterp.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = planet_terp.Configuration(
    host = "https://planetterp.com/api/v1"
)

# Enter a context with an instance of the API client
with planet_terp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grades_api.GradesApi(api_client)

    # example passing only optional values
    query_params = {
        'course': "MATH140",
        'professor': "Jon Snow",
        'semester': "202001",
        'section': "0101",
    }
    try:
        api_response = api_instance.get_grades(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling GradesApi->get_grades: %s\n" % e)
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
course | CourseSchema | | optional
professor | ProfessorSchema | | optional
semester | SemesterSchema | | optional
section | SectionSchema | | optional


# CourseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfessorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SemesterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SectionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_grades.ApiResponseFor200) | Returns grades matching query
400 | [ApiResponseFor400](#get_grades.ApiResponseFor400) | bad input parameter

#### get_grades.ApiResponseFor200
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
[**Grades**]({{complexTypePrefix}}Grades.md) | [**Grades**]({{complexTypePrefix}}Grades.md) | [**Grades**]({{complexTypePrefix}}Grades.md) |  | 

#### get_grades.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

