# Import libraries
from xml.dom import minidom
from datetime import datetime

# Record start time
start_time = datetime.now()

# Load XML file
xmldoc = minidom.parse("go_obo.xml")

# Get all term elements
terms = xmldoc.getElementsByTagName("term")

# Store results for each ontology
results = {
    "molecular_function": ("", 0),
    "biological_process": ("", 0),
    "cellular_component": ("", 0)
}

# get term names
for term in terms:
    name_nodes = term.getElementsByTagName("name")

    if len(name_nodes) > 0 and name_nodes[0].firstChild:
        term_name = name_nodes[0].firstChild.data
    else:
        term_name = "Unknown"

    # Get namespace
    namespace_nodes = term.getElementsByTagName("namespace")

    if len(namespace_nodes) > 0 and namespace_nodes[0].firstChild:
        namespace = namespace_nodes[0].firstChild.data #data：extract the content of the node
    else:
        continue

    is_a_count = len(term.getElementsByTagName("is_a"))

    # -----------------------------
    # Update maximum value
    # -----------------------------
    current_max = results[namespace][1]

    if is_a_count > current_max:
        results[namespace] = (term_name, is_a_count)

# Record end time
end_time = datetime.now()

# Calculate execution time
execution_time = end_time - start_time

#print results
for ontology in results:
    term_name = results[ontology][0]
    count = results[ontology][1]

    print("Ontology:", ontology)
    print("GO term with most <is_a> elements:", term_name)
    print("Number of <is_a> elements:", count)
    print()

print("DOM execution time:", execution_time)

#this file has no attrivute so we don't need to use atri