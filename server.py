from ariadne import (
    gql,
    make_executable_schema,
    QueryType,
    MutationType,
    ObjectType
)

from ariadne.asgi import GraphQL
from fastapi import FastAPI
from mysql.connector import pooling

dbconfig = {
  "database": "Todo",
  "user":     "root",
  "password": "example"
}

cnxpool = pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 3,
                                                      **dbconfig)
                                                      
type_defs = gql("""
    type Query{
        test: String
    }

    type Mutation{
        setTask(task: TaskInput!): Task!
    }

    input TaskInput{
        title: String!
        description: String!
    }

    type Task{
        id: Int!
        title: String!
        description: String!
        timestamp: String!
    }
""")

#region Query
query = QueryType()
@query.field("test")
def resolve_test(obj,info):
    return "hello julia"
#end region

#region Mutation
mutation = MutationType()
@mutation.field("setTask")
def resolve_set_task(obj,info,task):
    return task
#end region

#region Task
task = ObjectType()
@task.field("id")
def resolve_task_task(obj,info):
    return obj["id"]
@task.field("title")
def resolve_task_task(obj,info):
    return obj["title"]
@task.field("description")
def resolve_task_task(obj,info):
    return obj["description"]
@task.field("timestamp")
def resolve_task_task(obj,info):
    return obj["timestamp"]
#end region 

schema = make_executable_schema(type_defs, query, mutation, task)

graph_app = GraphQL(schema)

app = FastAPI()

app.mount("/", graph_app)
