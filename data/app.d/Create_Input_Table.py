from deephaven import dtypes as dht
from deephaven import input_table

coldefs = {"Concept": dht.string}

book_search = input_table(col_defs = coldefs)

def get_response(concept):
    near_text = {"concepts": [concept]}
    return (client.query.get("Book", ["title", "description", "language"]).with_near_text(near_text).with_limit(1).do())

def get_title(response) -> str:
    return response["data"]["Get"]["Book"][0]["title"]

def get_description(response) -> str:
    return response["data"]["Get"]["Book"][0]["description"]

book_recommendations = book_search.update(["Response = get_response(Concept)", "Title = get_title(Response)", "Description = get_description(Response)"]).drop_columns("Response")