import chevron

import jimi

class _chevronFormat(jimi.action._action):
    templateData = dict()
    template = str()

    def doAction(self,data):
        templateData = jimi.helpers.evalDict(self.templateData, {"data" : data["flowData"]})
        template = jimi.helpers.evalString(self.template, {"data" : data["flowData"]})

        renderedTemplate = chevron.render(template, templateData)

        return {"result" : True, "rc" : 0, "renderedTemplate" : renderedTemplate}
