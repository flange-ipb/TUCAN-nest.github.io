from tucan.canonicalization import canonicalize_molecule
from tucan.serialization import serialize_molecule
from tucan.io import graph_from_molfile_text, graph_from_tucan, graph_to_molfile
from pyodide.ffi import to_js
import js

js.console.log("tucanweb.py is loading")


def serialize(m):
  return serialize_molecule(canonicalize_molecule(m))


# see https://pyodide.org/en/stable/usage/type-conversions.html#calling-python-objects-from-javascript
def molfile_to_tucan(molfile):
  result = ""
  if molfile:
    graph = graph_from_molfile_text(molfile)
    if list(graph.nodes):
      result = serialize(graph)

  return to_js(result)


def tucan_to_molfile(tucan, calc_coordinates):
  molfile = ""
  canonical_tucan = ""

  if tucan:
    graph = graph_from_tucan(tucan)
    molfile = graph_to_molfile(graph, calc_coordinates)
    canonical_tucan = serialize(graph)

  return to_js((molfile, canonical_tucan))


molfile_to_tucan, tucan_to_molfile