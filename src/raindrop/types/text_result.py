# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TextResult", "Source", "SourceBucket"]


class SourceBucket(BaseModel):
    application_name: Optional[str] = None

    application_version_id: Optional[str] = None

    bucket_name: Optional[str] = None

    module_id: Optional[str] = None


class Source(BaseModel):
    bucket: Optional[SourceBucket] = None
    """
    **DESCRIPTION** The bucket information containing this result **EXAMPLE**
    {"moduleId": "01jt3vs2nyt2xwk2f54x2bkn84", "bucketName": "mr-bucket"}
    """

    object: Optional[str] = None
    """**DESCRIPTION** The object key within the bucket **EXAMPLE** "document.pdf" """


class TextResult(BaseModel):
    chunk_signature: Optional[str] = None
    """**DESCRIPTION** Unique identifier for this text segment.

    Used for deduplication and result tracking **EXAMPLE**
    "51abb575a5e438a2db5fa064611995dfd76aa14d9e4b2a44c29a6374203126a5"
    """

    embed: Optional[str] = None
    """**DESCRIPTION** Vector representation for similarity matching.

    Used in semantic search operations **EXAMPLE** "base64_encoded_vector_data"
    """

    payload_signature: Optional[str] = None
    """**DESCRIPTION** Parent document identifier.

    Links related content chunks together **EXAMPLE**
    "e2ec3b118e205ff5d627e0c866224a25ba52e6d3ab758a3ef3d49e80908d7444"
    """

    score: Optional[float] = None
    """**DESCRIPTION** Relevance score (0.0 to 1.0).

    Higher scores indicate better matches **EXAMPLE** 0.95
    """

    source: Optional[Source] = None
    """**DESCRIPTION** Source document references.

    Contains bucket and object information **EXAMPLE** {"bucket": {"moduleId":
    "01jt3vs2nyt2xwk2f54x2bkn84", "bucketName": "mr-bucket"}, "object":
    "document.pdf"}
    """

    text: Optional[str] = None
    """**DESCRIPTION** The actual content of the result.

    May be a document excerpt or full content **EXAMPLE** "This is a sample text
    chunk from the document"
    """

    type: Optional[str] = None
    """**DESCRIPTION** Content MIME type.

    Helps with proper result rendering **EXAMPLE** "application/pdf"
    """
