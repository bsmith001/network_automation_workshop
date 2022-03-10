from jinja2 import Environment, FileSystemLoader, Template


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

    inline_template = Template("Hai fren, I'm {{ person }}, how you doin!?")
    print(inline_template.render(person="tacocat"))

    interfaces = [
        {"intf_num": "1", "ip_addr": "1.1.1.1/30", "descr": "tacocat was here again!"},
        {"intf_num": "2", "ip_addr": "2.2.2.2/30", "descr": "racecar potato"},
        {"intf_num": "3", "ip_addr": "3.3.3.3/30", "descr": "is it lunch yet??"},
        {"intf_num": "4", "ip_addr": "4.4.4.4/30", "descr": "zzzzzzzzzz"},
    ]

    interface_configs = []
    for interface in interfaces:
        interface_configs.append(template.render(**interface))
 #       print(template.render(**interface)) 

    print("!\n".join(interface_configs))


if __name__ == "__main__":
    main()
