print("+ = "+__name__)
import json

class Load:
    def __init__(self):
        self.file_name = "config/data.json"
        self.info = {'save': 'False', 'name': '', 'password': '',
                     'resolution': [1200, 800],
                     'camera': 'True', 'ip': 'localhost'}
        self.data = self.load()
        self.check = self.issaved()

    def load(self):
        try:
            with open(self.file_name, 'r') as fp:
                return json.load(fp)
        except IOError:
            with open(self.file_name, 'w') as fp:
                json.dump(self.info, fp, indent=4)
            try:
                with open(self.file_name, 'r') as fp:
                    return json.load(fp)
            except IOError:
                pass

    def save_user_info(self, save, name, password):
        for k in self.data.keys():
            if k == "save":
                self.data[k] = save
            if k == "name":
                self.data[k] = name
            if k == "password":
                self.data[k] = password
                self.save()

    def write(self, key, value):
        for k in self.data.keys():
            if k == key:
                self.data[k] = value
                self.save()

    def issaved(self):
        for k, v in self.data.items():
            if k == "save" and v == "False":
                return False
            else:
                return True

    def get(self, key):
        for k in self.data.keys():
            if k == key:
                return self.data[k]

    def getcamera(self):
        if self.data.get("camera") == "True":
            return True
        else:
            return False

    def getip(self):
        return self.data.get("ip")

    def getresolution(self):
        return self.data.get("resolution")

    def save(self):
        with open(self.file_name, 'w') as fp:
            json.dump(self.data, fp, indent=4)

    def resolution(self, value, value2):
        for k in self.data.keys():
            if k == "resolution":
                self.data[k] = [int(value), int(value2)]
                self.save()


print("- = "+__name__)