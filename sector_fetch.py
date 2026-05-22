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
    sub_sectors_id = []
    sectors_id = []
    sectors = set() 
    sub_sectors = content['data']['base_sub_sectors']
    for sub_sector in sub_sectors:
        sub_sectors_id.append({
            "name":sub_sector['namejson']['en'],
            "id":sub_sector['id']
        })
        sector,sector_id = sub_sector['sector']['namejson']['en'],sub_sector['sector']['id'] 
        if sector not in sectors:
          sectors_id.append({
              "name":sector,
              "id":sector_id
          })
          sectors.add(sector)
    #save to json file
    file_name = "sector_sub_sector_ids.json"
    with open(file_name,'w') as file:
       json.dump({
          "sub_sectors":sub_sectors_id,
          "sectors":sectors_id
       },file)
    print("="*50)
    print(f"{file_name} saved success!")
        

run_query(SUBSECTOR_QUERY)


