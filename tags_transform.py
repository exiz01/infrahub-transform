from infrahub_sdk.transforms import InfrahubTransform


class TagsTransform(InfrahubTransform):

    query = "tags_query"
    url = "https://webhook.site/de5d946f-adc7-4a59-8afb-c5652ad33c87"

    async def transform(self, data):
        tag = data["BuiltinTag"]["edges"][0]["node"]
        tag_name = tag["name"]["value"]
        tag_description = tag["description"]["value"]

        return {
            "tag_title": tag_name.title(),
            "bold_description": f"*{tag_description}*".upper()
        }
