from kivy.app import App
from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import urllib.request

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        query = self.manager.current_screen.ids.user_query.text
        page = wikipedia.page(query)
        image_link = page.images[0]

        return image_link


    def download_image(self):
        a = 'files/image.jpg'
        req = urllib.request.urlretrieve(self.get_image_link(), a)

        return a

    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()





class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()

