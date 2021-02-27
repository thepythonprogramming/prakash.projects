import os
from instabot import Bot


class InstagramAutomation:
    # taking username and password to login
    def __init__(self, user_name, password, description):
        self.user_name = user_name
        self.password = password
        self.description = description

    # reading the first file from the directory
    def reading_first_file(self):
        first_file_name = os.listdir('C:\\Users\\reddy\\OneDrive\\Desktop 1\\Testing_program')
        return first_file_name[0]

    # only for logging in and uploading the picture
    def insta_bot(self):
        bot = Bot()
        caption = self.reading_first_file()[:-4]  # to remove ".jpj" from the file name
        bot.login(username=self.user_name, password=self.password)
        bot.upload_photo('C:\\Users\\reddy\\OneDrive\\Desktop 1\\Testing_program' + str(self.reading_first_file()),
                         caption=caption + self.description)

    # for deleting the picture after uploading
    def delete_file(self):
        os.remove('C:\\Users\\reddy\\OneDrive\\Desktop 1\\Testing_program' + str(self.reading_first_file()))


# your own hashtags and description
with open("hashtags.txt", "r") as file:
    data = file.read()

if __name__ == '__main__':
    testingprocess = InstagramAutomation(user_name="Your instagram id", password="Your password",
                                         description=data)
    testingprocess.reading_first_file()
    print(testingprocess.reading_first_file())
    testingprocess.insta_bot()
    testingprocess.delete_file()
