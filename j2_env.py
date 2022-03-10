from jinja2 import Environment, FileSystemLoader


def main():

    j2_env = Environment(loader=FileSystemLoader("/home/brad/network_automation_workshop/templates"))
    template = j2_env.get_template("interface.j2")
#    print(template.render(intf_num="1234", descr="Tacocat was here!!", ip_addr="1.1.1.1 255.255.255.0"))

    template_agrs = {
        "intf_num": "1234",
        "descr": "Tacocat was here!!",
        "ip_addr": "1.2.3.4/30"
    }

    print(template.render(**template_agrs))


if __name__ == "__main__":
    main()
