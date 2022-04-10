import yaml


class GetCaseInfo:
    def get_case_info(self):
        casePath = "../case/case.yaml"
        f = open(casePath, 'r', encoding='utf-8')
        cont = f.read()
        case_info = yaml.load(cont, Loader=yaml.FullLoader)
        # {'case1': {'origin': 'select nickname from users;', 'current': 'select nickname from users_copy;'}}
        case_list = []
        for k, v in case_info.items():
            case_list.append({k: v})
        return case_list
        # [{'case1': {'origin': 'select nickname from users;', 'current': 'select nickname from users_copy;'}}]



if __name__ == '__main__':
    print(GetCaseInfo().get_case_info())