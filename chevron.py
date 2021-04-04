from core import plugin, model

class _chevron(plugin._plugin):
    version = 0.11

    def install(self):
        # Register models
        model.registerModel("chevronFormat","_chevronFormat","_action","plugins.chevron.models.action")
        return True

    def uninstall(self):
        # deregister models
        model.deregisterModel("chevronFormat","_chevronFormat","_action","plugins.chevron.models.action")
        return True
    
    def upgrade(self,LatestPluginVersion):
        return True
