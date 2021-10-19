from typing import List, Dict, Any


class SceneItem:

    def __init__(self, cx: float, cy: float, alignment: int, name: str, identifier: int, render: bool, muted: bool,
                 locked: bool, source_cx: float, source_cy: float, srcType: float, volume: float, x: float, y: float,
                 parentGroupName: str, groupChildren: list = None):

        self.cx: float = cx
        self.cy: float = cy

        self.alignment: int = alignment
        self.name: str = name
        self.id: int = identifier
        self.render: bool = render
        self.muted: bool = muted
        self.locked: bool = locked

        self.source_cx: float = source_cx
        self.source_cy: float = source_cy

        self.srcType: float = srcType
        self.volume: float = volume

        self.x: float = x
        self.y: float = y

        self.parentGroupName: str = parentGroupName
        self.groupChildren: List[SceneItem] = groupChildren


def createFromDict(values: Dict[str, Any]) -> SceneItem:
    return SceneItem(values['cx'], values['cy'], values['alignment'], values['name'], values['id'], values['render'],
                     values['muted'], values['locked'], values['source_cx'], values['source_cy'], values['type'],
                     values['volume'], values['x'], values['y'], values['parentGroupName'], values['groupChildren'])
