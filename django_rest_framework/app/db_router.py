class MultiDBRouter(object):
    """
    init 에서 app list 로 각각 어느 db로 보낼지 관리
    기본적으로 특정 db = 특정 list 1 대 1 매칭
    커스터마이징 하여 사용 가능
    """
    def __init__(self):
        self.first_list = ['default', 'pos', 'batch']
        self.second_list = ['mssql_server', 'common', 'combination', 'access', 'crm']
        self.third_list = ['batch', 'aianalysis']

    def db_for_read(self, model, **hints):
        if model is not None:
            print(f"MultiDBRouter mssql_server db_for_read model._meta.app_label : {model._meta.app_label}")
            if model._meta.app_label in self.first_list:  # in self.model_list:
                return 'pos'  # model._meta.app_label
            elif model._meta.app_label in self.second_list:
                return 'batch'
            return None

    def db_for_write(self, model, **hints):
        if model is not None:
            print(f"MultiDBRouter mssql_server db_for_write model._meta.app_label : {model._meta.app_label}")
            if model._meta.app_label in self.first_list:
                return 'pos'
            elif model._meta.app_label in self.second_list:
                return 'batch'
            return None

    def allow_relation(self, obj1, obj2, **hints):
        print(f"MultiDBRouter mssql_server allow_relation obj1._meta.app_label : {obj1._meta.app_label}")
        print(f"MultiDBRouter mssql_server allow_relation obj2._meta.app_label : {obj2._meta.app_label}")
        if obj1._meta.app_label in self.first_list \
                or obj2._meta.app_label in self.first_list:
            return True
        elif obj1._meta.app_label in self.second_list \
                or obj2._meta.app_label in self.second_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(f"MultiDBRouter mssql_server allow_migrate app_label : {app_label}")
        if app_label in self.first_list:
            return db == 'pos'
        elif app_label in self.second_list:
            return db == 'batch'
        return None
