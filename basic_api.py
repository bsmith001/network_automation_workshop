import httpx


def main():

    r = httpx.get('http://brad-netbox.workshop/')
    print(r, type(r), dir(r))

    print(r.text)

    print(r.headers, r.status_code, r.elapsed)

    r = httpx.get("http://brad-netbox.workshop/api/dcim/devices", headers={"Authorization": "Token a546e15a088bc072150c67d65ed0bf7b3fad803c"})
    print(f"Fetching dcim/devices response: {r}")
    print(r.text)
    print(r.json())


if __name__ == "__main__":
    main()
