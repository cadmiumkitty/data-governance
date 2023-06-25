import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, SKOS, DCTERMS

namespace_manager = NamespaceManager(Graph())
namespace_manager.bind('skos', SKOS, override = True)
namespace_manager.bind('dcterms', DCTERMS, override = True)
namespace_manager.bind('dg', Namespace('https://dalstonsemantics.com/dg/'), override = True)
namespace_manager.bind('pav', Namespace('http://purl.org/pav/'), override = True)

schema_df = pd.read_csv('data-governance-rdfs-schema.csv', index_col = '@id', keep_default_na = True)
schema = rdfpandas.to_graph(schema_df, namespace_manager)

concept_scheme_df = pd.read_csv('data-governance-skos-concept-scheme.csv', index_col = '@id', keep_default_na = True)
concept_scheme = rdfpandas.to_graph(concept_scheme_df, namespace_manager)

g = Graph()
g = schema + concept_scheme

ttl = g.serialize(format = 'turtle')
with open('data-governance.ttl', 'w') as file:
   file.write(ttl)
