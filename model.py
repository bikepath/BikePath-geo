from mesa_geo import GeoSpace, GeoAgent, AgentCreator
from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

# shp_roads='roads.shp'
# file_roads = open("roads.geojson")
# geojson_roads = file_roads.read()

class Road(GeoAgent):
    def __init__(self, unique_id, model, shape):
        super().__init__(unique_id, model, shape)

class GeoModel(Model):
    def __init__(self, num_bikes=10):
        self.grid = GeoSpace()
        self.num_bikes = 10
        
        road_agent_kwargs = dict(model=self)
        AC = AgentCreator(agent_class=Road, agent_kwargs=road_agent_kwargs)
        # agents = AC.from_GeoJSON(GeoJSON=geojson_roads, unique_id="osm_id")
        agents = AC.from_file("roads.geojson")
        print(agents[0].shape)
        self.grid.add_agents(agents)
        self.datacollector = DataCollector()

        self.running = True
        self.schedule = RandomActivation(self)

    def step(self):
        """Run one step of the model.

        If All agents are happy, halt the model.
        """
        self.schedule.step()
        self.datacollector.collect(self)