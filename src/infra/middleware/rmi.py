from Pyro5.api import Proxy

const_adapters_list = [
    "adapters.create_user_adapter",
    "adapters.user_login_adapter",
    "adapters.login_user_with_username_adapter",
    "adapters.follow_user_adapter",
    "adapters.list_all_users_adapters",
    "adapters.list_others_users_adapter",
    "adapters.search_in_users_barn_adapter",
    "adapters.search_users_adapter",
    "adapters.unfollow_user_adapter",
    "adapters.update_photo_user_adapter",
    "adapters.update_user_adapter",
    "adapters.user_profile_adapter",
    "adapters.users_barn_adapter",
    "adapters.save_recipe_adapter",
    "adapters.search_recipe_adapter",
    "adapters.remove_recipe_adapter",
    "adapters.create_recipe_adapter",
    "adapters.list_recipe_adapter",
    "adapters.reaction_recipe_adapter",
    "adapters.search_recipe_barn_adapter",
    "adapters.create_file_adapter",
    "adapters.delete_file_adapter",
    "adapters.create_dive_adapter",
    "adapters.enter_dive_adapter",
    "adapters.exit_dive_adapter",
    "adapters.list_dive_recipes_adapter",
    "adapters.search_dive_adapter",
    "adapters.update_dive_adapter",
    "adapters.list_users_adapter",
    "adapters.create_ingredients_unit_adapter",
    "adapters.delete_ingredients_unit_adapter",
    "adapters.list_ingredients_unit_adapter",
    "adapters.search_dive_and_users_adapter"
]

class RMI:
    def __init__(self):
        self.adapters = const_adapters_list  # List of adapters
        
        self.services = {}  # Dictionary to store the services
        
        # Create a Proxy object for each adapter and store it in the services dictionary
        for adapter in self.adapters:
            self.services[adapter] = Proxy("PYRONAME:" + adapter)