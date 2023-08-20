import random

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line
from kivy.uix.button import Button
from kivy.uix.widget import Widget

Window.clearcolor = (1, 1, 1, 1)  # r,g,b,alpha


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)

        self.canvas.add(Color(rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0)))
        # print(touch) x and y coordinte of touch
        d = 50
        self.canvas.add(Line(size=(d, d), pos=(touch.x - d / 2, touch.y - d / 2)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


# root window = paint window + button
class ColorFusionApp(App):
    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        clearnBtn = Button(text='Clear' )  # pos = (0 ,600) , size = (100, 100 ) )
        clearnBtn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearnBtn)

        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


ColorFusionApp().run()

