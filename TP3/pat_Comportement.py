class Observateur:
    """Interface pour les observateurs dans le pattern Observer."""

    
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method.")