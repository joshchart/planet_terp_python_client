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