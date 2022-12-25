<a name="__pageTop"></a>
# planet_terp.apis.tags.search_api.SearchApi

All URIs are relative to *https://planetterp.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](#search) | **get** /search | 

# **search**
<a name="search"></a>
> [SearchResult] search(query)



Search both professors and courses with a query string. This will match professors and courses which have the query string as a substring of their name.

### Example

```python
import planet_terp
from planet_terp.apis.tags import search_api
from planet_terp.model.search_result import SearchResult
from pprint import pprint
# Defining the host is optional and defaults to https://planetterp.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = planet_terp.Configuration(
    host = "https://planetterp.com/api/v1"
)

# Enter a context with an instance of the API client
with planet_terp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "CMSC13",
    }
    try:
        api_response = api_instance.search(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)

    # example passing only optional values
    query_params = {
        'query': "CMSC13",
        'limit': 1,
        'offset': 0,
    }
    try:
        api_response = api_instance.search(
            query_params=query_params,
        )
        pprint(api_response)
    except planet_terp.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)
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
query | QuerySchema | | 
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 30

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search.ApiResponseFor200) | Returns professors and courses matching the query
400 | [ApiResponseFor400](#search.ApiResponseFor400) | bad input parameter

#### search.ApiResponseFor200
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
[**SearchResult**]({{complexTypePrefix}}SearchResult.md) | [**SearchResult**]({{complexTypePrefix}}SearchResult.md) | [**SearchResult**]({{complexTypePrefix}}SearchResult.md) |  | 

#### search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

