import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class PS4App(App):
    def build(self):
        layout = FloatLayout()

        # شاشة نصية لعرض الأزرار المضغوطة
        self.status = Label(
            text="PS4 Controller Ready",
            size_hint=(1, 0.1),
            pos_hint={'x': 0, 'y': 0.85},
            font_size='20sp'
        )
        layout.add_widget(self.status)

        # زر CROSS (X)
        btn_cross = Button(
            text="X",
            size_hint=(0.15, 0.15),
            pos_hint={'x': 0.75, 'y': 0.15},
            background_color=(0, 0.5, 1, 1)
        )
        btn_cross.bind(on_press=lambda x: self.press_button("Cross (X)"))

        # زر CIRCLE (O)
        btn_circle = Button(
            text="O",
            size_hint=(0.15, 0.15),
            pos_hint={'x': 0.85, 'y': 0.3},
            background_color=(1, 0, 0, 1)
        )
        btn_circle.bind(on_press=lambda x: self.press_button("Circle (O)"))

        # زر SQUARE ([])
        btn_square = Button(
            text="[]",
            size_hint=(0.15, 0.15),
            pos_hint={'x': 0.65, 'y': 0.3},
            background_color=(1, 0, 1, 1)
        )
        btn_square.bind(on_press=lambda x: self.press_button("Square ([])"))

        # زر TRIANGLE (/\)
        btn_triangle = Button(
            text="/\\",
            size_hint=(0.15, 0.15),
            pos_hint={'x': 0.75, 'y': 0.45},
            background_color=(0, 1, 0, 1)
        )
        btn_triangle.bind(on_press=lambda x: self.press_button("Triangle (/\\)"))

        # إضافة الأزرار للواجهة
        layout.add_widget(btn_cross)
        layout.add_widget(btn_circle)
        layout.add_widget(btn_square)
        layout.add_widget(btn_triangle)

        return layout

    def press_button(self, btn_name):
        self.status.text = f"Pressed: {btn_name}"

if __name__ == '__main__':
    PS4App().run()
