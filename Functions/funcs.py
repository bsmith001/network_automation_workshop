

def connect(hostname,*, port, username="racecar", password):
    if hostname.count(".") == 3:
        print(f"Connecting to device {hostname}:{port}, as user {username}!")
        return True
    else:
        print(f"Invalid IP provided, cannot continue ...")
        return False

if __name__ == "__main__":
    result = connect(hostname="1.1.1.1", port="22", username="tacocat", password="racecare")
    print(f"result1: {result}")
    result = connect(hostname="2.2.2.2", port="22", password="potato")
    print(f"result2: {result}")



