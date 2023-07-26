# Deephaven + Weaviate for real-time semantic search

This repository combines Deephaven with Weaviate to show a simple example of a combination that could be used to power a real-time semantic search engine. It uploads 80 books with descriptions and language from the [Skelebor/book_titles_and_descriptions](https://huggingface.co/datasets/Skelebor/book_titles_and_descriptions) dataset. The dataset itself contains nearly 2 million books. However, this tool uses Weaviate's free tier, which is rate-limited at 100 items/hour. Thus, 80 is chosen to allow some room to perform searches on the data. The books are added to a `Book` class (which is created if it doesn't exist). From there, the Deephaven instance creates an input table called `book_genres`. Add data to this table by double clicking on cells and typing search terms. Click commit to automatically trigger the `book_recommandations` table to update with the top result (both book title and description) returned from Weaviate's vector search engine.

## About this project 

Deephaven is a real-time, column-oriented database query engine that excels with real-time and big data.
Weaviate is an open-source vector database.

Combining the two provides a powerful infrastructure that could be the backend for semantic search engines, recommendation engines, and much more. The framework provided by this application can be built upon in many ways - with a frontend UI, more vectors to search, etc.

## Requirements

This uses Deephaven run from Docker. For installation instructions and prerequisites, see [here](https://deephaven.io/core/docs/tutorials/quickstart/).

For Weaviate's installation instructions, see [here](https://weaviate.io/developers/weaviate/client-libraries/python).

## Usage

This application uses Deephaven's [application mode](https://deephaven.io/core/docs/reference/app-mode/application-mode-config/) to perform configuration on startup. It requires the following environment variables to be set:

- `DH_PSK`: The Deephaven pre-shared key. If this isn't set, the pre-shared key will either be an empty string, or a randomly generated sequence of characters. If the latter, see [How to configure and use pre-shared key authentication](https://deephaven.io/core/docs/how-to-guides/authentication/auth-psk/).
- `WEAVIATE_ENDPOINT`: Your Weaviate cluster endpoint. If this isn't set properly, you will not be able to upload data to Weaviate, or perform semantic search.
- `WEAVIATE_TOKEN`: Your Weaviate authentication token. If this isn't set properly, you will not be able to connect to your Weaviate cluster.
- `HUGGINGFACE_TOKEN`: Your Hugging Face token. If this isn't set properly, you will not be able to use its vectorization engines to vectorize text data, resulting the inability to perform semantic search.

To see the scripts that run upon startup, see [here](./data/app.d/app.app).

To start the application, perform:

```bash
docker compose up --build
```

The first time you start the application, it can take a few minutes, since it has to download the entire dataset. Wait for the Docker logs to display `Server started on port 10000`, then connect to `http://localhost:10000/ide` in your preferred web browser. The Deephaven IDE should appear with a default layout showing the tables `book_genres` and `book_recommendations` on the bottom half. If it doesn't, you can bring them up via the `Panels` dropdown menu at the top right of the screen, or by importing the layout file found in `data/storage/layouts` via the same dropdown.

If you start this application more than once per hour, you will likely notice the following message appear numerous times on subsequent launches:

```
{'error': [{'message': 'update vector: failed with status: 429 error: Rate limit reached. You reached free usage limit (reset hourly). Please subscribe to a plan at https://huggingface.co/pricing to use the API at this rate'}]}
```

This, by itself, is fine, but subsequent entries to the `book_genres` table will cause the application to crash. Exceeding the rate limit by attempting to perform a search causes an error, which ends the Python process, and subsequently the JVM, and Deephaven.

## Terms of use

See the [license](./LICENSE.md), Deephaven's [code of conduct](https://github.com/deephaven/deephaven-core/blob/main/CODE_OF_CONDUCT.md), and Weaviate's [code of conduct](https://github.com/weaviate/weaviate/blob/master/CODE_OF_CONDUCT.md) for usage guidelines.
