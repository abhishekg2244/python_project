class Git:
    def __init__(self,repository,branch):
        self.r1=repository
        self.b1=branch

    def show_repository(self):
        print(f"Reposiotyr:{self.r1}")

    def show_branch(self):
        print(f"Branch is: {self.b1}")

    def show_all(self):
        print(f"Reposiotyr:{self.r1}")
        print(f"Branch is: {self.b1}")

git=Git("DevOps-Learning","main")
git.show_repository()
git.show_branch()
git.show_all()