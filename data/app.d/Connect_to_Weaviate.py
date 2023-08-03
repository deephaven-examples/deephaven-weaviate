import weaviate
import os

weaviate_endpoint = os.environ["WEAVIATE_ENDPOINT"]
weaviate_token = os.environ["WEAVIATE_TOKEN"]
huggingface_token = os.environ["HUGGINGFACE_TOKEN"]

client = weaviate.Client(url=weaviate_endpoint, auth_client_secret=weaviate.AuthApiKey(api_key=weaviate_token), additional_headers={"X-HuggingFace-Api-Key": huggingface_token})
