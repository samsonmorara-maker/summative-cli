class Project:
     def __init__(self, project_id, title):
         self.project_id = project_id 
         self.title = title 
         self.tasks = [] 
     def to_dict(self): 
         return { "project_id": self.project_id, "title": self.title, "tasks": self.tasks }