# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from planet_terp.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    COURSES = "Courses"
    PROFESSORS = "Professors"
    GRADES = "Grades"
    SEARCH = "Search"
