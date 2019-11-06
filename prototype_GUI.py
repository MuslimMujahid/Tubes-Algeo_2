import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.stacklayout import StackLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown

class FaceRecognitionApp(App):
    def build(self):
        self.title = "Face Recognition"

        window = BoxLayout(orientation='vertical')
        image_panel = BoxLayout(orientation='horizontal')

        file_dd = DropDown(auto_width=False,width=400)
        choosef_btn = Button(text="Choose file...", size_hint_y=None, height= 25, halign='left')
        choosef_btn.text_size = (None,None)
        choosef_btn.bind(on_release=lambda btn: file_dd.select(choosef_btn.text))
        file_dd.add_widget(choosef_btn)

        percentage = Label(text="Match: n%,",size_hint=(1,.1))

        nav_bar = StackLayout(orientation='lr-bt',size_hint=(1,.1))
        top_bar = StackLayout(orientation='lr-tb',size_hint=(1,.1))
        menu_bar = StackLayout(orientation='lr-tb',size_hint=(1,.05))

        file_btn = Button(text="[u]F[/u]ile",size_hint=(.05,1),markup=True)
        file_btn.bind(on_release=file_dd.open)
        help_btn = Label(text="[u]H[/u]elp",size_hint=(.05,1),markup=True)

        next_btn = Button(text="Next",size_hint=(1/3,1))
        prev_btn = Button(text="Previous",size_hint=(1/3,1))
        detail_btn = ToggleButton(text="Detail",size_hint=(1/3,1))

        euclid_btn = ToggleButton(text="Euclidean Distance",size_hint=(1/2,1))
        cosine_btn = ToggleButton(text="Cosine Similarity",size_hint=(1/2,1))

        img1 = Image(source = './Aaron Paul0_262.jpg')
        img2 = Image(source = './Aaron Paul0_262.jpg')

        menu_bar.add_widget(file_btn)
        menu_bar.add_widget(help_btn)

        nav_bar.add_widget(prev_btn)
        nav_bar.add_widget(detail_btn)
        nav_bar.add_widget(next_btn)

        top_bar.add_widget(euclid_btn)
        top_bar.add_widget(cosine_btn)

        image_panel.add_widget(img1)
        image_panel.add_widget(img2)

        window.add_widget(menu_bar)
        window.add_widget(top_bar)
        window.add_widget(image_panel)
        window.add_widget(percentage)
        window.add_widget(nav_bar)
        
        return window

if __name__ == '__main__':
    FaceRecognitionApp().run()