# openapi_client.RatingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rating_get**](RatingApi.md#rating_get) | **GET** /rating | Returns current rating


# **rating_get**
> Rating rating_get()

Returns current rating

Returns current rating.

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
    api_instance = openapi_client.RatingApi(api_client)
    
    try:
        # Returns current rating
        api_response = api_instance.rating_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RatingApi->rating_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Rating**](Rating.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rating Sorted by DESC |  -  |
**405** | No users exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

