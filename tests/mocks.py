class MockRegion(object):

  def __init__(self, a, b):
    self.a = long(a)
    self.b = long(b)

  def begin(self):
    return self.a


class MockRegionSet(object):

  def __init__(self):
    self.regions = []

  def add(self, region):
    self.regions.append(region)

  def clear(self):
    self.regions = []

  def __getitem__(self, key):
    print self.regions
    return self.regions[key]


class MockView(object):

  def __init__(self, buffer):
    self.buffer = buffer
    self.regions = MockRegionSet()

  def size(self):
    return len(self.buffer)

  def substr(self, region):
    return self.buffer[region.a:region.b]

  def replace(self, edit, region, string):
    self.buffer = string
    self.regions.clear()
    self.regions.add(MockRegion(len(self.buffer), len(self.buffer)))

  def sel(self):
    return self.regions


class MockSublimePackage(object):

  Region = MockRegion
