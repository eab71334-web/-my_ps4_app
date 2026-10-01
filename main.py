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
            text="PS4 Full Controller Ready",
            size_hint=(1, 0.1),
            pos_hint={'x': 0, 'y': 0.88},
            font_size='20sp'
        )
        layout.add_widget(self.status)

        # --- أزرار الأكتاف العلوية (Shoulder Buttons) ---
        btn_l1 = Button(text="L1", size_hint=(0.18, 0.08), pos_hint={'x': 0.05, 'y': 0.78}, background_color=(0.3, 0.3, 0.3, 1))
        btn_l1.bind(on_press=lambda x: self.press_button("L1"))

        btn_l2 = Button(text="L2", size_hint=(0.18, 0.08), pos_hint={'x': 0.05, 'y': 0.68}, background_color=(0.2, 0.2, 0.2, 1))
        btn_l2.bind(on_press=lambda x: self.press_button("L2"))

        btn_r1 = Button(text="R1", size_hint=(0.18, 0.08), pos_hint={'x': 0.77, 'y': 0.78}, background_color=(0.3, 0.3, 0.3, 1))
        btn_r1.bind(on_press=lambda x: self.press_button("R1"))

        btn_r2 = Button(text="R2", size_hint=(0.18, 0.08), pos_hint={'x': 0.77, 'y': 0.68}, background_color=(0.2, 0.2, 0.2, 1))
        btn_r2.bind(on_press=lambda x: self.press_button("R2"))

        # --- أزرار النظام (Share / Options / PS) ---
        btn_share = Button(text="SHARE", size_hint=(0.12, 0.06), pos_hint={'x': 0.3, 'y': 0.75})
        btn_share.bind(on_press=lambda x: self.press_button("SHARE"))

        btn_options = Button(text="OPTIONS", size_hint=(0.12, 0.06), pos_hint={'x': 0.58, 'y': 0.75})
        btn_options.bind(on_press=lambda x: self.press_button("OPTIONS"))

        # --- أزرار التحكم الرئيسية (Right Side) ---
        btn_cross = Button(text="X", size_hint=(0.12, 0.12), pos_hint={'x': 0.75, 'y': 0.15}, background_color=(0, 0.5, 1, 1))
        btn_cross.bind(on_press=lambda x: self.press_button("Cross (X)"))

        btn_circle = Button(text="O", size_hint=(0.12, 0.12), pos_hint={'x': 0.85, 'y': 0.27}, background_color=(1, 0, 0, 1))
        btn_circle.bind(on_press=lambda x: self.press_button("Circle (O)"))

        btn_square = Button(text="[]", size_hint=(0.12, 0.12), pos_hint={'x': 0.65, 'y': 0.27}, background_color=(1, 0, 1, 1))
        btn_square.bind(on_press=lambda x: self.press_button("Square ([])"))

        btn_triangle = Button(text="/\\", size_hint=(0.12, 0.12), pos_hint={'x': 0.75, 'y': 0.39}, background_color=(0, 1, 0, 1))
        btn_triangle.bind(on_press=lambda x: self.press_button("Triangle (/\\)"))

        # --- أزرار الاتجاهات D-Pad (Left Side) ---
        btn_up = Button(text="^", size_hint=(0.12, 0.12), pos_hint={'x': 0.15, 'y': 0.39})
        btn_up.bind(on_press=lambda x: self.press_button("D-Pad UP"))

        btn_down = Button(text="v", size_hint=(0.12, 0.12), pos_hint={'x': 0.15, 'y': 0.15})
        btn_down.bind(on_press=lambda x: self.press_button("D-Pad DOWN"))

        btn_left = Button(text="<", size_hint=(0.12, 0.12), pos_hint={'x': 0.05, 'y': 0.27})
        btn_left.bind(on_press=lambda x: self.press_button("D-Pad LEFT"))

        btn_right = Button(text=">", size_hint=(0.12, 0.12), pos_hint={'x': 0.25, 'y': 0.27})
        btn_right.bind(on_press=lambda x: self.press_button("D-Pad RIGHT"))

        # إضافة جميع الأزرار للواجهة
        all_buttons = [
            btn_l1, btn_l2, btn_r1, btn_r2,
            btn_share, btn_options,
            btn_cross, btn_circle, btn_square, btn_triangle,
            btn_up, btn_down, btn_left, btn_right
        ]
        for btn in all_buttons:
            layout.add_widget(btn)

        return layout

    def press_button(self, btn_name):
        self.status.text = f"Pressed: {btn_name}"

if __name__ == '__main__':
    PS4App().run()
