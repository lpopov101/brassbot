from dataclasses import dataclass, field

from .eras import Era
from .location import Location
from .industries import IndustryType
from .deck import build_merchant_tile_deck
from .nodes import (
    CityNode,
    CityNodeIndustrySlot,
    MerchantNode,
    MerchantNodeBonusType,
    ConnectorNode,
)


CITY_NODES = [
    CityNode(
        Location.STOKE_ON_TRENT,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS]),
            CityNodeIndustrySlot([IndustryType.POTTERY, IndustryType.IRON]),
            CityNodeIndustrySlot(
                [IndustryType.COTTON, IndustryType.MANUFACTURED_GOODS]
            ),
        ],
    ),
    CityNode(
        Location.LEEK,
        [
            CityNodeIndustrySlot(
                [IndustryType.COTTON, IndustryType.MANUFACTURED_GOODS]
            ),
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.BELPER,
        [
            CityNodeIndustrySlot(
                [IndustryType.COTTON, IndustryType.MANUFACTURED_GOODS]
            ),
            CityNodeIndustrySlot([IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.POTTERY]),
        ],
    ),
    CityNode(
        Location.STONE,
        [
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.BEER]),
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.UTTOXETER,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.BEER]),
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.BEER]),
        ],
    ),
    CityNode(
        Location.DERBY,
        [
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.BEER]),
            CityNodeIndustrySlot(
                [IndustryType.COTTON, IndustryType.MANUFACTURED_GOODS]
            ),
            CityNodeIndustrySlot([IndustryType.IRON]),
        ],
    ),
    CityNode(
        Location.STAFFORD,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.BEER]),
            CityNodeIndustrySlot([IndustryType.POTTERY]),
        ],
    ),
    CityNode(
        Location.BURTON_ON_TRENT,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.BEER]),
        ],
    ),
    CityNode(
        Location.CANNOCK,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.COALBROOKDALE,
        [
            CityNodeIndustrySlot([IndustryType.IRON, IndustryType.BEER]),
            CityNodeIndustrySlot([IndustryType.IRON]),
            CityNodeIndustrySlot([IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.WOLVERHAMPTON,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS]),
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.WALSALL,
        [
            CityNodeIndustrySlot([IndustryType.IRON, IndustryType.MANUFACTURED_GOODS]),
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.BEER]),
        ],
    ),
    CityNode(
        Location.TAMWORTH,
        [
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.DUDLEY,
        [
            CityNodeIndustrySlot([IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.IRON]),
        ],
    ),
    CityNode(
        Location.BIRMINGHAM,
        [
            CityNodeIndustrySlot(
                [IndustryType.COTTON, IndustryType.MANUFACTURED_GOODS]
            ),
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS]),
            CityNodeIndustrySlot([IndustryType.IRON]),
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS]),
        ],
    ),
    CityNode(
        Location.NUNEATON,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.BEER]),
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.COAL]),
        ],
    ),
    CityNode(
        Location.KIDDERMINSTER,
        [
            CityNodeIndustrySlot([IndustryType.COTTON, IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.COTTON]),
        ],
    ),
    CityNode(
        Location.COVENTRY,
        [
            CityNodeIndustrySlot([IndustryType.POTTERY]),
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.IRON, IndustryType.MANUFACTURED_GOODS]),
        ],
    ),
    CityNode(
        Location.WORCESTER,
        [
            CityNodeIndustrySlot([IndustryType.COTTON]),
            CityNodeIndustrySlot([IndustryType.COTTON]),
        ],
    ),
    CityNode(
        Location.REDDITCH,
        [
            CityNodeIndustrySlot([IndustryType.MANUFACTURED_GOODS, IndustryType.COAL]),
            CityNodeIndustrySlot([IndustryType.IRON]),
        ],
    ),
    CityNode(Location.FARM1, [CityNodeIndustrySlot([IndustryType.BEER])]),
    CityNode(Location.FARM2, [CityNodeIndustrySlot([IndustryType.BEER])]),
]

