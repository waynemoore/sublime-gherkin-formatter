class MockRegion():

  def __init__(self, a, b):
    self.a = long(a)
    self.b = long(b)


class MockView(object):

  def __init__(self, buffer):
    self.buffer = buffer

  def size(self):
    return len(self.buffer)

  def substr(self, region):
    return self.buffer[region.a:region.b]

  def replace(self, edit, region, string):
    self.buffer = string


class MockSublimePackage(object):

  Region = MockRegion
