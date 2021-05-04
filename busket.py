import os
import shutil


class work_with_files:
    def __init__(self, path):
        self.path = path

    def rename_file(self):

        try:

            if os.path.dirname(self.path):
                files_in_folder = os.listdir(self.path)
                print(files_in_folder)
                if len(files_in_folder) != 0:

                    for file_txt in files_in_folder:

                        user_choice = input("если вы хотите просто перенсти файл в другуб папку введите - NO, а если "
                                                "хотите перемиминовать файл прежде чем пренести введите - Yes>> ")
                        if user_choice == "Yes":
                            inp = input("Enter the namefile")
                            os.rename(f"{self.path}\{file_txt}", f"{self.path}\{inp}.txt")

                        elif user_choice == "NO":
                            os.rename(f"{self.path}\{file_txt}", f"{self.path}\{file_txt}")

        except FileNotFoundError:
                pass

    def move_in_bucket(self):
        files_in_folder = os.listdir(self.path)
        for renamed_files in files_in_folder:
            shutil.move(f"{self.path}\{renamed_files}", "C:\computer_busket")

    def watch_text_in_file(self):
        files_in_folder = os.listdir(self.path)
        for files in files_in_folder:
            with open(f"{self.path}\{files}", encoding="utf-8") as file:
                for words in file.read():
                    print(words, end='')
            print()
            print("Конец файла\n>>>")



if __name__ == "__main__":

    user = work_with_files('C:\\files')
    user_choice = input("Ваши действия с файлом(переименовать названией файлов, посмотреть текст файлов,"
                        "переместить в корзину) и нажмите - Enter>> ")

    if user_choice == "посмотреть текст файлов":
        print(user.watch_text_in_file())
    elif user_choice == "переименовать названией файлов":
        print(user.rename_file())
    elif user_choice == "переместить в корзину":
        print(user.move_in_bucket())