CONNECTOR_NODES = [
    ConnectorNode(
        {Location.WARRINGTON, Location.STOKE_ON_TRENT}, {Era.CANAL, Era.RAIL}
    ),
    ConnectorNode({Location.STOKE_ON_TRENT, Location.LEEK}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.LEEK, Location.BELPER}, {Era.RAIL}),
    ConnectorNode({Location.BELPER, Location.DERBY}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.STOKE_ON_TRENT, Location.STONE}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.STONE, Location.UTTOXETER}, {Era.RAIL}),
    ConnectorNode({Location.UTTOXETER, Location.DERBY}, {Era.RAIL}),
    ConnectorNode({Location.NOTTINGHAM, Location.DERBY}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.STONE, Location.STAFFORD}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.STONE, Location.BURTON_ON_TRENT}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.DERBY, Location.BURTON_ON_TRENT}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.STAFFORD, Location.CANNOCK}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.BURTON_ON_TRENT, Location.CANNOCK}, {Era.RAIL}),
    ConnectorNode({Location.CANNOCK, Location.FARM1}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.CANNOCK, Location.WOLVERHAMPTON}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.CANNOCK, Location.WALSALL}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.BURTON_ON_TRENT, Location.WALSALL}, {Era.CANAL}),
    ConnectorNode({Location.BURTON_ON_TRENT, Location.TAMWORTH}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.TAMWORTH, Location.WALSALL}, {Era.RAIL}),
    ConnectorNode({Location.WOLVERHAMPTON, Location.WALSALL}, {Era.CANAL, Era.RAIL}),
    ConnectorNode(
        {Location.WOLVERHAMPTON, Location.COALBROOKDALE}, {Era.CANAL, Era.RAIL}
    ),
    ConnectorNode({Location.SHREWSBURY, Location.COALBROOKDALE}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.TAMWORTH, Location.NUNEATON}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.TAMWORTH, Location.BIRMINGHAM}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.STONE, Location.STAFFORD}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.WOLVERHAMPTON, Location.DUDLEY}, {Era.CANAL, Era.RAIL}),
    ConnectorNode(
        {Location.COALBROOKDALE, Location.KIDDERMINSTER}, {Era.CANAL, Era.RAIL}
    ),
    ConnectorNode({Location.DUDLEY, Location.KIDDERMINSTER}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.WALSALL, Location.BIRMINGHAM}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.TAMWORTH, Location.BIRMINGHAM}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.NUNEATON, Location.BIRMINGHAM}, {Era.RAIL}),
    ConnectorNode({Location.NUNEATON, Location.COVENTRY}, {Era.RAIL}),
    ConnectorNode({Location.COVENTRY, Location.BIRMINGHAM}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.BIRMINGHAM, Location.OXFORD}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.BIRMINGHAM, Location.REDDITCH}, {Era.RAIL}),
    ConnectorNode({Location.REDDITCH, Location.GLOUCESTER}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.WORCESTER, Location.GLOUCESTER}, {Era.CANAL, Era.RAIL}),
    ConnectorNode({Location.WORCESTER, Location.BIRMINGHAM}, {Era.CANAL, Era.RAIL}),
    ConnectorNode(
        {Location.WORCESTER, Location.KIDDERMINSTER, Location.FARM2},
        {Era.CANAL, Era.RAIL},
    ),
]


def setup_merchant_nodes(player_count: int) -> list[MerchantNode]:
    merchant_tile_deck = build_merchant_tile_deck(player_count)
    return [
        MerchantNode(
            Location.WARRINGTON,
            (
                [merchant_tile_deck.draw() for _ in range(2)]
                if player_count >= 3
                else []
            ),
            MerchantNodeBonusType.FIVE_POUNDS,
        ),
        MerchantNode(
            Location.NOTTINGHAM,
            (
                [merchant_tile_deck.draw() for _ in range(2)]
                if player_count >= 4
                else []
            ),
            MerchantNodeBonusType.THREE_VP,
        ),
        MerchantNode(
            Location.SHREWSBURY,
            [merchant_tile_deck.draw() for _ in range(2)],
            MerchantNodeBonusType.FOUR_VP,
        ),
        MerchantNode(
            Location.GLOUCESTER,
            [merchant_tile_deck.draw() for _ in range(2)],
            MerchantNodeBonusType.DEVELOP,
        ),
        MerchantNode(
            Location.OXFORD,
            [merchant_tile_deck.draw() for _ in range(2)],
            MerchantNodeBonusType.TWO_INCOME,
        ),
    ]


class BrassBoard:
    def __init__(self, player_count: int):
        self.location_nodes = CITY_NODES + setup_merchant_nodes(player_count)
        self.city_nodes = [
            node for node in self.location_nodes if isinstance(node, CityNode)
        ]
        self.merchant_nodes = [
            node for node in self.location_nodes if isinstance(node, MerchantNode)
        ]
        self.location_to_node = {node.location: node for node in self.location_nodes}
        self.connector_nodes = CONNECTOR_NODES
        self.location_to_connector_nodes = {}
        for connector_node in self.connector_nodes:
            for location in connector_node.connected_locations:
                if location not in self.location_to_connector_nodes:
                    self.location_to_connector_nodes[location] = []
                self.location_to_connector_nodes[location].append(connector_node)

    def location_is_in_player_network(self, location: Location, player_id: int) -> bool:
        if location not in self.location_to_connector_nodes:
            return False
        node = self.location_to_node[location]
        if not isinstance(node, CityNode):
            return False
        for industry_slot in node.industry_slots:
            if industry_slot.cur_industry.player_id == player_id:
                return True
        for connector_node in self.location_to_connector_nodes[location]:
            if connector_node.cur_player == player_id:
                return True
        return False

    def locations_are_connected(self, location1: Location, location2: Location) -> bool:
        if location1 not in self.location_to_connector_nodes:
            return False
        if location2 not in self.location_to_connector_nodes:
            return False
        start_node = self.location_to_node[location1]
        target_node = self.location_to_node[location2]
        visited_locations = set[Location]
        bfs_queue = [start_node]
        while len(bfs_queue) > 0:
            if node == target_node:
                return True
            node = bfs_queue.pop(0)
            visited_locations.add(node.location)
            for connector_node in self.location_to_connector_nodes[node.location]:
                if connector_node.cur_player is None:
                    continue
                for location in connector_node.connected_locations:
                    if (
                        location not in self.location_to_node
                        or location in visited_locations
                    ):
                        continue
                    bfs_queue.append(self.location_to_node[location])
        return False

    def get_connector_node_vp(self, connector_node: ConnectorNode) -> int:
        if connector_node.player_id is None:
            return 0
        player = connector_node.player_id
        vp = 0
        for location in connector_node.connected_locations:
            if location not in self.location_to_node:
                continue
            node = self.location_to_node[location]
            if isinstance(node, CityNode):
                for industry_slot in node.industry_slots:
                    if industry_slot.cur_industry is not None:
                        cur_industry = industry_slot.cur_industry
                        vp += cur_industry.connection_vp
            elif isinstance(node, MerchantNode):
                vp += 2
        return vp
