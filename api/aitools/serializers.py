import serpy

class TemplateAISerializer(serpy.Serializer):
    id = serpy.Field()
    name = serpy.Field()
    slug = serpy.Field()
    description = serpy.Field()
    human_example = serpy.Field()
    ai_example = serpy.Field()
    