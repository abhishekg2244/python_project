class Docker:
    def __init__(self,version, engine):
        self.version=version
        self.engine=engine
    
    def show_details(self):
        print(self.version)
        print(self.engine)
        
    

docker=Docker("1.272.0", "Dockerenginer")
docker.show_details()