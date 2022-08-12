from ariadne import (
    gql,
    make_executable_schema,
    QueryType
)

from ariadne.asgi import GraphQL
from fastapi import FastAPI
type_defs = gql("""
    type Query{
        test: String
    }
""")

query = QueryType()
@query.field("test")
def resolve_test(obj,info):
    return "hello julia"

schema = make_executable_schema(type_defs, query)

graph_app = GraphQL(schema)

app = FastAPI()

app.mount("/", graph_app)
