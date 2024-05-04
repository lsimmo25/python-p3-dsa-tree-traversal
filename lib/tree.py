class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if not self.root:
            return None

        return self._find_element_by_id(self.root, id)

    def _find_element_by_id(self, current, id):
        if current.get("id") == id:
            return current

        for child in current.get("children", []):
            result = self._find_element_by_id(child, id)
            if result:
                return result
        return None
      