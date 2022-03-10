from jinja2 import Environment, FileSystemLoader


def main():

    j2_env = Environment(loader=FileSystemLoader("/home/brad/network_automation_workshop/templates"))
 #   template = j2_env.get_template("interface.j2")
 #   print(template.render())
    print(dir(j2_env))



if __name__ == "__main__":
    main()
