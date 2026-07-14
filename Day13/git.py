class Git:
    def __init__(self,Repository, Branch):
        self.version=Repository
        self.engine=Branch
    
    def show_details(self):
        print(self.version)
        print(self.engine)
        

    

git=Git("DevOps-Learning","main")
git.show_details()