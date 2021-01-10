import yaml

def get_yaml(yaml_file="test_data.yml"):
    with open(yaml_file,'r',encoding='utf-8') as fp:
        f = fp.read() #读出来是字符串
        # print(type(f))
    d = yaml.load(f)
    print(d)
    return d

if __name__ == '__main__':
    yaml_file = "test_data.yml"
    get_yaml(yaml_file)