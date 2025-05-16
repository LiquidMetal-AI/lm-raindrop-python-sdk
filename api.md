# Search

Types:

```python
from lm_raindrop.types import SearchFindResponse
```

Methods:

- <code title="post /v1/search">client.search.<a href="./src/lm_raindrop/resources/search.py">find</a>(\*\*<a href="src/lm_raindrop/types/search_find_params.py">params</a>) -> <a href="./src/lm_raindrop/types/search_find_response.py">SearchFindResponse</a></code>

# DocumentQuery

Types:

```python
from lm_raindrop.types import DocumentQueryAskResponse
```

Methods:

- <code title="post /v1/document_query">client.document_query.<a href="./src/lm_raindrop/resources/document_query.py">ask</a>(\*\*<a href="src/lm_raindrop/types/document_query_ask_params.py">params</a>) -> <a href="./src/lm_raindrop/types/document_query_ask_response.py">DocumentQueryAskResponse</a></code>

# ChunkSearch

Types:

```python
from lm_raindrop.types import ChunkSearchFindResponse
```

Methods:

- <code title="post /v1/chunk_search">client.chunk_search.<a href="./src/lm_raindrop/resources/chunk_search.py">find</a>(\*\*<a href="src/lm_raindrop/types/chunk_search_find_params.py">params</a>) -> <a href="./src/lm_raindrop/types/chunk_search_find_response.py">ChunkSearchFindResponse</a></code>

# SummarizePage

Types:

```python
from lm_raindrop.types import SummarizePageCreateResponse
```

Methods:

- <code title="post /v1/summarize_page">client.summarize_page.<a href="./src/lm_raindrop/resources/summarize_page.py">create</a>(\*\*<a href="src/lm_raindrop/types/summarize_page_create_params.py">params</a>) -> <a href="./src/lm_raindrop/types/summarize_page_create_response.py">SummarizePageCreateResponse</a></code>

# Object

Types:

```python
from lm_raindrop.types import (
    ObjectListObjectsResponse,
    ObjectPutObjectResponse,
    ObjectRetrieveObjectResponse,
)
```

Methods:

- <code title="get /v1/object/{bucket_name}">client.object.<a href="./src/lm_raindrop/resources/object.py">list_objects</a>(bucket_name, \*\*<a href="src/lm_raindrop/types/object_list_objects_params.py">params</a>) -> <a href="./src/lm_raindrop/types/object_list_objects_response.py">ObjectListObjectsResponse</a></code>
- <code title="post /v1/object/{bucket_name}/{object_key}">client.object.<a href="./src/lm_raindrop/resources/object.py">put_object</a>(object_key, \*, bucket_name, \*\*<a href="src/lm_raindrop/types/object_put_object_params.py">params</a>) -> <a href="./src/lm_raindrop/types/object_put_object_response.py">ObjectPutObjectResponse</a></code>
- <code title="get /v1/object/{bucket_name}/{object_key}">client.object.<a href="./src/lm_raindrop/resources/object.py">retrieve_object</a>(object_key, \*, bucket_name, \*\*<a href="src/lm_raindrop/types/object_retrieve_object_params.py">params</a>) -> <a href="./src/lm_raindrop/types/object_retrieve_object_response.py">ObjectRetrieveObjectResponse</a></code>
