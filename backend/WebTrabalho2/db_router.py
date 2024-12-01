
class DBRouter():
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'corrida_pessoa':
            return 'DBRunners'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'corrida_pessoa':
            return 'DBRunners'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'corrida_pessoa' or \
            obj2._meta.db_table == 'corrida_pessoa':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'WebTrabalho21':
            return db == 'DBRunners'
        return None
    
class DBRouter2():
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'RunnersList':
            return 'DBRunners2'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'RunnersList':
            return 'DBRunners2'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'RunnersList' or \
            obj2._meta.db_table == 'RunnersList':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'WebTrabalho2':
            return db == 'DBRunners2'
        return None