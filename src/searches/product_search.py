from elasticsearch_dsl import FacetedSearch, TermsFacet
from models import Product


class ProductSearch(FacetedSearch):
    index = "products"
    doc_types = [Product, ]
    fields = ['title', 'description', 'tags']

    facets = {
        'tags': TermsFacet(field='tags'),
    }


# when using:
# ProductSearch(filters={"title": "a"})
