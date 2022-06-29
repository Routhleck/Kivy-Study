from platform import platform
from kivy.config import Config
Config.set('graphics', 'width', '1600')
Config.set('graphics', 'height', '720')

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty, Clock
from kivy.uix.widget import Widget



class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    #竖线
    V_NB_LINES = 10
    V_LINE_SPACING = .25 # width百分比
    vertical_line = []

    #横线
    H_NB_LINES = 15
    H_LINE_SPACING = .1 # height百分比
    horizontal_line = []

    speed = 1
    current_offset_y = 0

    speed_x = 3
    current_speed_x = 0
    current_offset_x = 0
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("INIT W: " + str(self.width) + "H: " + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        
        # 键盘相应绑定
        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0 / 60.0)
    
    # 键盘相应
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None
    
    #判断是否为linux， Windows， MacOS
    def is_desktop(self):
        return platform()[:5] == 'linux' or platform()[:5] == 'Windo' or platform()[:5] == 'macos'
        

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.current_speed_x = self.speed_x
        elif keycode[1] == 'right':
            self.current_speed_x = - self.speed_x
        return True
    
    def on_keyboard_up(self, keyboard, keycode):
        self.current_speed_x = 0
        return True
    # 触控响应
    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            print("LEFT")
            self.current_speed_x = self.speed_x
        else:
            print("RIGHT")
            self.current_speed_x = -self.speed_x

    def on_touch_up(self, touch):
        self.current_speed_x = 0
    
    def on_parent(self, widget, parent):
        print("ON PARENT W: " + str(self.width) + "H: " + str(self.height))
    
    def on_size(self, *args):
        # print("ON SIZE W: " + str(self.width) + "H: " + str(self.height))
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height *0.75
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        pass
        

    def on_perspective_point_x(self, widget, value):
        # print("ON PERSPECTIVE X: " + str(value))
        pass
    
    def on_perspective_point_y(self, widget, value):
        # print("ON PERSPECTIVE Y: " + str(value))
        pass

    # 初始化竖线
    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            # self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_line.append(Line())
    # 更新竖线
    def update_vertical_lines(self):
        center_line_x = int(self.width / 2)
        spacing = self.V_LINE_SPACING * self.width
        offset = -int(self.V_NB_LINES/2) + 0.5
        for i in range(0, self.V_NB_LINES):
            line_x = int(center_line_x + offset * spacing + self.current_offset_x)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_line[i].points = [x1, y1, x2, y2]
            offset += 1
        # self.line.points = [center_x, 0, center_x, 100]
    
    # 初始化横线
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1,1,1)
            # self.line = Line(points=[100, 0, 100, 100])
            for i in range(0, self.H_NB_LINES):
                self.horizontal_line.append(Line())
    # 更新横线
    def update_horizontal_lines(self):
        center_line_x = int(self.width / 2)
        spacing = self.V_LINE_SPACING * self.width
        offset = -int(self.V_NB_LINES/2) + 0.5

        xmin = center_line_x + offset * spacing + self.current_offset_x
        xmax = center_line_x - offset * spacing + self.current_offset_x
        spacing_y = self.H_LINE_SPACING * self.height
        for i in range(0, self.H_NB_LINES):
            line_y = i * spacing_y - self.current_offset_y
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_line[i].points = [x1, y1, x2, y2]
    
    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)
    
    def transform_2D(self, x, y):
        return int(x), int(y)
    
    #转换成3D透视图，需要数学运算
    def transform_perspective(self, x, y):
        # TO DO
        lin_y = y * self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y
        
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y
        factory_y = diff_y / self.perspective_point_y # 1 when diff_y == self.perspective_point_y / 0 when diff_y == 0
        factory_y = factory_y * factory_y
        tr_x = self.perspective_point_x + diff_x * factory_y
        tr_y =self.perspective_point_y - factory_y * self.perspective_point_y
        return int(tr_x), int(tr_y)

    def update(self, dt):
        # print("dt: " + str(dt) + " - 1/60: " + str(1.0 / 60.0))
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y += self.speed * time_factor

        spacing_y = self.H_LINE_SPACING * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x += self.current_speed_x * time_factor
class GalaxyApp(App):
    pass

GalaxyApp().run()