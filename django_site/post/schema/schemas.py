from copy import deepcopy

from drf_yasg.openapi import FORMAT_DATETIME as DATETIME
from drf_yasg.openapi import TYPE_ARRAY as ARR
from drf_yasg.openapi import TYPE_INTEGER as INT
from drf_yasg.openapi import TYPE_OBJECT as OBJ
from drf_yasg.openapi import TYPE_STRING as STR
from drf_yasg.openapi import Schema as S


def properties(schema, *names):
    return {name: schema.properties[name] for name in names}


def copy_schema(schema, **kwargs):
    schema = deepcopy(schema)
    schema.update(kwargs)
    return schema


post = S(title='Post', type=OBJ, properties={
    'id': S(type=INT),
    'user': S(type=INT),
    'created': S(type=STR, format=DATETIME),
    'updated': S(type=STR, format=DATETIME),
    'title': S(type=STR),
    'content': S(type=STR),
})

posts = S(type=ARR, items=post)

post_create = S(title='Post Create', type=OBJ, required=['title', 'content'], properties={
    'title': copy_schema(post.properties['title']),
    'content': copy_schema(post.properties['content']),
})

post_create_response = copy_schema(
    post_create,
    title=None,
    required=None,
)
