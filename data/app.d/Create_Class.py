import weaviate

try:
    myclass = {"class": "Book", "vectorizer": "text2vec-huggingface", "moduleConfig": {"text2vec-huggingface": {"model": "sentence-transformers/all-MiniLM-L6-v2", "options": {"waitForModel": True}}}}
    client.schema.create_class(myclass)

except weaviate.exceptions.UnexpectedStatusCodeException:
    print("Class already exists.")


