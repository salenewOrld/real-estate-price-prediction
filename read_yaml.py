import yaml

if __name__ == '__main__':
    with open('/usr/src/volume/volume/configs/experiment_regressor.yaml', 'r') as yaml_file:
        file = yaml.load(yaml_file, Loader=yaml.FullLoader)
        
    print(type(file['y']))
          