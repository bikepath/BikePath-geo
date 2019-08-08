from mesa_geo.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from model import GeoModel
from mesa_geo_folder.visualization.MapModule import MapModule


class HappyElement(TextElement):
    """
    Display a text count of how many happy agents there are.
    """

    def __init__(self):
        pass

    def render(self, model):
        return "Bike agents: " + str(model.num_bikes)


model_params = {
    "num_bikes": UserSettableParameter("slider", "Num Bikes", 10, 10, 20),
}


def road_draw(agent):
    """
    Portrayal Method for canvas
    """
    portrayal = dict()
    # if agent.atype is None:
    #     portrayal["color"] = "Grey"
    # elif agent.atype == 0:
    #     portrayal["color"] = "Red"
    # else:
    #     portrayal["color"] = "Blue"

    portrayal["color"] = "Blue"

    return portrayal


happy_element = HappyElement()
map_element = MapModule(road_draw, [42.3601, -71.0589], 14, 500, 500)
happy_chart = ChartModule([{"Label": "bikes", "Color": "Blue"}])
server = ModularServer(
    GeoModel, [map_element, happy_element, happy_chart], "BikePath", model_params
)
server.launch()
