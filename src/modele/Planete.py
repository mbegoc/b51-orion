class Planete(object):
    def __init__(self, parent,id):
        self.parent=parent
        self.id = id
        self.typeDev = None
        self.specialisation = None
        self.infrastructure = None
        
        
    def developInfrastructure (self):
        if self.specialisation == "education":
            self.typeDev=Education
            self.typeDev.developEducation ()
        
        
        

        