"""Reference implementtation with using high-level API.
"""
from mjai import Bot


class RiichiBot(Bot):
    def __init__(self, player_id: int = 0):
        super().__init__(player_id)

    def think(self) -> str:
        if self.can_tsumo_agari:
            return self.action_tsumo_agari()
        elif self.can_ron_agari:
            return self.action_ron_agari()
        elif self.can_riichi:
            return self.action_riichi()

        if self.can_discard:
            candidates = self.find_improving_tiles()
            candidates = list(
                sorted(candidates, key=lambda x: len(x[1]), reverse=True)
            )
            for discard_tile, improving_tiles in candidates:
                return self.action_discard(discard_tile)
            return self.action_discard(self.last_self_tsumo)
        else:
            return self.action_nothing()
