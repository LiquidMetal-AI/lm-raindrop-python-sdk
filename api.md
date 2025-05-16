# Object

Types:

```python
from raindrop.types import (
    BucketResponse,
    ObjectRetrieveResponse,
    ObjectListResponse,
    ObjectUploadResponse,
)
```

Methods:

- <code title="get /v1/object/{bucket_name}/{object_key}">client.object.<a href="./src/raindrop/resources/object.py">retrieve</a>(object_key, \*, bucket_name, \*\*<a href="src/raindrop/types/object_retrieve_params.py">params</a>) -> <a href="./src/raindrop/types/object_retrieve_response.py">ObjectRetrieveResponse</a></code>
- <code title="get /v1/object/{bucket_name}">client.object.<a href="./src/raindrop/resources/object.py">list</a>(bucket_name, \*\*<a href="src/raindrop/types/object_list_params.py">params</a>) -> <a href="./src/raindrop/types/object_list_response.py">ObjectListResponse</a></code>
- <code title="post /v1/object/{bucket_name}/{object_key}">client.object.<a href="./src/raindrop/resources/object.py">upload</a>(object_key, \*, bucket_name, \*\*<a href="src/raindrop/types/object_upload_params.py">params</a>) -> <a href="./src/raindrop/types/object_upload_response.py">ObjectUploadResponse</a></code>
