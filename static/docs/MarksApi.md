# openapi_client.MarksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marks_id_get**](MarksApi.md#marks_id_get) | **GET** /marks/{id} | return current student&#39;s marks.
[**marks_id_post**](MarksApi.md#marks_id_post) | **POST** /marks/{id} | Assign a new Discipline to the student


# **marks_id_get**
> list[OneOfstringintegermarks] marks_id_get(id)

return current student's marks.

return current student's marks

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarksApi(api_client)
    id = 56 # int | ID

    try:
        # return current student's marks.
        api_response = api_instance.marks_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MarksApi->marks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 

### Return type

[**list[OneOfstringintegermarks]**](OneOfstringintegermarks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return student&#39;s marks\&quot; |  -  |
**405** | Not found response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marks_id_post**
> marks_id_post(id, discipline=discipline)

Assign a new Discipline to the student

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MarksApi(api_client)
    id = 56 # int | ID
discipline = openapi_client.Discipline() # Discipline |  (optional)

    try:
        # Assign a new Discipline to the student
        api_instance.marks_id_post(id, discipline=discipline)
    except ApiException as e:
        print("Exception when calling MarksApi->marks_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 
 **discipline** | [**Discipline**](Discipline.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Simillar discipline already has been added |  -  |
**405** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

