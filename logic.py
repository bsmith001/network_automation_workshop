from jinja2 import Environment, FileSystemLoader


def main():

    j2_env = Environment(
        loader=FileSystemLoader("/home/brad/network_automation_workshop/templates")
    )
    template = j2_env.get_template("acl.j2")

    acl_lines = [
        "deny ip 0.0.0.0 0.255.255.255 any",
        "deny ip 10.0.0.0 0.255.255.255 any",
        "deny ip 100.64.0.0 0.63.255.255 any",
        "deny ip 127.0.0.0 0.255.255.255 any",
        "deny ip 169.254.0.0 0.0.255.255 any",
        "deny ip 172.16.0.0 0.15.255.255 any",
        "deny ip 192.0.0.0 0.0.0.255 any",
        "deny ip 192.0.2.0 0.0.0.255 any",
        "deny ip 198.18.0.0 0.2.255.255 any",
        "deny ip 198.51.100.0 0.0.0.255 any",
        "deny ip 203.0.113.0 0.0.0.255 any",
        "deny ip 224.0.0.0 15.255.255.255 any",
        "deny ip 240.0.0.0 15.255.255.255 any" 
    ]

    print(template.render(acl_lines=acl_lines))



if __name__ == "__main__":
    main()
