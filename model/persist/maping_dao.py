from view import maping

class MapingDAO:
	def __init__(self, myMap):
		self.map_obj = myMap

	def get_map(self):
		saveMap = self.map_obj.get_map_obj()
		returnObj = ''

		for mapElement in saveMap:
			returnObj += mapElement.element_type + '|' + str(mapElement.pos_x) + '|' + str(mapElement.pos_y) + '&'
			
		return returnObj			