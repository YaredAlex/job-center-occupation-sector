import requests
import json
import pandas as pd
HASURA_URL = "https://job-center-api.staging.lmis.gov.et/v1/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "x-hasura-admin-secret": "3LcJH8gT4sZkYVnfpqkDwY130m4S2G"
}

POSITIONS_QUERY = """
query GetPositions {
  base_positions(limit: 10) {
    id
    namejson
  }
}
"""

SUBSECTOR_QUERY = """query GetSubSectors {
  base_sub_sectors {
    id
    namejson
    sector {
      id
      namejson
    }
  }
}"""

def run_query(query, variables=None):
    response = requests.post(
        HASURA_URL,
        headers=HEADERS,
        json={"query": query, "variables": variables},
    )
    content = response.json()
    print("="*50)
    print(content)

run_query(SUBSECTOR_QUERY)


