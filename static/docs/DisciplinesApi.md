# openapi_client.DisciplinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disciplines_id_get**](DisciplinesApi.md#disciplines_id_get) | **GET** /disciplines/{id} | 
[**disciplines_id_post**](DisciplinesApi.md#disciplines_id_post) | **POST** /disciplines/{id} | New Discipline.
[**disciplines_id_put**](DisciplinesApi.md#disciplines_id_put) | **PUT** /disciplines/{id} | update discipline.


# **disciplines_id_get**
> Discipline disciplines_id_get(id)



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
    api_instance = openapi_client.DisciplinesApi(api_client)
    id = 56 # int | ID

    try:
        api_response = api_instance.disciplines_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DisciplinesApi->disciplines_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 

### Return type

[**Discipline**](Discipline.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a JSON of Discipline |  -  |
**405** | No discipline found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disciplines_id_post**
> object disciplines_id_post(id, discipline=discipline)

New Discipline.

Creation page.

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
    api_instance = openapi_client.DisciplinesApi(api_client)
    id = 56 # int | ID
discipline = openapi_client.Discipline() # Discipline |  (optional)

    try:
        # New Discipline.
        api_response = api_instance.disciplines_id_post(id, discipline=discipline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DisciplinesApi->disciplines_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 
 **discipline** | [**Discipline**](Discipline.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nice, we&#39;ve created a new Discipline |  -  |
**405** | Error. You might wanna recheck the fields you gave us, some error till creation uccured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disciplines_id_put**
> disciplines_id_put(id, discipline=discipline)

update discipline.

update discipline by json

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
    api_instance = openapi_client.DisciplinesApi(api_client)
    id = 56 # int | ID
discipline = openapi_client.Discipline() # Discipline |  (optional)

    try:
        # update discipline.
        api_instance.disciplines_id_put(id, discipline=discipline)
    except ApiException as e:
        print("Exception when calling DisciplinesApi->disciplines_id_put: %s\n" % e)
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
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update sucssesful |  -  |
**405** | Internal Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

