import typing_extensions

from planet_terp.paths import PathValues
from planet_terp.apis.paths.course import Course
from planet_terp.apis.paths.courses import Courses
from planet_terp.apis.paths.professor import Professor
from planet_terp.apis.paths.professors import Professors
from planet_terp.apis.paths.grades import Grades
from planet_terp.apis.paths.search import Search

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.COURSE: Course,
        PathValues.COURSES: Courses,
        PathValues.PROFESSOR: Professor,
        PathValues.PROFESSORS: Professors,
        PathValues.GRADES: Grades,
        PathValues.SEARCH: Search,
    }
)

path_to_api = PathToApi(
    {
        PathValues.COURSE: Course,
        PathValues.COURSES: Courses,
        PathValues.PROFESSOR: Professor,
        PathValues.PROFESSORS: Professors,
        PathValues.GRADES: Grades,
        PathValues.SEARCH: Search,
    }
)
