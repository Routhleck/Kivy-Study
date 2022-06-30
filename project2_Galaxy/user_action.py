# 键盘响应
def _keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None

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