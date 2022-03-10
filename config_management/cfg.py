from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg


def main():

    dev = {
        "host": "spine1",
        "auth_strict_key": False,
        "auth_username": "admin",
        "auth_password": "admin",
        "platform": "arista_eos"
    }

    conn = Scrapli(**dev)
    conn.open()

    cfg_conn = ScrapliCfg(conn=conn)

    print(type(cfg_conn), dir(cfg_conn))

    cfg_conn.prepare()

    get_result = cfg_conn.get_config()
    print(type(get_result), dir(get_result))


if __name__ == "__main__":
    main()
