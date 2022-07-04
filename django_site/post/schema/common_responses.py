from drf_yasg.openapi import TYPE_OBJECT as OBJ
from drf_yasg.openapi import TYPE_STRING as STR
from drf_yasg.openapi import Schema as S

response204 = ''

response401 = S(type=OBJ, properties={
    'detail': S(type=STR),
})

response404 = S(type=OBJ, properties={
    'detail': S(type=STR),
})
