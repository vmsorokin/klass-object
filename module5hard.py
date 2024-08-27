class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
class Video:
    def __init__(self, title, duration, time_now =0, adult_mode = None, boll = False):
        self.title = title
        self.duration = duration
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
    def log_out(self):
        self.current_user = None
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
    def add(self, *args):
        for title in self.videos:
            if video.title == args:
                continue
            else: self.title.append(videos)



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)