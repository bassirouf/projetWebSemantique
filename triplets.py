import rdflib
from rdflib.namespace import RDF, RDFS, FOAF, XSD

# Créer un nouveau graphe RDF
g = rdflib.Graph()

# Définir les préfixes
ex = rdflib.Namespace("http://example.org/")
dbo = rdflib.Namespace("http://dbpedia.org/ontology/")
foaf = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
xsd = rdflib.Namespace("http://www.w3.org/2001/XMLSchema#")

# Ajouter des triplets RDF
g.add((rdflib.URIRef("http://example.org/Inception"), RDF.type, dbo.Film))
g.add((rdflib.URIRef("http://example.org/Inception"), foaf.name, rdflib.Literal("Inception")))
g.add((rdflib.URIRef("http://example.org/Inception"), dbo.director, rdflib.URIRef("http://example.org/Christopher_Nolan")))
g.add((rdflib.URIRef("http://example.org/Inception"), dbo.starring, rdflib.URIRef("http://example.org/Leonardo_DiCaprio")))
g.add((rdflib.URIRef("http://example.org/Inception"), dbo.genre, rdflib.URIRef("http://example.org/Action_film")))
g.add((rdflib.URIRef("http://example.org/Inception"), dbo.abstract, rdflib.Literal("A thief who enters the dreams of others to steal secrets from their subconscious.")))
g.add((rdflib.URIRef("http://example.org/Inception"), dbo.releaseDate, rdflib.Literal("2010-07-16", datatype=XSD.date)))
g.add((rdflib.URIRef("http://example.org/Inception"), dbo.runtime, rdflib.Literal("148", datatype=XSD.int)))

# Sauvegarder le graphe RDF dans un fichier
g.serialize(destination="films_with_users.rdf", format="turtle")

# Afficher les triplets ajoutés
for subj, pred, obj in g:
    print(subj, pred, obj)
