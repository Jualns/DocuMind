import enum
import json

class Visibility(str, enum.Enum):
    public = "public"
    internal = "internal"


class Category(str, enum.Enum):
    manual = "manual"
    reference = "reference"
    policy = "policy"
    faq = "faq"
    tutorial = "tutorial"
    announcement = "announcement"
    security = "security"

class Document:
    id: int
    title: str
    category: Category
    content: str
    visibility: Visibility

    def __init__(self, id: int, title: str, category: Category, content: str, visibility: Visibility):
        self.id = id
        self.title = title
        self.category = category
        self.content = content
        self.visibility = visibility

documents: list[Document] = []

def read_seed_data():
    with open("docs/seed_documents.json", "r") as f:
        data = json.load(f)
        for doc in data:
            documents.append(Document(**doc))



def register_document(document: Document):
    documents.append(document)



def list_documents():
    return documents