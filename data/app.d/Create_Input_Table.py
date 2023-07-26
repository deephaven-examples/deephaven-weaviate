from deephaven import dtypes as dht
from deephaven import input_table

response = None

coldefs = {"Concept": dht.string}

book_genres = input_table(col_defs = coldefs)

def get_title(concept) -> str:
    global response
    near_text = {"concepts": [concept]}
    response = (client.query.get("Book", ["title", "description", "language"]).with_near_text(near_text).with_limit(1).do())
    return response["data"]["Get"]["Book"][0]["title"]

def get_description() -> str:
    global response
    return response["data"]["Get"]["Book"][0]["description"]

book_recommendations = book_genres.update(["Title = get_title(Concept)", "Description = get_description()"])
