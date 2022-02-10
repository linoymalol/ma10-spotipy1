from user.user import User




class Free_user(User):

    @deco
    def create_playlist(self, name, songs):
        super().create_playlist(name, songs)