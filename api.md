# DocumentQuery

Types:

```python
from raindrop.types import BucketLocator, DocumentQueryCreateResponse
```

Methods:

- <code title="post /v1/document_query">client.document_query.<a href="./src/raindrop/resources/document_query.py">create</a>(\*\*<a href="src/raindrop/types/document_query_create_params.py">params</a>) -> <a href="./src/raindrop/types/document_query_create_response.py">DocumentQueryCreateResponse</a></code>

# ChunkSearch

Types:

```python
from raindrop.types import TextResult, ChunkSearchExecuteResponse
```

Methods:

- <code title="post /v1/chunk_search">client.chunk_search.<a href="./src/raindrop/resources/chunk_search.py">execute</a>(\*\*<a href="src/raindrop/types/chunk_search_execute_params.py">params</a>) -> <a href="./src/raindrop/types/chunk_search_execute_response.py">ChunkSearchExecuteResponse</a></code>

# SummarizePage

Types:

```python
from raindrop.types import SummarizePageCreateSummaryResponse
```

Methods:

- <code title="post /v1/summarize_page">client.summarize_page.<a href="./src/raindrop/resources/summarize_page.py">create_summary</a>(\*\*<a href="src/raindrop/types/summarize_page_create_summary_params.py">params</a>) -> <a href="./src/raindrop/types/summarize_page_create_summary_response.py">SummarizePageCreateSummaryResponse</a></code>

# Search

Types:

```python
from raindrop.types import SearchRunResponse
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/raindrop/resources/search.py">run</a>(\*\*<a href="src/raindrop/types/search_run_params.py">params</a>) -> <a href="./src/raindrop/types/search_run_response.py">SearchRunResponse</a></code>

# Object

Types:

```python
from raindrop.types import (
    BucketResponse,
    ObjectListObjectsResponse,
    ObjectPutObjectResponse,
    ObjectRetrieveObjectResponse,
)
```

Methods:

- <code title="get /v1/object/{bucket_name}">client.object.<a href="./src/raindrop/resources/object.py">list_objects</a>(bucket_name, \*\*<a href="src/raindrop/types/object_list_objects_params.py">params</a>) -> <a href="./src/raindrop/types/object_list_objects_response.py">ObjectListObjectsResponse</a></code>
- <code title="post /v1/object/{bucket_name}/{object_key}">client.object.<a href="./src/raindrop/resources/object.py">put_object</a>(object_key, \*, bucket_name, \*\*<a href="src/raindrop/types/object_put_object_params.py">params</a>) -> <a href="./src/raindrop/types/object_put_object_response.py">ObjectPutObjectResponse</a></code>
- <code title="get /v1/object/{bucket_name}/{object_key}">client.object.<a href="./src/raindrop/resources/object.py">retrieve_object</a>(object_key, \*, bucket_name, \*\*<a href="src/raindrop/types/object_retrieve_object_params.py">params</a>) -> <a href="./src/raindrop/types/object_retrieve_object_response.py">ObjectRetrieveObjectResponse</a></code>
