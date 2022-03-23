import json
import httpx

def main():

    headers = {'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567'}
#    data = {'name': 'Netgear', 'slug': 'netgear'}
    
#    r = httpx.post('http://localhost:8000/api/dcim/manufacturers/', headers=headers, data=data)

#    print(r.headers, r.status_code)

    dict_man_1 = {'name': 'Arista', 'slug': 'arista'}
    dict_man_2 = {'name': 'Cisco', 'slug': 'cisco'}
    dict_man_3 = {'name': 'HP', 'slug': 'hp'}
    dict_man_4 = {'name': 'Aruba', 'slug': 'aruba'}
    dict_man_5 = {'name': 'Dell', 'slug': 'dell'}

    man_list = [dict_man_1, dict_man_2, dict_man_3, dict_man_4, dict_man_5]

    for item in man_list:
        r = httpx.post('http://localhost:8000/api/dcim/manufacturers/', headers=headers, data=item)
        print(item, r.status_code)

        # r.status_code = 201 = Successful
        # r.status_code = 400 = Failed

        if r.status_code == 201:
            _ = r.text
            man_dict = json.loads(_)

            print(man_dict["id"], man_dict["name"])
        else:
            print(f'{item} failed to be created')

if __name__ == "__main__":
    main()
