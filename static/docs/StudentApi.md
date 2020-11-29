# openapi_client.StudentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**student_id_get**](StudentApi.md#student_id_get) | **GET** /student/{id} | 
[**student_id_post**](StudentApi.md#student_id_post) | **POST** /student/{id} | New Student.
[**student_id_put**](StudentApi.md#student_id_put) | **PUT** /student/{id} | Update student.


# **student_id_get**
> Student student_id_get(id)



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
    api_instance = openapi_client.StudentApi(api_client)
    id = 56 # int | ID

    try:
        api_response = api_instance.student_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudentApi->student_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 

### Return type

[**Student**](Student.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a JSON of user |  -  |
**405** | No user found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **student_id_post**
> object student_id_post(id, student=student)

New Student.

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
    api_instance = openapi_client.StudentApi(api_client)
    id = 56 # int | ID
student = openapi_client.Student() # Student |  (optional)

    try:
        # New Student.
        api_response = api_instance.student_id_post(id, student=student)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudentApi->student_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 
 **student** | [**Student**](Student.md)|  | [optional] 

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
**200** | Nice, we&#39;ve created a new Student |  -  |
**405** | Error. You might wanna recheck the fields you gave us, some error till creation uccured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **student_id_put**
> student_id_put(id, student=student)

Update student.

update user by json

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
    api_instance = openapi_client.StudentApi(api_client)
    id = 56 # int | ID
student = openapi_client.Student() # Student |  (optional)

    try:
        # Update student.
        api_instance.student_id_put(id, student=student)
    except ApiException as e:
        print("Exception when calling StudentApi->student_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 
 **student** | [**Student**](Student.md)|  | [optional] 

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

