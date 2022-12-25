<a name="__pageTop"></a>
# planet_terp.apis.tags.professors_api.ProfessorsApi

All URIs are relative to *https://planetterp.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_a_professor**](#get_a_professor) | **get** /professor | 
[**get_all_professors**](#get_all_professors) | **get** /professors | 

# **get_a_professor**
<a name="get_a_professor"></a>
> Professor get_a_professor(name)



Get the specified professor.  <aside class=\"notice\"> <code>slug</code> is PlanetTerp's identifier for professors. Slugs are unique to a professor and is often, but not always, their last name. <br/><br/> You may find a professor's slug useful to get a unique identifier for professors, or to link to a professor's page on PlanetTerp (via <code>https://planetterp.com/professor/SLUG</code>). <br/><br/> For example, Jon Snow's slug might be <code>snow</code>. <br/><br/> </aside> 

### Example

```python
import planet_terp
from planet_terp.apis.tags import professors_api
from planet_terp.model.professor import Professor
from pprint import pprint
# Defining the host is optional and defaults to https://planetterp.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = planet_terp.Configuration(
    host = "https://planetterp.com/api/v1"
)

# Enter a context with an instance of the API client
with planet_terp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = professors_api.ProfessorsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'name': "Jon Snow",
    }
    try:
        api_response = api_instance.get_a_professor(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling ProfessorsApi->get_a_professor: %s\n" % e)

    # example passing only optional values
    query_params = {
        'name': "Jon Snow",
        'reviews': True,
    }
    try:
        api_response = api_instance.get_a_professor(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling ProfessorsApi->get_a_professor: %s\n" % e)
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
200 | [ApiResponseFor200](#get_a_professor.ApiResponseFor200) | Returns professor matching query
400 | [ApiResponseFor400](#get_a_professor.ApiResponseFor400) | bad input parameter

#### get_a_professor.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Professor**](../../models/Professor.md) |  | 


#### get_a_professor.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_professors**
<a name="get_all_professors"></a>
> [Professor] get_all_professors()



Get all professors, in alphabetical order

### Example

```python
import planet_terp
from planet_terp.apis.tags import professors_api
from planet_terp.model.professor import Professor
from pprint import pprint
# Defining the host is optional and defaults to https://planetterp.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = planet_terp.Configuration(
    host = "https://planetterp.com/api/v1"
)

# Enter a context with an instance of the API client
with planet_terp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = professors_api.ProfessorsApi(api_client)

    # example passing only optional values
    query_params = {
        'type': "professor",
        'reviews': True,
        'limit': 1,
        'offset': 0,
    }
    try:
        api_response = api_instance.get_all_professors(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling ProfessorsApi->get_all_professors: %s\n" % e)
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
type | TypeSchema | | optional
reviews | ReviewsSchema | | optional
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["professor", "ta", ] 

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
200 | [ApiResponseFor200](#get_all_professors.ApiResponseFor200) | Returns professors matching query
400 | [ApiResponseFor400](#get_all_professors.ApiResponseFor400) | bad input parameter

#### get_all_professors.ApiResponseFor200
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
[**Professor**]({{complexTypePrefix}}Professor.md) | [**Professor**]({{complexTypePrefix}}Professor.md) | [**Professor**]({{complexTypePrefix}}Professor.md) |  | 

#### get_all_professors.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

