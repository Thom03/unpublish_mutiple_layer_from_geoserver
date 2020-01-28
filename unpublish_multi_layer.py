from geoserver.catalog import Catalog

"""To Establish connection to the catalog"""
conn = Catalog("http://localhost:8080/geoserver/rest", username="admin", password="geoserver")

print(conn)

# all_layers = conn.get_layers()
