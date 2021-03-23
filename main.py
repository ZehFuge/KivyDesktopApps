# *-* coding: utf-8 *-*
from kivy.app import App
from kivy.uix.button import Button

#-Lesson-6-------------------------------------------------------------------------------------------------------------#
# # Topic: Creating a window with a button and set its position and size
# # the App needs to be in a class to able to run
# # the class needs to end with "App" and the argument is "App" too
# class LanguageLearnerApp(App):
#     def build(self):
#         """
#         Set the position of the button with pos=(x_pos, y_pos).
#
#         For creating a button label, you need to use text="Button Label Text".
#
#         To set the size of the button, you need to set size_hint=(None, None). So you can pass the size of the
#         button with size=(y_size_from_pos/x_size_from_pos). But the button wount scale with window scaling. Some
#         widgets could be cut out.
#         Example: size_hint=(None, None)
#                  size=(50, 80)
#
#         If you want the button to scale with the window, you only use size_hint=(x_size_in_%, y_size_in_%).
#         Example: size_hint=(.8, .8)
#         This sets the button x_ and y_size to 80% of its parentsize (LanguageLearnerApp)
#         """
#         return Button(text="Hello World",
#                       pos=(50, 50),
#                       size_hint=(.2, .15)
#                       )
#
# if __name__ == "__main__":
#     LanguageLearnerApp().run()

#-Lesson-7-------------------------------------------------------------------------------------------------------------#
# # Topic: Create a class for a button and super initialize it
#
# class FunkyButton(Button):
#     def __init__(self, **kwargs):
          # super() is able initialize a class with already set vars
          # so this class can be called by the name without to need to create an object at first
#         super(FunkyButton, self,).__init__(**kwargs)
#         self.text="Funky button"
#         self.pos=(100, 100)
#         self.size_hint=(.25, .25)
#
# class LanguageLearnerApp(App):
#     def build(self):
#         return FunkyButton()
#
# if __name__ == "__main__":
#     LanguageLearnerApp().run()

#-Lesson-8-------------------------------------------------------------------------------------------------------------#
# # Topic:

class FunkyButton(Button):
    def __init__(self, **kwargs):
        super(FunkyButton, self,).__init__(**kwargs)
        self.text="Funky button"
        self.pos=(100, 100)
        self.size_hint=(.25, .25)

class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton()

if __name__ == "__main__":
    LanguageLearnerApp().run()
