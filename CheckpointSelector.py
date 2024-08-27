class CheckpointSelectorWithMultipleCLIP:
    """
    A node to select a checkpoint and its corresponding CLIP model from multiple options.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "checkpoint_1": ("MODEL",),
                "clip_model_1": ("CLIP",),  # CLIP para el checkpoint 1
                "checkpoint_2": ("MODEL",),
                "clip_model_2": ("CLIP",),  # CLIP para el checkpoint 2
                "checkpoint_3": ("MODEL",),
                "clip_model_3": ("CLIP",),  # CLIP para el checkpoint 3
                "selection": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 3,
                    "step": 1,
                    "display": "number",  # Cambiado a "number" para entrada numérica
                    "lazy": True 
                }),
            },
        }

    RETURN_TYPES = ("MODEL", "CLIP")  # Devuelve el checkpoint y el CLIP seleccionado
    FUNCTION = "select_checkpoint"
    CATEGORY = "Model Selection"

    def select_checkpoint(self, checkpoint_1, clip_model_1, checkpoint_2, clip_model_2, checkpoint_3, clip_model_3, selection):
        if selection == 1:
            return (checkpoint_1, clip_model_1)
        elif selection == 2:
            return (checkpoint_2, clip_model_2)
        elif selection == 3:
            return (checkpoint_3, clip_model_3)
        else:
            raise ValueError("Selection must be between 1 and 3.")

# Map the node class to a unique name
NODE_CLASS_MAPPINGS = {
    "CheckpointSelectorWithMultipleCLIP": CheckpointSelectorWithMultipleCLIP
}

# Map the node name to a display-friendly name
NODE_DISPLAY_NAME_MAPPINGS = {
    "CheckpointSelectorWithMultipleCLIP": "Checkpoint Selector with Multiple CLIPs"
}

