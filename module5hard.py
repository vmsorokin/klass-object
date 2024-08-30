class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __str__(self):
        return self.nickname
class Video:
    def __init__(self, title, duration, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
    def __eq__(self, other):
        return self.title == other.title
    def __contains__(self, item):
        return  item in self.title
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and user.password == password:
                self.current_user = user
    def log_out(self):
        self.current_user = None
    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
    def add(self, *videos):
        for new_video in videos:
            video_exist = False
            for v in self.videos:
                if new_video.title == v.title:
                    video_exist = True
                    print('Такое видео уже есть')
            if not video_exist:
                self.videos.append(new_video)
    def get_videos(self, text):
        list_mov = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_mov.append(video.title)
        return list_mov
    def watch_video(self, movie):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(x.duration):
                    print(i, end=' ')
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')

if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')