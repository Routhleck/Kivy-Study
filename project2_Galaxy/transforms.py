
def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)
    
def transform_2D(self, x, y):
    return int(x), int(y)
    
    #转换成3D透视图，需要数学运算
def transform_perspective(self, x, y):
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