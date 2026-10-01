import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class PS4App(App):
    def build(self):
        layout = FloatLayout()

        # شاشة نصية لعرض الحالة
        self.status = Label(
            text="PS4 Controller Layout Ready",
            size_hint=(1, 0.1),
            pos_hint={'x': 0, 'y': 0.85},
            font_size='20sp'
        )
        layout.add_widget(self.status)

        # --- أزرار التحكم الرئيسية (Right Side) ---
        # Cross (X)
        btn_cross = Button(text="X", size_hint=(0.12, 0.12), pos_hint={'x': 0.75, 'y': 0.15}, background_color=(0, 0.5, 1, 1))
        btn_cross.bind(on_press=lambda x: self.press_button("Cross (X)"))

        # Circle (O)
        btn_circle = Button(text="O", size_hint=(0.12, 0.12), pos_hint={'x': 0.85, 'y': 0.27}, background_color=(1, 0, 0, 1))
        btn_circle.bind(on_press=lambda x: self.press_button("Circle (O)"))

        # Square ([])
        btn_square = Button(text="[]", size_hint=(0.12, 0.12), pos_hint={'x': 0.65, 'y': 0.27}, background_color=(1, 0, 1, 1))
        btn_square.bind(on_press=lambda x: self.press_button("Square ([])"))

        # Triangle (/\)
        btn_triangle = Button(text="/\\", size_hint=(0.12, 0.12), pos_hint={'x': 0.75, 'y': 0.39}, background_color=(0, 1, 0, 1))
        btn_triangle.bind(on_press=lambda x: self.press_button("Triangle (/\\)"))

        # --- أزرار الاتجاهات D-Pad (Left Side) ---
        # Up
        btn_up = Button(text="^", size_hint=(0.12, 0.12), pos_hint={'x': 0.15, 'y': 0.39})
        btn_up.bind(on_press=lambda x: self.press_button("D-Pad UP"))

        # Down
        btn_down = Button(text="v", size_hint=(0.12, 0.12), pos_hint={'x': 0.15, 'y': 0.15})
        btn_down.bind(on_press=lambda x: self.press_button("D-Pad DOWN"))

        # Left
        btn_left = Button(text="<", size_hint=(0.12, 0.12), pos_hint={'x': 0.05, 'y': 0.27})
        btn_left.bind(on_press=lambda x: self.press_button("D-Pad LEFT"))

        # Right
        btn_right = Button(text=">", size_hint=(0.12, 0.12), pos_hint={'x': 0.25, 'y': 0.27})
        btn_right.bind(on_press=lambda x: self.press_button("D-Pad RIGHT"))

        # إضافة جميع الأزرار للواجهة
        for btn in [btn_cross, btn_circle, btn_square, btn_triangle, btn_up, btn_down, btn_left, btn_right]:
            layout.add_widget(btn)

        return layout

    def press_button(self, btn_name):
        self.status.text = f"Pressed: {btn_name}"

if __name__ == '__main__':
    PS4App().run()
