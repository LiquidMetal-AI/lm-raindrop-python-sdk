# Search

Types:

```python
from raindrop.types import SearchResponse, TextResult
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/raindrop/resources/search.py">create</a>(\*\*<a href="src/raindrop/types/search_create_params.py">params</a>) -> <a href="./src/raindrop/types/search_response.py">SearchResponse</a></code>
- <code title="get /v1/search">client.search.<a href="./src/raindrop/resources/search.py">retrieve</a>(\*\*<a href="src/raindrop/types/search_retrieve_params.py">params</a>) -> <a href="./src/raindrop/types/search_response.py">SearchResponse</a></code>

# DocumentQuery

Types:

```python
from raindrop.types import DocumentQueryAskResponse
```

Methods:

- <code title="post /v1/document_query">client.document_query.<a href="./src/raindrop/resources/document_query.py">ask</a>(\*\*<a href="src/raindrop/types/document_query_ask_params.py">params</a>) -> <a href="./src/raindrop/types/document_query_ask_response.py">DocumentQueryAskResponse</a></code>

# ChunkSearch

Types:

```python
from raindrop.types import ChunkSearchExecuteResponse
```

Methods:

- <code title="post /v1/chunk_search">client.chunk_search.<a href="./src/raindrop/resources/chunk_search.py">execute</a>(\*\*<a href="src/raindrop/types/chunk_search_execute_params.py">params</a>) -> <a href="./src/raindrop/types/chunk_search_execute_response.py">ChunkSearchExecuteResponse</a></code>

# SummarizePage

Types:

```python
from raindrop.types import SummarizePageCreateResponse
```

Methods:

- <code title="post /v1/summarize_page">client.summarize_page.<a href="./src/raindrop/resources/summarize_page.py">create</a>(\*\*<a href="src/raindrop/types/summarize_page_create_params.py">params</a>) -> <a href="./src/raindrop/types/summarize_page_create_response.py">SummarizePageCreateResponse</a></code>

# Object

Types:

```python
from raindrop.types import ObjectListResponse, ObjectDeleteResponse, ObjectUploadResponse
```

Methods:

- <code title="get /v1/object/{bucket}">client.object.<a href="./src/raindrop/resources/object.py">list</a>(bucket) -> <a href="./src/raindrop/types/object_list_response.py">ObjectListResponse</a></code>
- <code title="delete /v1/object/{bucket}/{key}">client.object.<a href="./src/raindrop/resources/object.py">delete</a>(key, \*, bucket) -> <a href="./src/raindrop/types/object_delete_response.py">ObjectDeleteResponse</a></code>
- <code title="get /v1/object/{bucket}/{key}">client.object.<a href="./src/raindrop/resources/object.py">download</a>(key, \*, bucket) -> BinaryAPIResponse</code>
- <code title="put /v1/object/{bucket}/{key}">client.object.<a href="./src/raindrop/resources/object.py">upload</a>(key, \*, bucket, \*\*<a href="src/raindrop/types/object_upload_params.py">params</a>) -> <a href="./src/raindrop/types/object_upload_response.py">ObjectUploadResponse</a></code>
