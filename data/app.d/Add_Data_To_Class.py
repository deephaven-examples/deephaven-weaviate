import weaviate

with client.batch(batch_size=80) as batch:
    for idx in range(80):
        book = dataset["train"][idx]
        properties = {"title": book["title"], "description": book["description"], "language": book["language"]}
        client.batch.add_data_object(properties, "Book")

print("Done uploading data to the Class.")
