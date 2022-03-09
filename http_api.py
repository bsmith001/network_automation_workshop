import json

import httpx


def main():
    nxapi_payload = """
{
   "ins_api": {
     "version": "1.0",
     "type": "cli_show",
     "chunk": "0",
     "sid": "1",
     "input": "show version",
     "output_format": "json"
  }
}"""

    nxapi_payload_dict = json.loads(nxapi_payload)
    print(nxapi_payload_dict)

    reponse = httpx.post("https://leaf3/ins", json=nxapi_payload_dict, auth=("admin", "admin"), verify=False)
    print(reponse)



if __name__ == "__main__":
    main()
