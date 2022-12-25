import typing_extensions

from planet_terp.apis.tags import TagValues
from planet_terp.apis.tags.courses_api import CoursesApi
from planet_terp.apis.tags.professors_api import ProfessorsApi
from planet_terp.apis.tags.grades_api import GradesApi
from planet_terp.apis.tags.search_api import SearchApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COURSES: CoursesApi,
        TagValues.PROFESSORS: ProfessorsApi,
        TagValues.GRADES: GradesApi,
        TagValues.SEARCH: SearchApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COURSES: CoursesApi,
        TagValues.PROFESSORS: ProfessorsApi,
        TagValues.GRADES: GradesApi,
        TagValues.SEARCH: SearchApi,
    }
)
